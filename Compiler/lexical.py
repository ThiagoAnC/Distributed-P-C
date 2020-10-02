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

def rcb_token(act):
    symbols = '<-'
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

        if (num_token(actual)): #incomplete
            token =  ''
            token = token + actual
            aux = ind
            while(num_token(nex)):
                token = token + nex
                if (aux == tam-1):
                    error("Missing ; at the end of the line: " + line_num)
                    break
                aux += 1
            return token

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
                    error("Literal constant is not closed, in line: " + str(line_num))
                    return
            return token

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
                        error("Invalid character in line: " + str(line_num))
                        return
                return token
            
        elif (comment_token(actual)):#should be tested
            #recognize but do nothing
            token =  ''
            token = token + actual
            aux = ind
            while(not comment_token(nex)):
                token = token + nex
                if (aux == tam-1):
                    error("Comment hasn't been closed, at line: " + line_num)
                    break
                aux += 1
                nex = line[aux+1]
            return
                
        elif (eof_token(actual)):#should be tested
            return actual
            
        elif (opr_token(actual)):
            pass
            
        elif (rcb_token(actual)):
            pass
                        
        elif (opm_token(actual)):
            pass
                        
        elif (ab_p_token(actual)):
            pass
                        
        elif (fc_p_token(actual)):
            pass
                        
        elif (pt_v_token(actual)):
            pass
                        
        else:
            error("In")
            
#inicio
with open('Compiler\entry.txt') as f:
    global dictionary
    try:
        line_num = 1
        line = f.readline()
        while line:
            lexical(line_num,line)
            line  = f.readline()
            line_num += 1
    finally:
        f.close()