def lexical(f,i):
    #token = ' '
    aux = f.read(i)
    print (aux)
    while True:
        if (aux.isalpha()):
            print (aux)
            #print ("Token:" + token.strip() + " Tipo: ID")
            return (token + ' ' + str(i))
        
        elif (aux == '"'):
            print (aux)
            #print ("Token:" + token + " Tipo: Literal")
            return (token + ' ' + str(i))
        
        elif (aux.isdigit()):
            print (aux)
            #print ("Token:" + token + " Tipo: Num")
            return (token + ' ' + str(i))
        
        elif (aux == '{'):
            print (aux)
            #print ("Token:" + token + " Tipo: comment")
            return (token + ' ' + str(i))
        
        elif (aux == '<'):
            print (aux)
            #print ("Token:" + token + " Tipo: OPR")
            return (token + ' ' + str(i))
       
        elif (aux == '>'):
            print (aux)
            #print ("Token:" + token + " Tipo: OPR")
            return (token + ' ' + str(i))
        
        elif (aux == '+' or aux == '-' or aux == '*' or aux == '/'):
            print (aux)
            #print ("Token:" + token + " Tipo: OPM")
            return (token + ' ' + str(i))
        
        elif (aux == '('):
            print (aux)
            #print ("Token:" + token + " Tipo: AB_P")
            return (token + ' ' + str(i))
        
        elif (aux == ')'):
            print (aux)
            #print ("Token:" + token + " Tipo: FC_P")
            return (token + ' ' + str(i))
        
        elif (aux == ';'):
            print (aux)
            #print ("Token:" + token + " Tipo: PT_V")
            return (token + ' ' + str(i))
        
        else:
            i+= 1 

        if aux == '$':
            break
        i += 1

def spliter(token):
    token,stop = token.split()
    return int(stop)

#inicio
f = open("Compiler\entry.txt", "r")

token = lexical(f,0)
stop = spliter(token)
print (stop)
token = lexical(f,stop)