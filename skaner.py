from token import Token
NUMBER, PLUS, EOF, MULTIPLE, MINUS = 'NUMBER', 'PLUS', 'EOF', 'MULTIPLE', 'MINUS'

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True

def join_numbers(tokens):
    numbers_to_join = []
    for i in tokens:
        if (i.type == NUMBER):
            numbers_to_join.append(i.value)
        elif (i.type != NUMBER):
            return numbers_to_join

def join_list(list):
    list = "".join(list)
    return int(list)

def join_tokens(tokens):
    joined_tokens = []
    length = 0
    for i in range(tokens.__len__()):
        if (length == 0):
            if (tokens[i].type == NUMBER):
                join_numbers2 = join_numbers(tokens[i:])
                length = join_numbers2.__len__()
                joined_tokens.append(Token(NUMBER,join_list(join_numbers2)))
            elif (tokens[i].type != NUMBER):
                joined_tokens.append(tokens[i])
                length = 1
        length = length - 1
    return joined_tokens

def skan(string):
    string.split();
    string.join("")
    token_list = []
    for i in string:
        if (is_number(i)):
            token_list.append(Token(NUMBER, i))
        elif (i == "+"):
            token_list.append(Token(PLUS,i))
        elif (i == "-"):
            token_list.append(Token(MINUS, i))
        elif (i == "*"):
            token_list.append(Token(MULTIPLE, i))
    token_list.append(Token(EOF,None))
    return token_list


print(join_tokens(skan("243+15 4 *1 00")))