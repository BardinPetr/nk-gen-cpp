import copy
import re
from typing import List, Dict, Tuple

from pycparser import parse_file, c_generator, c_parser, CParser, c_ast
from pygtrie import StringTrie

fname = "/home/petr/CLionProjects/trafficlight/GPIO.edl.h"

parser = CParser()

text = open(fname).read()
ast = parser.parse(text, fname)


class StructVisitor(c_ast.NodeVisitor):
    def __init__(self, ast: c_ast.Node):
        self.name_trie = StringTrie(separator="_")
        self.visit(ast)

    def visit_Struct(self, node: c_ast.Struct):
        name = node.name
        if name is None or node.decls is None: return
        self.name_trie[node.name] = node


class SelfUsageVisitor(c_ast.NodeVisitor):
    def __init__(self, self_name: str):
        self.self_name = self_name

    def visit_ID(self, node: c_ast.ID):
        if node.name == self.self_name:
            node.name = "this"


class FuncVisitor(c_ast.NodeVisitor):

    def __init__(self, ast: c_ast.Node, name_trie: StringTrie):
        self.method_rewrite: Dict[str, Tuple[str, str]] = {}
        self.name_trie = name_trie
        self.visit(ast)

    def visit_FuncDef(self, node: c_ast.FuncDef):
        decl: c_ast.Decl = node.decl
        name = decl.name
        base_name = re.sub("^_+", "", name)

        # find struct which could be base class for this method
        prefix = self.name_trie.longest_prefix(base_name)
        if not prefix: return
        class_name, struct_def = prefix.key, prefix.value

        # check if function has "self" argument
        params = decl.type.args.params
        if not params: return

        self_class = params[0].type.type.type
        if isinstance(self_class, c_ast.IdentifierType):
            self_class = self_class.names[0]
        elif isinstance(self_class, c_ast.Struct):
            self_class = self_class.name

        if self_class != class_name: return

        # deduct method name and register it for fast search of usages
        method_name = name.split(class_name + "_")[1]
        self.method_rewrite[name] = (class_name, method_name)

        # remove self argument
        self_arg = decl.type.args.params.pop(0)

        # replace self usages with "this" in func body
        SelfUsageVisitor(self_arg.name).visit(node.body)

        # remove static and add class identifier
        decl.storage.remove("static")

        self._set_name(decl, f"{class_name}::{method_name}")

        # insert func edf into struct with new name
        struct_func_decl = copy.deepcopy(decl)
        self._set_name(struct_func_decl, method_name)
        struct_def.decls.append(struct_func_decl)

    def _set_name(self, decl: c_ast.Decl, name: str):
        if isinstance(decl.type.type, c_ast.PtrDecl):
            decl.type.type.type.declname = name
        else:
            decl.type.type.declname = name

class MethodUsageVisitor(c_ast.NodeVisitor):

    def __init__(self, ast: c_ast.Node, method_rewrite: Dict[str, Tuple[str, str]]):
        self.method_rewrite = method_rewrite
        self.visit(ast)

    def visit_FuncCall(self, node: c_ast.FuncCall):
        name = node.name.name

        target_id = self.method_rewrite.get(name, None)
        if not target_id: return
        target_method = target_id[1]

        # remove self from args
        args: c_ast.ExprList = node.args
        base_obj: c_ast.StructRef = args.exprs.pop(0)

        # replace function name with this->method_name
        node.name = c_ast.StructRef(
            name=base_obj,
            type="->",
            field=c_ast.ID(target_method)
        )


class KOSFixesVisitor(c_ast.NodeVisitor):

    def visit_FuncDef(self, node: c_ast.FuncDef):
        node.body.block_items = [i for i in node.body.block_items if not isinstance(i, c_ast.TernaryOp)]


"""
NK uses "entity" and "component" postfixes to name Entity.
That happens because official docs also has problems with naming Entity as Component.
NK is using "_component" for structs and "_entity" for methods of entity class.
For now just calling everything a component
name = name.replace("_entity", "_component")
"""

struct_v = StructVisitor(ast)
func_v = FuncVisitor(ast, struct_v.name_trie)
MethodUsageVisitor(ast, func_v.method_rewrite)

# KOSFixesVisitor().visit(ast)

output = c_generator.CGenerator().visit(ast)

# fix for pycparser's way of printing attributes
# output = re.sub("(__typeof__\(\(\w+\)\s+[\w\s\->.]+\))", "(\\1)", output)

open(fname + ".out.hpp", "w").write(output)
