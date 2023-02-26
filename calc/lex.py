from enum import Enum


class Reader:
    _tape: list
    _head: int

    START_SYMBOL = "<"
    END_SYMBOL = ">"

    def __init__(self, expression: str = ""):
        self._tape = [*f"{self.START_SYMBOL}{expression}{self.END_SYMBOL}"]
        self._head = 0

    @property
    def size(self) -> int:
        return len(self._tape)

    @property
    def head(self) -> int:
        return self._head

    def peek(self) -> str:
        return self._tape[self._head + 1]

    def read(self) -> str:
        self._head += 1
        return self._tape[self._head]

    def is_empty(self) -> bool:
        return self.size == 2

    def eof(self) -> bool:
        return self._tape[self._head + 1] == self.END_SYMBOL

    def bof(self) -> bool:
        return self._tape[self._head] == self.START_SYMBOL

    def retract(self, count: int = 1) -> None:
        if not self.bof():
            if count == 1:
                self._head -= 1
            else:
                for _ in range(count):
                    self.retract()
        else:
            raise Exception(
                "Cannot retract the tape head past the beginning of the tape"
            )

    def __str__(self) -> str:
        return "".join(self._tape)[1:-1]


class TokenType(Enum):
    INTEGER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    LPAREN = 6
    RPAREN = 7
    EOF = 8


class Token:
    type: TokenType
    value: any

    def __init__(self, type: TokenType, value: any = None):
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type}, {self.value})"


class Input:
    def __init__(self):
        pass


class Scanner:
    def __init__(self):
        pass
