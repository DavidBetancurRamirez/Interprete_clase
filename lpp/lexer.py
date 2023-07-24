from re import match
from lpp.tokens import (
    Token,
    TokenType
)

class Lexer:
    def __init__(self,source:str) -> None:
        self._source:str=source        
        self._character:str=''        
        self._position:int=0        
        self._read_position:int=0
    
    def next_token(self) -> Token:
        # Tokens validos
        if match(r'^=$',self._character):
            token=Token(TokenType.ASSING,self._character)
        elif match(r'^;$',self._character):
            token=Token(TokenType.SEMICOLON,self._character)
        elif match(r'^($',self._character):
            token=Token(TokenType.LPAREN,self._character)
        elif match(r'^)$',self._character):
            token=Token(TokenType.RPAREN,self._character)
        elif match(r'^{$',self._character):
            token=Token(TokenType.LBRACE,self._character)
        elif match(r'^}$',self._character):
            token=Token(TokenType.RBRACE,self._character)
        elif match(r'^\+$',self._character):
            token=Token(TokenType.PLUS,self._character)
        elif match(r'^-$',self._character):
            token=Token(TokenType.MINUS,self._character)
        else:
            token=Token(TokenType.ILLEGAL, self._character)
        return token

    def _read_character(self) -> None:
        # Lectura del archivo
        if self._read_position>=len(self._source):
            self._character=''
        else:
            self._character=self._source[self._read_position]
        self._read_position=self._position
        self._read_position+=1
        