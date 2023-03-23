# this file will contain functions used to comparer and make the lexer.py file cleaner

def is_letter(ch):
    if ch != ' ' and ch != ';' and ch != '(' and ch !=  ')' and ch != '<' and ch != '>' and ch != '=':
        return True
    else:
        return False
    

def is_seperator(ch):
    if ch == '(' or  ch == ')' or ch == ';' or ch == '{' or ch == '}' or ch == '[' or ch ==  ']':
        return True
    else:
        return False
    
def is_keyword(word):
    if word == ("while" or "for" or "double" or "else" or "float" or "int" or "long" or "short" or "struct"):
        return True
    else:
        return False
    
def is_operator(ch):
    if ch == '<' or ch == '>' or ch == '=':
        return True
    else:
        return False
        
    

