from token import Token
NUMBER, PLUS, EOF, MULTIPLE, MINUS = 'NUMBER', 'PLUS', 'EOF', 'MULTIPLE', 'MINUS'

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True

def join_tokens(token_list,splitted_value):
    length = token_list.__len__();
    print(length)
    if (length>1):
        if (token_list[0].type == NUMBER and token_list[1].type == NUMBER):
            print("here")
            splitted_value.append(Token(NUMBER,token_list[0].value+token_list[1].value))
            return join_tokens(splitted_value + token_list[2:],splitted_value)
        else:
            splitted_value.append(token_list[0])
            return join_tokens(token_list[1:])

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
    return token_list


print(skan("24+54-6"))