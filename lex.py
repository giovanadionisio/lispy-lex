import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    tokens = [
        ("LPAR", r"\("),
        ("RPAR", r"\)"),
        ("NUMBER", r"(?:-|\+)?\d*\.?\d+"),
        ("NAME", r"(?:;.*|\.\.\.|[+\-\.\*\/<=>!?:$_&~^']|%[a-zA-z]*|[a-zA-z](?:[a-zA-z%?!]*(?:->|-)?)*)"),
        ("CHAR", r"#\\(?:[a-zA-z]+|.)"),
        ("BOOL", r"#t|#f"),
        ("STRING", r"\"(?:[^\"\\\b\f\n\r\t]|\\[\"\\/bfnrt]|u[0-9a-fA-F]{4})*\""),
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)

    return [Token('INVALIDA', 'valor inválido')]