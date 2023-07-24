from enum import (
    auto,
    Enum,
    unique,
    Dict
)
from typing import NamedTuple


@unique
class TokenType(Enum):
    # Tipos de tokens
    ASSING=auto()#
    COMMA=auto()
    EOF=auto()
    FUNCTION=auto()
    IDENT=auto()
    ILLEGAL=auto()#
    INT=auto()
    LBRACE=auto()#
    LET=auto()
    LPAREN=auto()#
    MINUS=auto()#
    PLUS=auto()#
    RBRACE=auto()#
    RPAREN=auto()#
    SEMICOLON=auto()#



class Token(NamedTuple):
    token_type: TokenType
    literal:str

    def __str__(self) -> str:
        return f'Type {self.token_type}, literal {self.literal}'
    
    def lookup_token_type(literal:str) -> TokenType:
        # Palabras reservadas
        keywords:Dict[str,TokenType]={
            'variable':TokenType.LET,
            'function':TokenType.FUNCTION
        }
        return keywords.get(literal,TokenType.IDENT)
    