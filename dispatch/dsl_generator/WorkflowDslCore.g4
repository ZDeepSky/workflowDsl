// WorkflowDslCore.g4
// 当前只实现没有收发消息的同步动作：一行一个函数名，ignore 可选。
// receive / send / delay / async / if / while / call / fail 后续再加。
grammar WorkflowDslCore;

workflowFile
    : (workflow | procedure)* EOF
    ;

workflow
    : NEWLINE? 'workflow' procedureBody
    ;

procedure
    : NEWLINE? 'procedure' procedureBody
    ;

procedureBody
    : identifier '{' NEWLINE sequenceAction '}' NEWLINE?
    ;

sequenceAction
    : action*
    ;

action
    : syncAction
    ;

// [ignore] Func
syncAction
    : Ignore? function NEWLINE
    ;


function: ID;
identifier: ID;
Ignore: 'ignore';

ID: ID_LETTER (ID_LETTER | DIGIT)*;

// 换行是 token：前面可以夹空格、块注释、行注释；连续空行合成一个 NEWLINE。
// 带 -> skip 的规则不能再被别的词法规则引用，所以空白和注释拆成 fragment。
NEWLINE
    : ((SPACES | BLOCK_COMMENT | EOL_COMMENT)* (('\r\n') | '\n'))+
    ;

SPACE
    : SPACES -> skip
    ;

COMMENT
    : BLOCK_COMMENT -> skip
    ;

LINE_COMMENT
    : EOL_COMMENT -> skip
    ;

fragment SPACES
    : [ \t]+
    ;

fragment BLOCK_COMMENT
    : '/*' .*? '*/'
    ;

fragment EOL_COMMENT
    : '//' ~[\r\n]*
    ;

fragment ID_LETTER
    : 'a'..'z' | 'A'..'Z' | '_'
    ;

fragment DIGIT
    : '0'..'9'
    ;
