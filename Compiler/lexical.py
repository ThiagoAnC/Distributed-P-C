def lexical(f,i):
    token = ''
    aux = f.read(i)
    while (aux != '$'):
        if (not aux.isspace()):
            token = token + aux
        aux = f.read(i+1)
        if token == "aux":
            print ("Token:" + token.strip() + " Tipo: ID")
            return (token + ' ' + str(i+1))
        if token == '<-':
            print ("Token:" + token.strip() + " Tipo: ATTR")
            return (token + ' ' + str(i+1))
        i += 1
        if i > 15:
            break

#inicio
f = open("Compiler\entry.txt", "r")

point = lexical(f,0)
print(point.split())