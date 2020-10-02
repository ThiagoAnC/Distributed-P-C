def num_token(act,nex):
    pass

def lit_token(act,nex):
    if (act == '\"'):
        return True
    else:
        return False        
    
def id_token(act,nex):
    pass

def comment_token(act,nex):
    pass

def eof_token(act,nex):
    pass

def opr_token(act,nex):
    pass

def rcb_token(act,nex):
    pass

def opm_token(act,nex):
    pass

def ab_p_token(act,nex):
    pass

def fc_p_token(act,nex):
    pass

def pt_v_token(act,nex):
    pass

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

        if (num_token(actual,nex)):
            dictionary['num'] = num_token(actual,nex)

        elif (lit_token(actual,nex)):
            if (actual == '\"' and nex != '\"'):
                aux = itr
                while aux < tam - 1:
                    if (nex == '\"'):
                        break
                    nex = line[aux+1]
                if (aux == tam - 1):
                    error("Literal constant is not closed, in line: " + str(line_num))
                    return
            dictionary['lit'] = lit_token(actual,nex)

        elif (id_token(actual,nex)):
            dictionary['id'] = id_token(actual,nex)
        
        elif (comment_token(actual,nex)):
            #recognize but do nothing
            pass
            
        elif (eof_token(actual,nex)):
            dictionary['eof'] = eof_token(actual,nex)
            
        elif (opr_token(actual,nex)):
            dictionary['opr'] = opr_token(actual,nex)
            
        elif (rcb_token(actual,nex)):
            dictionary['rcb'] = rcb_token(actual,nex)
                        
        elif (opm_token(actual,nex)):
            dictionary['opm'] = opm_token(actual,nex)
                        
        elif (ab_p_token(actual,nex)):
            dictionary['abp'] = ab_p_token(actual,nex)
                        
        elif (fc_p_token(actual,nex)):
            dictionary['fcp'] = fc_p_token(actual,nex)
                        
        elif (pt_v_token(actual,nex)):
            dictionary['ptv'] = pt_v_token(actual,nex)
                        
        else:
            error(actual)
            #implement it later
            pass
            
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