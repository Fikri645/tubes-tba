import re

# Token types
TOKEN_FOR = 'FOR'
TOKEN_SEMICOLON = 'SEMICOLON'
TOKEN_ASSIGNMENT = 'ASSIGNMENT'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_COMPARE_OP = 'COMPARE_OP'
TOKEN_ARITHMETIC_OP = 'ARITHMETIC_OP'
TOKEN_INCREMENT = 'INCREMENT'
TOKEN_DECREMENT = 'DECREMENT'
TOKEN_OPEN_BRACE = 'OPEN_BRACE'
TOKEN_CLOSE_BRACE = 'CLOSE_BRACE'
TOKEN_BOOLEAN = 'BOOLEAN'
TOKEN_DIGIT = 'DIGIT'
TOKEN_STRING = 'STRING'
TOKEN_WHITESPACE = 'WHITESPACE'
TOKEN_UNKNOWN = 'UNKNOWN'

# Grammar rules
GRAMMAR = {
    '<for_loop>': ['FOR', '<for_clause>', '<block>'],
    '<for_clause>': ['<init>', 'SEMICOLON', '<condition>', 'SEMICOLON', '<inc_dec_stmt>'],
    '<init>': ['<assignment>', 'SEMICOLON', '<condition>', 'SEMICOLON'],
    '<condition>': ['<identifier>', '<comparison_op>', '<identifier>'],
    '<inc_dec_stmt>': ['<identifier>', 'INCREMENT'],
    '<block>': ['OPEN_BRACE', '<assignment>', 'CLOSE_BRACE'],
    '<assignment>': ['<identifier>', 'ASSIGNMENT', '<expression>'],
    '<expression>': ['<operand>', '<arithmetic_op>', '<operand>'],
    '<arithmetic_op>': ['+', '-', '*', '/', '%'],
    '<operand>': ['<literal>', '<identifier>'],
    '<literal>': ['<boolean>', '<digit>', '<string>'],
    '<identifier>': ['<letter>', '<letter>', '<digit>'],
    '<letter>': ['a', 'b', 'c'],
    '<string>': ['`', '<string_characters>', '`'],
    '<string_characters>': ['<letter>', '<digit>', '<string_characters>', '<string_characters>'],
    '<digit>': ['0', '1', '2'],
    '<boolean>': ['true', 'false']
}


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]

    def parse(self):
        stack = ['<for_loop>']
        while stack:
            symbol = stack.pop()
            if symbol in GRAMMAR:
                production = GRAMMAR[symbol]
                for item in reversed(production):
                    stack.append(item)
            else:
                if not self.parse_terminal(symbol):
                    print("Susunan token tidak memenuhi aturan grammar")
                    return
        if self.current_token[0] != TOKEN_UNKNOWN:
            print("Susunan token memenuhi aturan grammar")
        else:
            print("Susunan token tidak memenuhi aturan grammar")

    def parse_terminal(self, terminal):
        if self.current_token[0] == terminal:
            self.advance()
            return True
        else:
            return False

    def advance(self):
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = (None, None)


# Tokenize input source code
def tokenize(source_code):
    tokens = []
    source_code = source_code.strip()
    while source_code:
        match = None
        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(source_code)
            if match:
                value = match.group(0)
                if token_type != TOKEN_WHITESPACE and token_type != TOKEN_UNKNOWN:
                    tokens.append((token_type, value))
                source_code = source_code[match.end():]
                break
        if not match:
            tokens.append((TOKEN_UNKNOWN, source_code[0]))
            return tokens  # Token tidak diterima
    return tokens


# Token patterns
TOKEN_PATTERNS = [
    (TOKEN_FOR, r'for'),
    (TOKEN_SEMICOLON, r';'),
    (TOKEN_ASSIGNMENT, r':='),
    (TOKEN_IDENTIFIER, r'[a-c]+'),
    (TOKEN_COMPARE_OP, r'==|!=|>|<|>=|<='),
    (TOKEN_ARITHMETIC_OP, r'\+|-|\*|/|%'),
    (TOKEN_INCREMENT, r'\+\+'),
    (TOKEN_DECREMENT, r'--'),
    (TOKEN_OPEN_BRACE, r'{'),
    (TOKEN_CLOSE_BRACE, r'}'),
    (TOKEN_BOOLEAN, r'true|false'),
    (TOKEN_DIGIT, r'[0-2]'),
    (TOKEN_STRING, r'`[a-c0-2]*`'),
    (TOKEN_WHITESPACE, r'\s+'),
    (TOKEN_UNKNOWN, r'.')
]

# Example usage
source_code = 'for a := 0; b < 2; b++ { a = a + 1 }'
tokens = tokenize(source_code)
parser = Parser(tokens)
parser.parse()
