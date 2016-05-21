from token import Token

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', '(', ')', 'EOF'
)


def is_number(s):
    try:
        complex(s)  # for int, long, float and complex
    except ValueError:
        return False
    return True


def join_numbers(tokens):
    numbers_to_join = []
    for i in tokens:
        if (i.type == INTEGER):
            numbers_to_join.append(i.value)
        elif (i.type != INTEGER):
            return numbers_to_join


def join_list(list):
    list = "".join(list)
    return int(list)


def join_tokens(tokens):
    joined_tokens = []
    length = 0
    for i in range(tokens.__len__()):
        if (length == 0):
            if (tokens[i].type == INTEGER):
                join_numbers2 = join_numbers(tokens[i:])
                length = join_numbers2.__len__()
                joined_tokens.append(Token(INTEGER,join_list(join_numbers2)))
            elif (tokens[i].type != INTEGER):
                joined_tokens.append(tokens[i])
                length = 1
        length = length - 1
    return joined_tokens


def scan(string):
    string.split()
    string.join("")
    token_list = []
    for i in string:
        if (is_number(i)):
            token_list.append(Token(INTEGER, i))
        elif (i == "+"):
            token_list.append(Token(PLUS, i))
        elif (i == "-"):
            token_list.append(Token(MINUS, i))
        elif (i == "*"):
            token_list.append(Token(MULTIPLY, i))
        elif (i == "/"):
            token_list.append(Token(DIVIDE, i))
        elif (i == "("):
            token_list.append(Token(LPAREN, i))
        elif (i == ")"):
            token_list.append(Token(RPAREN, i))

    token_list.append(Token(EOF, None))
    return token_list
