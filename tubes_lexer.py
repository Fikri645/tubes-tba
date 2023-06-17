import re

# Token types
TOKEN_FOR = 'FOR'
TOKEN_SEMICOLON = 'SEMICOLON'
TOKEN_BOOLEAN = 'BOOLEAN'
TOKEN_COMPARE_OP = 'COMPARE_OP'
TOKEN_ARITHMETIC_OP = 'ARITHMETIC_OP'
TOKEN_INIT = 'INITIALIZE'
TOKEN_ASSIGNMENT = 'ASSIGNMENT'
TOKEN_INCREMENT = 'INCREMENT'
TOKEN_DECREMENT = 'DECREMENT'
TOKEN_OPEN_BRACE = 'OPEN_BRACE'
TOKEN_CLOSE_BRACE = 'CLOSE_BRACE'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_DIGIT = 'DIGIT'
TOKEN_WHITESPACE = 'WHITESPACE'
TOKEN_UNKNOWN = 'UNKNOWN'

# Regular expressions for token patterns
TOKEN_PATTERNS = [
    (TOKEN_FOR, r'for'),
    (TOKEN_SEMICOLON, r';'),
    (TOKEN_BOOLEAN, r'(true|false)'),
    (TOKEN_COMPARE_OP, r'==|!=|>|<|>=|<='),
    (TOKEN_ARITHMETIC_OP, r'\+|-|\*|/|%'),
    (TOKEN_INIT, r':='),
    (TOKEN_ASSIGNMENT, r'='),
    (TOKEN_INCREMENT, r'\+\+'),
    (TOKEN_DECREMENT, r'--'),
    (TOKEN_OPEN_BRACE, r'\{'),
    (TOKEN_CLOSE_BRACE, r'\}'),
    (TOKEN_IDENTIFIER, r'(a|b|c)'),
    (TOKEN_DIGIT, r'(0|1|2)'),
    (TOKEN_WHITESPACE, r'\s+'),
    (TOKEN_UNKNOWN, r'.')
]

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
            source_code = source_code[1:]
    return tokens

# Example usage
source_code = 'for a := 0; a < 2; i++ { c = a / b }'
tokens = tokenize(source_code)
for token_type, value in tokens:
    print(f'Token: {token_type}, Value: {value}')
    
