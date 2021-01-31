p_int = ?/[0-9]+/? ;
p_id_ = ?/[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z0-9_]+)*/? ;
p_id = ?/[a-zA-Z_]+/? ;
p_string = ?/".*?"/? ;

EOF = ?/\Z/? ;

INT = "int" ;

STRUCT = "struct" ;
LET = "let" ;
VAR = "var" ;
FN = "fn" ;
IF = "if" ;
THEN = "then" ;
ELSE = "else" ;
ELIF = "elif" ;
RETURN = "return" ;
BEGIN = "begin" ;
MODULE = "module" ;
END = "end" ;
JMP = "jmp" ;
BREAK = "brk" ;
DEFER = "defer" ;

EQ = "=" ;
PIPE = "|" ;
SPIPE = "|>" ;
DOLLAR = "$" ;
BACKSLASH = "\\" ;
DOUBLE_COLON = "::" ;
COLON = ":" ;
SEMICOLON = ";" ;
COMMA = "," ;
ARROW = "->" ;
HASH = "#" ;

LPAREN = "(" ;
RPAREN = ")" ;
LBRACE = "{" ;
RBRACE = "}" ;
LBRACK = "[" ;
RBRACK = "]" ;

start = 
      {p_node} EOF ;

p_node = 
      name:p_id DOUBLE_COLON [ LBRACK includes:{p_id} RBRACK ] 
      [ LPAREN [ args+:p_field { COMMA args:{p_field} } ] RPAREN ARROW type:p_type ] 
      LBRACE elems:{p_elem} RBRACE ;

p_elem = 
      var:p_var
    | stm:p_stm
    | node:p_node ;

p_var =
      VAR name:p_id_ COLON type:p_type SEMICOLON ;

p_field =
      name:p_id_ COLON type:p_type ;

p_type =
      type_prim:p_type_prim
    | type_fn:p_type_fn ;

p_type_prim =
      name:p_id ;

p_type_fn =
      LPAREN [args+:p_type {COMMA args+:p_type}] RPAREN ARROW return_type:p_type ;

p_exp_basic =
      LPAREN @:p_exp RPAREN
    | exp_int:p_int
    | exp_str:p_string
    | exp_id:p_id ;

p_exp_app =
      l:p_exp_basic r:{p_exp_app} ;

p_exp_spipe =
      l:p_exp_app {SPIPE r:p_exp_spipe} ;

p_exp_dollar =
      l:p_exp_spipe {DOLLAR r:p_exp_dollar} ;

p_exp =
      @:p_exp_dollar ;

p_stm_let =
      LET name:p_id_ COLON type:p_type EQ val:p_exp ;

p_stm =
      stm_exp:p_exp SEMICOLON
    | stm_let:p_stm_let SEMICOLON
    | stm_ret:(RETURN (() | @:p_exp)) SEMICOLON
    | stm_jmp:(JMP (() | name:p_id_)) SEMICOLON
    | stm_brk:(BREAK (() | name:p_id_)) SEMICOLON ;