import re
from io import TextIOBase
from sqlparse import tokens, keywords

class Lexer:
    def __init__(self):
        self._SQL_REGEX = []
        self._keywords = []
        self.default_initialization()

    def default_initialization(self):
        self.clear()
        self.set_SQL_REGEX(keywords.SQL_REGEX)
        self.add_keywords(keywords.KEYWORDS_COMMON)
        self.add_keywords(keywords.KEYWORDS)

    def clear(self):
        self._SQL_REGEX = []
        self._keywords = []

    def set_SQL_REGEX(self, SQL_REGEX):
        FLAGS = re.IGNORECASE | re.UNICODE
        self._SQL_REGEX = [
            (re.compile(rx, FLAGS).match, tt)
            for rx, tt in SQL_REGEX
        ]

    def add_keywords(self, keywords_dict):
        self._keywords.append(keywords_dict)

    def is_keyword(self, value):
        val = value.upper()
        for kwdict in self._keywords:
            if val in kwdict:
                return kwdict[val], value
        return tokens.Name, value

    def get_tokens(self, text, encoding=None):
        if isinstance(text, TextIOBase):
            text = text.read()

        if isinstance(text, bytes):
            text = text.decode(encoding or 'utf-8', errors='replace')
        elif not isinstance(text, str):
            raise TypeError(f"Expected str or file-like object, got {type(text)}")

        text_len = len(text)
        pos = 0
        while pos < text_len:
            for rexmatch, action in self._SQL_REGEX:
                m = rexmatch(text, pos)
                if not m:
                    continue
                if isinstance(action, tokens._TokenType):
                    yield action, m.group()
                elif action is keywords.PROCESS_AS_KEYWORD:
                    yield self.is_keyword(m.group())
                pos = m.end()
                break
            else:
                yield tokens.Error, text[pos]
                pos += 1


def tokenize(sql, encoding=None):
    lexer = Lexer()
    return lexer.get_tokens(sql, encoding)

# Testing the Lexer
if __name__ == "__main__":
    sql=input("Enter SQL query: ")
    for token_type, value in tokenize(sql):
        print(token_type, repr(value))
