import sys
import data

def lexical(line_num,line):

    def lex(line_num,line):
        ind = 0
        itr = 0
        aux = 0

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
                            error("Invalid notation caracter in given number, just one allowed, at line: " + str(line_num))
                        else:
                            notation = 1
                    elif (haspoint(nex)):
                        if point == 1:
                            error("Invalid point caracter in given number, just one allowed, at line: " + str(line_num))
                        else:
                            point = 1
                    elif (hassignal(nex)):
                        if sign == 1:
                            error("Invalid notation caracter in given number, just one allowed, at line: " + str(line_num))
                        else:
                            sign = 1
                    if (aux == tam):
                        error("Missing ; at the end of the line: " + str(line_num))
                    aux += 1
                    nex = line[aux]
                itr = itr +  (aux - itr)
                if notation == 1 or point == 1 or sign == 1:
                    save(token, 'NUM', 'real')
                else:
                    save(token, 'NUM', 'inteiro')

            elif (lit_token(actual)): #tested
                token = ''
                token = token + actual
                if (not lit_token(nex)):
                    aux = itr
                    while aux < tam - 1:
                        token = token + nex
                        if (lit_token(nex)):
                            break
                        #if (line[-3] != '\"' and line[-2] != ';'):
                            #error("Literal constant is not closed, in line: " + str(line_num))
                        elif (line[-1] == '\"'):
                            error("Semicolon is not at the end of line, in line: " + str(line_num))
                        aux += 1
                        nex = line[aux]
                    itr = itr + (aux - itr + 1)
                save(token,'Literal', 'string')

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
                        error("Invalid character in line: " + str(line_num))
                    itr = itr + (aux - itr)
                    if line[-1] == 'm' and token + nex == 'fim':
                        token = token + nex
                        nex = '\n'
                    if eof_token(token):
                        if line[-1] == '\n' or nex == None:
                            error("EOF not at the end of the file, at line: " + str(line_num))
                        save(token,'','')
                if not resv_words(token):
                    if not eof_token(token):
                        save(token,'ID','')
                    else:
                        save(token, '','')
                else:
                    resv_print(token,line_num)
            
            elif (comment_token(actual)):#tested
                #recognize but do nothing
                token =  ''
                token = token + actual
                aux = ind
                while(not comment_token(nex)):
                    token = token + nex
                    if (aux == tam):
                        error("Comment hasn't been closed, at line: " + str(line_num))
                        break
                    aux += 1
                    nex = line[aux]
                itr = itr + (aux - itr + 1)
                           
            elif (opr_token(actual)):#tested
                if (actual == '<' and nex == '-'):
                    token = actual + nex
                    save(token,'RCB','')
                    itr += 1
                elif (actual == '<' and ((nex == '>') or  (nex == '='))) or (actual == '>' and nex == '='):
                    token = actual + nex
                    save(token, 'OPR','')
                    itr += 1
                elif (actual == '<' and not opr_token(nex)):
                    save(token, 'OPR','')
                elif (actual == '>' and not opr_token(nex)):
                    save(actual, 'OPR','')
                elif (actual == '='):
                    save(actual, 'OPR','')
                            
            elif (opm_token(actual)):#tested
                if not opm_token(nex):
                    save(actual, 'OPM','')
                else:
                    error("Mathematical operand not recognized at line: " + str(line_num))
                            
            elif (ab_p_token(actual)):#tested
                save(actual, 'AB_P','')
                            
            elif (fc_p_token(actual)):#tested
                save(actual, 'FC_P','')
                            
            elif (pt_v_token(actual)):#tested
                nex = line[itr]
                if nex == '\n':
                    save(actual, 'PT_V','')
                else:
                    error("Semicolon placed wrongly at line: " + str(line_num))
    
            else:
                error("Inrecognized token: " + actual + " at line:" + str(line_num))
                queue.append(actual)
                data.get_error(actual, "Inrecognized token: " + actual + " at line:" + str(line_num))

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
        if token or typ:
            entry = (lexem + ',' + token + ',' + typ)
        else:
            entry = lexem
        if (token == 'ID'):
            dictionary[lexem] = token + typ
            queue.append('id')
        elif token == 'PT_V':
            queue.append(';')
        elif token == 'AB_P':
            queue.append('(')
        elif token == 'FC_P':
            queue.append(')')
        elif 'Literal' in token:
            queue.append('literal')
        elif 'OPR' in token:
            queue.append('opr')
        elif 'OPM' in token:
            queue.append('opm')
        elif 'NUM' in token:
            queue.append('num')
        elif 'RCB' in token:
            queue.append('rcb')
        else:
            queue.append(entry.lower())

    def resv_print(token,line_num):
        if token == 'real' or token == 'lit' or token == 'inteiro':
            if token == 'real':
                save(token, '','')
            if token == 'lit':
                save(token, '','')
            if token == 'inteiro':
                token = 'int'
                save(token, '','')
        elif token == 'inicio':
            if line_num != 1:
                print("Reserved word to mark the beginning is not at the beginning, at line: " + str(line_num))
            save(token, '','')
        elif token == 'fim':
            eof_token(token)
        else:
            save(token, '','')

    def resv_words(token):
        dictionary['resv'] = {('fim'),('inteiro'), ('lit'), ('real'), ('inicio'), ('varinicio'), ('varfim'), ('escreva'), ('leia'), ('se'), ('entao'), ('fimse')}
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

    lex (line_num,line)

def sintax():
        
    def sintatic():
        queue.append('$')
        stack = [0]
        begin = 0
        a = queue[begin]
        while True:
            s = stack[0]
            if 'S' in data.retrieve(s,a):
                null = data.retrieve(s,a)
                t = int(null[1:]) - 1
                stack.insert(0,t)
                print ("Add " + str(t) + " on stack")
                begin += 1
                a = queue[begin]
            elif 'R' in data.retrieve(s,a):
                null = data.retrieve(s,a)
                t = int(null[1:])
                A = data.goto(t)
                for i in range(data.rules(t,0) - 2):
                    stack.pop(0)
                s = stack[0]
                aux = data.retrieve(s,A)
                if type(aux) == float:
                    s = int(aux) - 1
                elif type(aux) == int:
                    s = aux - 1
                else:
                    s = int(aux[1:]) - 1
                stack.insert(0,s)
                print ("Reduced the rule: " + data.rules(t,1))
            elif 'ACC' in data.retrieve(s,a):
                print ("Reduced the rule: " + data.rules(s,1))
                break
            else:
                data.show_error(a)
                begin += 1
    sintatic()

#inicio    
global dictionary,queue
dictionary = {}
queue = []

#Lexical calling
with open('Compilers\entry.txt') as f:
    try:
        line_num = 1
        line = f.readline()
        while line:
            lexical(line_num,line)
            line  = f.readline()
            line_num += 1
    finally:
        f.close()
    
#Sintax calling
sintax()