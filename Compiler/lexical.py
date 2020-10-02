import sys

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
    if act == '$':
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

    tam = len(line)
    while itr < tam - 1:
        actual = line[itr]
        
        if (line[itr+1] != '\n'):
            nex = line[itr+1]
        itr += 1

        if (actual == ' '):
            actual = line[itr+1]
            nex = line[itr+2]

        elif (num_token(actual)): #incomplete
            token =  ''
            token = token + actual
            aux = ind
            while(num_token(nex)):
                token = token + nex
                if (aux == tam):
                    sys.exit(error("Missing ; at the end of the line: " + str(line_num)))
                else:
                    break
            print(token + ",NUM")
            dictionary[token] = "NUM"

        elif (lit_token(actual)): #should be tested
            token = ''
            token = token + actual
            if (not lit_token(nex)):
                aux = itr
                while aux < tam - 1:
                    token = token + nex
                    if (lit_token(nex)):
                        break
                    aux += 1
                    nex = line[aux+1]
                if (aux == tam - 1):
                    sys.exit(error("Literal constant is not closed, in line: " + str(line_num)))
            print (token + ',LITERAL')
            dictionary[token] = "LITERAL,string"

        elif (id_token(actual)): #should be tested
            alpha = 'abcdefghijklmnopqrstuvwyxz'
            token = ''
            if actual in alpha:
                token = token + actual
                if (id_token(nex)):
                    aux = itr
                    while aux < tam - 1:
                        token = token + nex
                        if (id_token(nex)):
                            break
                        aux += 1
                        nex = line[aux+1]
                    if (aux == tam - 1):
                        sys.exit(error("Invalid character in line: " + str(line_num)))
                print(token + ',ID')
                dictionary[token] = "ID,string"
            
        elif (comment_token(actual)):#should be tested
            #recognize but do nothing
            token =  ''
            token = token + actual
            aux = ind
            while(not comment_token(nex)):
                token = token + nex
                if (aux == tam-1):
                    sys.exit(error("Comment hasn't been closed, at line: " + str(line_num)))
                    break
                aux += 1
                nex = line[aux+1]
            return
                
        elif (eof_token(actual)):#should be tested
            print(actual + ',EOF')
            
        elif (opr_token(actual)):#not tested
            if (actual == '<' and nex == '-'):
                token = actual + nex
                print(token + ',RCB')
                dictionary[token] = "RCB"
                itr += 1
            elif actual == '<' and ((nex == '>') or  (nex == '=')):
                token = actual + nex
                print(token + ',OPR')
                dictionary[token] = "OPR"
            elif (actual == '<' and not opr_token(nex)):
                print(actual + ',OPR')
                dictionary[token] = "OPR"
            elif (actual == '>' and nex == '='):
                token = actual + nex
                print(token + ',OPR')
                dictionary[token] = "OPR"
            elif (actual == '>' and not opr_token(nex)):
                print(actual + ',OPR')
                dictionary[token] = "OPR"
            elif (actual == '='):
                print(actual + ',OPR')
                dictionary[token] = "OPR"
                        
        elif (opm_token(actual)):#not tested
            if not opm_token(nex):
                print(actual + ',OPM')
                dictionary[token] = "OPM"
            else:
                sys.exit(error("Mathematical operand not recognized at line: " + str(line_num)))
                        
        elif (ab_p_token(actual)):#not tested
            print(actual + ',AB_P')
            dictionary[token] = "AB_P"
                        
        elif (fc_p_token(actual)):#not tested
            print(actual + ',FC_P')
            dictionary[token] = "FC_P"
                        
        elif (pt_v_token(actual)):#not tested
            nex = line[itr]
            if nex == '\n':
                print(actual + ',PT_V')
                dictionary[token] = "PT_V"
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