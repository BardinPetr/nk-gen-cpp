grammar IDL;

idl: statement_package statements interface EOF;

interface: 'interface' '{' method_block '}';

statements:         statement*;
statement:          statement_const | statement_typedef | statement_import | statement_struct | statement_union;

statement_struct:    'struct' ID '{' declaration_block '}';
statement_union:     'union' ID '{' declaration_block '}';
statement_package:   'package' PACKAGE_ID;
statement_import:    'import' PACKAGE_ID;
statement_typedef:   'typedef' type ID ';';
statement_const:     'const'   const_type ID '=' INT ';';
const_type:          TYPE_PRIMITIVE | ID;

method_block:        (method ';')*;
method:              ID '(' method_arguments? ')';
method_arguments:    method_argument (',' method_argument)*;
method_argument:     ARG_DIRECTION declaration;

declaration_block:   (declaration ';')*;
declaration:         type ID;

type: ID
    | TYPE_PRIMITIVE
    | type_arr
    | type_arr_generic;

type_arr: TYPE_ARR '<' (INT | ID) '>';
type_arr_generic: TYPE_ARR_GENERIC '<' type ',' (INT | ID) '>';

TYPE_PRIMITIVE: TYPE_SINT | TYPE_UINT | TYPE_HANDLE;
TYPE_SINT:      'SInt8' | 'SInt16' | 'SInt32' | 'SInt64';
TYPE_UINT:      'UInt8' | 'UInt16' | 'UInt32' | 'UInt64';
TYPE_HANDLE:    'Handle';

TYPE_ARR:       TYPE_BYTES | TYPE_STRING;
TYPE_BYTES:     'bytes';
TYPE_STRING:    'string';

TYPE_ARR_GENERIC: TYPE_ARRAY | TYPE_SEQUENCE;
TYPE_ARRAY:     'array';
TYPE_SEQUENCE:  'sequence';

ARG_DIRECTION: 'in' | 'out' | 'error';

INT: [0-9]+ | INT_HEX;
INT_HEX: '0x' [a-fA-F0-9]+;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
PACKAGE_ID: [a-zA-Z_][a-zA-Z_0-9.]*;

COMMENT:    '/*' .*? '*/' -> skip;
OL_COMMENT: '//' .*? '\n' -> skip;
SPACE:      [ \t\n]+ -> skip;

