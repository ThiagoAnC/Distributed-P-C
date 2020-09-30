import time
import zmq

ok = "Done!"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()

    #Functions

    #The message format is 
    # (code,name,job_role,salary) separated with commas,w/o white spaces
    #code here is the function you do want to use, in this case, is "income"
    if "income" in str(message):
        aux = str(message)
        code,name,role,sal = aux.split(",")
        sal,escape = sal.split("'")

        if "operador" in role:
            socket.send_string("New income: " + str(float(int(sal)) *1.2))

        elif "programmer" in role:
            socket.send_string("New income: " + str(float(int(sal)) *1.18))

        else:
            socket.send_string("Invalid job role!")
            
        print ("ok")
        print("-------------")

    
    #The message format is
    # (code,name,gender,age) separated with commas,w/o white spaces
    # code here is "adult"  
    if "adult" in str(message):
        aux = str(message)
        code,name,gender,age = aux.split(",")
        age,escape = age.split("'")

        if "male" in gender:
            if int(age) < 18:
                socket.send_string(name + " has not yet come of age!")
            else:
                socket.send_string(name + " came of age!")

        elif "female" in gender:
            if int(age) < 21:
                socket.send_string(name + " has not yet come of age!")
            else:
                socket.send_string(name + " came of age!")

        else:
            socket.send_string("Invalid format!")
        print ("ok")
        print("-------------")


    #The message format is
    # (code,score1,score2.score3) separated with commas,w/o white spaces
    # code here is "score"
    if "score" in str(message):
        aux = str(message)
        code,n1,n2,n3 = aux.split(",")
        n3,escape = n3.split("'")

        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        if ((n1+n2)/2) >= 7:
            socket.send_string("You passed the course!")

        elif ((n1+n2)/2) >= 3:
            socket.send_string("You have not passed the course yet, you must do the third test!")

            if (((n1+n2)/2) + n3)/3 > 5:
                #print("Aprovado!")
                socket.send_string("You passed the course!")

            else:
                #print("Reprovado!")
                socket.send_string("You not passed the course!")
        else:
            #print("Reprovado!")
            socket.send_string("You not passed the course!")

        print ("ok")
        print("-------------")
    
    
    #The message format is
    # (code,height,gender) separated with commas,w/o white spaces
    # code here is "weight"
    if "weight" in str(message):
        aux = str(message)
        code,height,gender = aux.split(",")
        height,escape = height.split("'")

        height = float(height)

        if "female" in gender:
            socket.send_string("Recommended weight: " + str(round(height*62.1-44.7,2)))
        elif "male" in gender:
            socket.send_string("Recommended weight: " + str(round(height*72.7-58,2)))
        else:
            socket.send_string("Invalid format!")
        print ("ok")
        print("-------------")


    #The message format is
    # (code,age) separated with commas,w/o white spaces
    # code here is "categ"
    if "categ" in str(message):
        aux = str(message)
        code,age = aux.split(",")
        age,escape = age.split("'")

        age = int(age)

        if age < 5:
            socket.send_string("Idade insuficiente") # Not enough age to swim
        elif age <= 7:
            socket.send_string("Infantil A") #Child 1
        elif age <= 10:
            socket.send_string("Infantil B") #Child 2
        elif age <= 13:
            socket.send_string("Juvenil A") #Teen 1
        elif age <= 17:
            socket.send_string("Juvenil B") #Teen 2
        elif age >= 18:
            socket.send_string("Adulto")    #Adulto
        else:
            socket.send_string("Invalid age!")
        print ("ok")
        print("-------------")

    #The message format is
    # (code,name,level,gross,depend) separated with commas,w/o white spaces
    #code here is "net"
    if "net" in str(message):
        aux = str(message)
        code,name,level,gross,depend = aux.split(",")
        depend,escape = depend.split("'")

        gross = float(gross)

        if "a" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.92)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.97))
        
        elif "b" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.9)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.95))
        
        elif "c" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.85)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.92))

        elif "d" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.83)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Net wage: " + str(gross*0.9))

        else:
            socket.send_string("Invalid data!")
        print("ok")
        print("-------------")

    #The message format is
    # (code,age,work time) where code is "retire"
    if "retire" in str(message):
        aux = str(message)
        code,age,work = aux.split(",")
        work,escape = work.split("'")

        if int(age) >=65 and int(work) >=30:
            socket.send_string("You can retire, rest a little!")
        else:
            socket.send_string("Ah...you are not able to retire yet, go to job!")
        print("ok")
        print("-------------")
   
    
    #The message format is
    # (code,bank balance) where code is "bank"
    if "bank" in str(message):
        aux = str(message)
        code,balance = aux.split(",")
        balance,escape = balance.split("'")

        if int(balance) <= 200:
            socket.send_string("There is no bank loan to this balance:" + balance)
        elif int(balance) <= 400:
            socket.send_string("There is 20%. of loan to this balance: " + balance)
        elif int(balance) <= 600:
            socket.send_string("There is 30%. of loan to this balance: " + balance)
        elif int(balance) > 600:
            socket.send_string("There is 40%. of loan to this balance: " + balance)
        elif int(balance) < 0:
            socket.send_string("Invalid data!")
        print("ok")
        print("-------------")

    if "stop" in str(message):
        break
