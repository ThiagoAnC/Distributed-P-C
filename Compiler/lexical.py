def expr(item):
    aux = str(dictionary[item])
    escape,exp = aux.split('[\'')
    exp,escape = exp.split('\']')
    return str(exp)

def lexical(ind):
    aux = ''
    exp = expr(ind+1)
    nex = ind
    lenght = len(exp)
    print (exp[ind])
    while True:
        if exp[ind].isalpha():
                while exp[nex].isalpha():
                    if exp[nex+1].isalpha() or exp[nex+1].isdigit() or exp[nex+1] == '_':
                        nex += 1
                    else:
                        break
                return (str(nex) + str(ind))
        else:
            print ("invalid id token, in line " + str(ind))
            return '$'
    return '$'

def spliter(token):
    if token == '':
        return 1
    token,stop = token.split()
    return int(stop)

def tamanho(f):
    global lines
    lines = 0
    mat = {}

    for line in f:
        lines += 1
        mat[lines] = line.splitlines()
    return (mat)

#inicio        
with open('Compiler\entry.txt') as f:
    try:
        global dictionary
        dictionary = tamanho(f)
        while True:
            token = ''
            token = lexical(0)
            print (token)
            token = ''
            if token == '$' or token == '':
                break
    finally:
        f.close()