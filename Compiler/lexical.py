import sys

def indict(token):
    if token in dictionary:
        return dictionary[token]
    else:
        return False

def hassignal(token):
    if token == '+' or token == '-':
        return True
    else:
        return False

def hasnotation(token):
    if token == 'e' or token == 'E':
        return True
    else:
        return False

def haspoint(token):
    if token == '.':
        return True
    else: 
        return False

def save(lexem, token, typ):
    dictionary[lexem] = token + ',' + typ

def resv_print(token,line_num,last):
    if token == 'real' or token == 'lit' or token == 'inteiro':
        if token == 'real':
            print (last + ' Tipo: real')
            dictionary[last] = last + ",ID" + ",real"
        if token == 'lit':
            print (last + ' Tipo: lit')
            dictionary[last] = last + ",ID" + ",lit"
        if token == 'inteiro':
            print (last + ' Tipo: inteiro')
            dictionary[last] = last + ",ID" + ",inteiro"
    elif token == 'inicio':
        if line_num != 1:
            sys.exit("Reserved word to mark the beginning is not at the beginning, at line: " + str(line_num))
        else:
            print ("Reserved: " + token)
    elif token == 'fim':
        eof_token(token)
    else:
        print ("Reserved: " + token)

def resv_words(token):
    dictionary['resv'] = {('inteiro'), ('lit'), ('real'), ('inicio'), ('varinicio'), ('varfim'), ('escreva'), ('leia'), ('se'), ('entao'), ('fimse')}
    if token in dictionary['resv']:
        return True
    else:
        return False

def isalpha(act):
    alpha = 'abcdefghijklmnopqrstuvwyxz'
    if act.lower() in alpha:
        return True
    else:
        return False 

def num_token(act):
    digits = '1234567890'
    if act in digits:
        return True
    else:
        return False

def lit_token(act):
    if (act == '\"'):
        return True
    else:
        return False        
    
def id_token(act):
    alpha = 'abcdefghijklmnopqrstuvwyxz'
    adds = alpha + '1234567890_'
    if act.lower() in adds:
        return True
    else:
        return False  

def comment_token(act):
    comment = '}{'
    if act in comment:
        return True
    else:
        return False

def eof_token(act):
    if act == 'fim':
        return True
    else:
        return False

def opr_token(act):
    symbols = '<>='
    if act in symbols:
        return True
    else:
        return False

def opm_token(act):
    symbols = '+-*/'
    if act in symbols:
        return True
    else:
        return False

def ab_p_token(act):
    if act == '(':
        return True
    else:
        return False

def fc_p_token(act):
    if act == ')':
        return True
    else:
        return False

def pt_v_token(act):
    if act == ';':
        return True
    else:
        return False

def error(err):
    print (err)

