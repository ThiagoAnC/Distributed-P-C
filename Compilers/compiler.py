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
                    if line[aux] != '\n':
                        aux += 1
                        nex = line[aux]
                        itr = itr +  (aux - itr)
                    else:
                        aux += 1
                        itr = itr +  (aux - itr)
                if notation == 1 or point == 1 or sign == 1:
                    save(token, 'NUM', 'real', (line_num))
                else:
                    save(token, 'NUM', 'inteiro', (line_num))

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
                save(token,'Literal', 'string',(line_num))

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
                        save(token,'','',(line_num))
                if not resv_words(token):
                    if not eof_token(token):
                        save(token,'ID','',(line_num))
                    else:
                        save(token, '','',(line_num))
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
                    save(token,'RCB','',(line_num))
                    itr += 1
                elif (actual == '<' and ((nex == '>') or  (nex == '='))) or (actual == '>' and nex == '='):
                    token = actual + nex
                    save(token, 'OPR','',(line_num))
                    itr += 1
                elif (actual == '<' and not opr_token(nex)):
                    save(token, 'OPR','',(line_num))
                elif (actual == '>' and not opr_token(nex)):
                    save(actual, 'OPR','',(line_num))
                elif (actual == '='):
                    save(actual, 'OPR','',(line_num))
                            
            elif (opm_token(actual)):#tested
                if not opm_token(nex):
                    save(actual, 'OPM','',(line_num))
                else:
                    error("Mathematical operand not recognized at line: " + str(line_num))
                            
            elif (ab_p_token(actual)):#tested
                save(actual, 'AB_P','',(line_num))
                            
            elif (fc_p_token(actual)):#tested
                save(actual, 'FC_P','',(line_num))
                            
            elif (pt_v_token(actual)):#tested
                nex = line[itr]
                if nex == '\n':
                    save(actual, 'PT_V','',(line_num))
                else:
                    error("Semicolon placed wrongly at line: " + str(line_num))
    
            else:
                error("Inrecognized token: " + actual + " at line:" + str(line_num))
                queue.append(actual + ',' + str(line_num))
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

    def save(lexem, token, typ,pos):
        if token or typ:
            entry = (lexem + ',' + token + ',' + typ)
        else:
            entry = lexem
        dictionary[lexem] = entry
        if (token == 'ID'):
            queue.append('id' + ',' + str(line_num))
            order.append(lexem)    
        elif token == 'PT_V':
            queue.append(';' + ',' + str(line_num))
        elif token == 'AB_P':
            queue.append('(' + ',' + str(line_num))
        elif token == 'FC_P':
            queue.append(')' + ',' + str(line_num))
        elif 'Literal' in token:
            queue.append('literal' + ',' + str(line_num))
        elif 'OPR' in token:
            queue.append('opr' + ',' + str(line_num))
            var.append(lexem)
        elif 'OPM' in token:
            queue.append('opm' + ',' + str(line_num))
            var.append(lexem)
        elif 'NUM' in token:
            queue.append('num' + ',' + str(line_num))
        elif 'RCB' in token:
            queue.append('rcb' + ',' + str(line_num))
        else:
            queue.append(entry.lower() + ',' + str(line_num))

    def resv_print(token,line_num):
        if token == 'real' or token == 'lit' or token == 'inteiro':
            if token == 'real':
                save(token, '','',(line_num))
            if token == 'lit':
                save(token, '','',(line_num))
            if token == 'inteiro':
                token = 'int'
                save(token, '','',(line_num))
        elif token == 'inicio':
            if line_num != 1:
                print("Reserved word to mark the beginning is not at the beginning, at line: " + str(line_num))
            save(token, '','',(line_num))
        elif token == 'fim':
            eof_token(token)
        else:
            save(token, '','',(line_num))

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

def initialize():
    f = open('Compilers\output.txt','w')
    f.write("#include <stdio.h>\n")
    f.write("typedef char literal[256]\n")
    f.write("void main() {\n")
    return f

def sintax():
    
    f = initialize()

    def semantic(id,token):
        if token == 'id':
            token = order.pop(0)
        elif token == 'opm' or token == 'opr':
            token = var.pop(0)
        if token != '$':
            print (dictionary[token])
        if id == 5:
            f.write("\n")
            f.write("\n")
            f.write("\n")
        elif id == 6:
            print (dictionary[token])

    def sintatic():
        queue.append('$' + ',' + str(0))
        stack = [0]
        begin = 0
        a,pos = queue[begin].split(',')
        while True:
            s = stack[0]
            if 'S' in data.retrieve(s,a):
                null = data.retrieve(s,a)
                t = int(null[1:]) - 1
                stack.insert(0,t)
                begin += 1
                a,pos = queue[begin].split(',')
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
                semantic(s,a)
            elif 'ACC' in data.retrieve(s,a):
                break
            elif 'E' in data.retrieve(s,a):
                null = data.retrieve(s,a)
                t = int(null[1:])
                data.handle_error(t,pos)
                begin += 1
                if t == 4:
                    begin -= 2
                    queue.insert(-1,'fim,' + pos)
                    a,pos = queue[begin].split(',')
                elif t == 6:
                    begin -= 1
                    queue.insert(0,'inicio,' + pos)
                    a,pos = queue[begin].split(',')
                elif t == 7:
                    begin -= 1
                    queue.insert(1,'varinicio,'+ pos)
                    a,pos = queue[begin].split(',')
                elif t == 8:
                    stack.insert(0,56)
                elif t == 9:
                    begin -= 3
                    a,pos = queue[begin].split(',')
                elif t == 10:
                    stack.insert(0,1)
                    a,pos = queue[begin].split(',')
                elif t == 11:
                    begin += 1
                    a,pos = queue[begin].split(',')
                else:    
                    a,pos = queue[begin].split(',')
            else:
                code = data.show_error(a)
                if code == 1:
                    begin += 1
                    a,pos = queue[begin].split(',')
                elif code == 0:
                    #just to test
                    pass
    
    sintatic()
    print ("Errors found: ")
    data.show_all()

#inicio    
global dictionary,queue,order,var
dictionary = {}
order = []
var = []
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