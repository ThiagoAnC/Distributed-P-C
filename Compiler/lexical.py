def lexical(f,i):

    aux = ''
    line = f.readline()
    if line[0].isalpha():
        while line[i].isalpha():
            aux = aux + line
            i += 1
        return (aux + ' ' + str(i))

def spliter(token):
    token,stop = token.split()
    return int(stop)

def tamanho(f):
    lines = 0
    for line in f:
        print(line, end='')
        lines += 1
    return lines

#inicio
f = open("Compiler\entry.txt")
try:
    token = lexical(f,0)
    spliter(token)
finally:
    f.close()