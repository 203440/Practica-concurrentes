from threading import Thread 
import queue, time
import threading 
import random

#Clientes = []
#Cocineros = []



bufferRest = queue.Queue(maxsize=20)


#print(cantrecep.maxsize)

#cantidad de meseros
cant = float(10)
pormeseros = float(cant * bufferRest.maxsize/100)
meseros = queue.Queue(maxsize=pormeseros)
#print(pormeseros)

mutex = threading.Lock()

def reserva (id):
#cantidad de recepciones validas
    por = float(20)
    reception = int(por * bufferRest.maxsize/100)
    #cantrecep = queue.Queue(maxsize=reception)
    ciclo = True
    while ciclo == True:
        if not bufferRest.full():
            for x in range(reception):
                bufferRest.put(id)
                print("Hay una reservacion del cliente"+ str(id+1))

        ciclo = False

def atendiendo(id):
    ciclo = True
    while ciclo == True:
        if not bufferRest.empty():
            bufferRest.get(id)
            print("Atendiendo Cliente(s):" + str(id+1))
            #print("Recepcionista" + str(id2)+ "Atendiendo Cliente(s):" + str(id1+1))
            time.sleep(5)
            #atendiendo(id)

            ciclo = False
        else:
            ingresar(id)
            #reserva(id)

class Persona(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        atendiendo(self.id)
        mutex.release()

def ingresar(id):
    ciclo = True
    while ciclo == True:
        if not bufferRest.full():
            bufferRest.put(id)
            print("Hay un nuevo Cliente: " + str(id+1))
            time.sleep(5)
            #reserva(id)
            ciclo = False
        #else:
            #atendiendo(id)
                     
#class Persona(threading.Thread):
 #   def __init__(self, id):
  #      threading.Thread.__init__(self)
   #     self.id=id

    #def run(self):
     #   mutex.acquire()
      #  ingresar(self.id)
       # mutex.release()
        
person = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 0
recepcionista = [1]     
if __name__=="__main__": 
    for i in person:
        p = Persona(i-1) 
        p.start()

    #reserva()q