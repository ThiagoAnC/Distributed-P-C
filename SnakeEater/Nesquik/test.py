from time import time
global aux
aux = []

def get_data(a,tam):
  with open(a) as f:
    line  = f.readline()
    while line:
      line1 = line.split(',')
      for i in range(tam):
        aux.append(float(line1[i]))
      line = f.readline()
  return aux

def partition(a,start,final): 
    i = (start - 1)
    pivot = a[final]

    for n in range(start, final): 
        if a[n] < pivot: 
		
            i = i+1
            a[i],a[n] = a[n],a[i] 

    a[i+1],a[final] = a[final],a[i+1]
    return (i+1) 

def nesquik(a,start,final): 
    if start >= final:
        return 

    pivot = partition(a,start,final) 

    nesquik(a, start, pivot - 1) 
    nesquik(a, pivot + 1, final) 

def ordenate(a,tam):
    nesquik(a, 0, tam - 1)
    return a

def put_data(a, tam,elapsed):
  with open('SnakeEater\\Nesquik\\temp.txt','w') as f:
    f.write("Thiago de Andrade Correa\n")
    f.write('Time to sort: '"{:.0f}".format(elapsed%1000) + ' seconds and ' + "{:.0f}".format((elapsed*1000)%100) + ' miliseconds and ' + "{:.0f}".format((elapsed*1000000)%1000) + ' microseconds and ' + "{:.2f}".format((elapsed*1000000000)%1000) + ' nanoseconds!' + '\n')
    for i in range(tam):
      if i < tam - 1:
        f.write(str(aux[i]) + ';')
      else: 
        f.write(str(aux[i]))

def set_time(start):
  return time() - start

tam = 100000
aux = get_data('SnakeEater\\Nesquik\\dez_mil.txt',tam)
start = time()
aux = ordenate(aux, tam)
elapsed = set_time(start)
put_data(aux,tam,elapsed)