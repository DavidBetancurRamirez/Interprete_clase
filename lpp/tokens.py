from enum import (
    auto,
    Enum,
    unique,
    
)
from typing import (
    NamedTuple,
    Dict
)


@unique
class TokenType(Enum):
    ASSING=auto()
    COMMA=auto()
    DIVISION=auto()
    EQ=auto()
    ELSE=auto()
    ELSEIF=auto()
    EOF=auto()
    FOR=auto()
    FUNCTION=auto()
    GT=auto()
    GTE=auto()
    IDENT=auto()
    ILLEGAL=auto()
    IF=auto()
    INT=auto()
    LBRACE=auto()
    LET=auto()
    LPAREN=auto()
    LT=auto()
    LTE=auto()
    NEGATION=auto()
    MINUS=auto()
    MULTIPLICATION=auto()
    NEQ=auto()
    PLUS=auto()
    RBRACE=auto()
    RPAREN=auto()
    RETURN=auto()
    SEMICOLON=auto()

class Token(NamedTuple):
    token_type:TokenType
    literal:str
    def __str__(self) -> str:
        return f'Type {self.token_type}, Literal {self.literal}'
    
def lookup_token_type(literal:str)->TokenType:
    keywords:Dict[str,TokenType]={
        'variable':TokenType.LET,
        'funcion':TokenType.FUNCTION,
        'para':TokenType.FOR,
        'regresa':TokenType.RETURN,
        'si':TokenType.IF,
        'si_no':TokenType.ELSE,
        'si_no_si':TokenType.ELSEIF
    }
    return keywords.get(literal,TokenType.IDENT)