def lexical(line_num,line):
    ind = 0
    itr = 0
    aux = 0
    last = ''

    tam = len(line)
    while itr < tam - 1:
        actual = line[itr]
        
        if (line[itr+1] != '\n'):
            nex = line[itr+1]
        itr += 1

        if (actual == ' '):
            actual = line[itr+1]
            nex = line[itr+2]

        elif (num_token(actual)): #complete
            token =  ''
            aux = 0
            notation = 0
            sign = 0
            point = 0 
            token = token + actual
            aux = itr 
            while((num_token(nex) or hasnotation(nex) or haspoint(nex) or hassignal(nex)) and aux < tam):
                token = token + nex
                if (hasnotation(nex)):
                    if notation == 1:
                        sys.exit(error("Invalid notation caracter in given number, just one allowed, at line: " + line_num))
                    else:
                        notation = 1
                elif (haspoint(nex)):
                    if point == 1:
                        sys.exit(error("Invalid point caracter in given number, just one allowed, at line: " + line_num))
                    else:
                        point = 1
                elif (hassignal(nex)):
                    if sign == 1:
                        sys.exit(error("Invalid notation caracter in given number, just one allowed, at line: " + line_num))
                    else:
                        sign = 1
                if (aux == tam):
                    sys.exit(error("Missing ; at the end of the line: " + str(line_num)))
                aux += 1
                nex = line[aux]
            itr = itr +  (aux - itr)
            if notation == 1 or point == 1 or sign == 1:
                print(token + ",NUM", ',real')
                save(token, 'NUM', ',real')
            else:
                print(token + ",NUM", ',inteiro')
                save(token, 'NUM', ',inteiro')

        elif (lit_token(actual)): #tested
            token = ''
            token = token + actual
            if (not lit_token(nex)):
                aux = itr
                while aux < tam - 1:
                    token = token + nex
                    if (lit_token(nex)):
                        break
                    if (line[-3] != '\"' and line[-2] != ';'):
                        sys.exit(error("Literal constant is not closed, in line: " + str(line_num)))
                    elif (line[-1] == '\"'):
                        sys.exit(error("Semicolon is not at the end of line, in line: " + str(line_num)))
                    aux += 1
                    nex = line[aux]
                itr = itr + (aux - itr + 1)
            print (token + ',LITERAL',',string')
            save(token,',Literal', ',string')

        elif (isalpha(actual)): #tested
            token = ''
            token = token + actual
            if (id_token(nex)):
                aux = itr
                while aux < tam - 1:
                    token = token + nex
                    aux += 1
                    nex = line[aux]
                    if (not id_token(nex)):
                        break
                if (aux == tam):
                    sys.exit(error("Invalid character in line: " + str(line_num)))
                itr = itr + (aux - itr)
                if line[-1] == 'm' and token + nex == 'fim':
                    token = token + nex
                    nex = '\n'
            if eof_token(token):
                    if line[-1] == '\n' or nex == None:
                        sys.exit(error("EOF not at the end of the file, at line: " + str(line_num)))
                    print(token + ',EOF')
                    save(token, '','')
                    continue         
            if not resv_words(token):
                if indict(token):
                    print(indict(token))
                else:
                    print(token + ',ID')
                    save(token,',ID','')
                    last = token
            else:
                resv_print(token,line_num,last)
            
        elif (comment_token(actual)):#tested
            #recognize but do nothing
            token =  ''
            token = token + actual
            aux = ind
            while(not comment_token(nex)):
                token = token + nex
                if (aux == tam):
                    sys.exit(error("Comment hasn't been closed, at line: " + str(line_num)))
                    break
                aux += 1
                nex = line[aux]
            itr = itr + (aux - itr + 1)
            print ("comment here")
                           
        elif (opr_token(actual)):#tested
            if (actual == '<' and nex == '-'):
                token = actual + nex
                print(token + ',RCB')
                save(token,'RCB','')
                itr += 1
            elif actual == '<' and ((nex == '>') or  (nex == '=')):
                token = actual + nex
                print(token + ',OPR')
                save(token, 'OPR','')
                itr += 1
            elif (actual == '<' and not opr_token(nex)):
                print(actual + ',OPR')
                save(token, 'OPR','')
            elif (actual == '>' and nex == '='):
                token = actual + nex
                print(token + ',OPR')
                save(token, 'OPR','')
                itr += 1
            elif (actual == '>' and not opr_token(nex)):
                print(actual + ',OPR')
                save(actual, 'OPR','')
            elif (actual == '='):
                print(actual + ',OPR')
                save(actual, 'OPR','')
                        
        elif (opm_token(actual)):#tested
            if not opm_token(nex):
                print(actual + ',OPM')
                save(actual, 'OPM','')
            else:
                sys.exit(error("Mathematical operand not recognized at line: " + str(line_num)))
                        
        elif (ab_p_token(actual)):#tested
            print(actual + ',AB_P')
            save(actual, 'AB_P','')
                        
        elif (fc_p_token(actual)):#tested
            print(actual + ',FC_P')
            save(actual, 'FC_P','')
                        
        elif (pt_v_token(actual)):#tested
            nex = line[itr]
            if nex == '\n':
                print(actual + ',PT_V')
                save(actual, 'PT_V','')
            else:
                sys.exit(error("Semicolon placed wrongly at line: " + str(line_num)))
                return
 
        else:
            sys.exit(error("Inrecognized token: " + actual + " at line:" + str(line_num)))

            
#inicio
with open('Compiler\entry.txt') as f:
    global dictionary
    dictionary = {}
    try:
        line_num = 1
        line = f.readline()
        while line:
            lexical(line_num,line)
            line  = f.readline()
            line_num += 1
    finally:
        f.close()