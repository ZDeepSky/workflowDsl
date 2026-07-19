grammar WorkflowDSL;

program
    : (stepAlias | conditionAlias | workflowDef | actionBinding)* EOF
    ;

stepAlias
    : '@action' IDENT '=' IDENT
    ;

conditionAlias
    : '@condition' IDENT '=' IDENT
    ;

workflowDef
    : 'workflow' IDENT '{' statement* '}'
    ;

statement
    : 'action' IDENT                     # ActionStmt
    | 'send' IDENT                       # SendStmt
    | 'recv' IDENT                       # RecvStmt
    | 'goto' IDENT                       # GotoStmt
    | 'if' IDENT ':' statement           # IfBlock
    | 'while' 'not' IDENT ':' statement  # WhileBlock
    | 'final' ':' statement              # FinalBlock
    ;

actionBinding
    : 'action' IDENT '=' IDENT
    ;

IDENT     : [a-zA-Z_] [a-zA-Z0-9_]* ;
COMMENT   : '//' ~[\r\n]* -> skip ;
WS        : [ \t\r\n]+ -> skip ;
