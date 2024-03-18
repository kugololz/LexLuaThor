import ply.lex as lex

reserved = ['if','then','function','and','elseif','nil','return','while','break','end','not','do','false','in','true','else','for','local',
            'repeat','until','type','print','require','or','table']

# operadores = ['+','-','*','/','%','^','-','==','=','~=','<','>','>=','<=','#']

tokens = (
    'INT',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'FLOAT',
    'STRING',
    'IDENTIFIER',
    'RESERVED',
    'CORCHETE_DER',
    'CORCHETE_IZQ',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'OPERATOR',
    'COMA'
 )

t_CORCHETE_DER = r'\]'
t_CORCHETE_IZQ = r'\['
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_COMA = r'\,'


def t_OPERATOR(t):
    r'[+\-*/=><~#%^\.:]'
    t.type = 'OPERATOR'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.lower() in reserved:
        t.type = 'RESERVED'
    else:
        t.type = 'IDENTIFIER'
    return t

def t_STRING(t):
    r'\"([^\"\n]*?)(?<!\\)\"|\'([^\'\n]*?)(?<!\\)\'|"""([^"]*?)"""'
    t.value = t.value.strip('"').strip("'")
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+(?![\.\d])'
    t.value = int(t.value)
    return t
    
def t_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    

t_ignore = ' \t'

def t_error(t):
    print("Caracter invalido '%s'" % t.value[0] + ", in line: " + str(t.lexer.lineno))
    t.lexer.skip(1) 
    raise Exception("Error lexicografico.\n Por favor remueva el caracter invalido e intentelo de nuevo.\n Caracter invalido '%s'" % t.value[0] + ", en la linea: " + str(t.lexer.lineno))

    
def lexer_action(data):
    token_list =[]
    lexer = lex.lex()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type, tok.value, tok.lineno))
    return token_list
    
        