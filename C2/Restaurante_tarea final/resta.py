from threading import Thread 
import queue, time
import threading 
import random

#Clientes = []
#Cocineros = []
#clientes llegando 
bufferRest = queue.Queue(maxsize=20)
#print(cantrecep.maxsize)

#cantidad de meseros

#print(pormeseros)
#caoacidad del rest
rest = queue.Queue(maxsize=20)

mutex = threading.Lock()
#ordenes
bufferOrdenes = queue.Queue()
#cocinar
bufferCook = queue.Queue()

def reserva (id):
#cantidad de recepciones validas
    por = float(20)
    reception = int(por * bufferRest.maxsize/100)
    ciclo = True
    while ciclo == True:
        if not bufferRest.full():
            for x in range(reception):
                bufferRest.put(id)
                print("Hay una reservacion del cliente"+ str(id+1))
                

        ciclo = False

def cocinar (id):
    ciclo = True
    while ciclo == True:
        if not bufferOrdenes.empty():
            if not bufferCook.full():
                bufferOrdenes.get(id)
                print("Cocinero prepara la comida del cliente: "+str(id+1))
                bufferCook.put(id)
            else:
                ordenar(id)   
        else:
            atendiendo(id)


def ordenar(id):
    cant = float(10)
    mesero = int(cant * rest.maxsize/100)
    meseros = queue.Queue(maxsize=mesero)
    ciclo = True
    while ciclo == True:
        if not rest.empty():
            if not bufferOrdenes.full():
                    rest.get(id)
                    print("Mesero Tomando Orden del Cliente: "+str(id+1))
                    bufferOrdenes.put(id)
                    #cocinar(id)
            else:
               cocinar(id) 
        else:
            atendiendo(id)
            
            
def atendiendo(id):
    ciclo = True
    while ciclo == True:
        if not bufferRest.empty():
            if not rest.full():     
                bufferRest.get(id)
                print("Atendiendo Cliente:" + str(id+1))
                time.sleep(5)
                rest.put(id)
                print("Cliente: " +str(id+1)+ " ingreso al restaurante")
                ordenar(id)

                ciclo = False 
            else:
                ordenar(id)    
        else:
            ingresar(id)
            

class Persona(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        ingresar(self.id)
        mutex.release()

        

def ingresar(id):
    ciclo = True
    while ciclo == True:
        if not bufferRest.full():
            bufferRest.put(id)
            print("Hay un nuevo Cliente: " + str(id+1))
            atendiendo(id)
            ciclo = False
        else:
            atendiendo(id)


        
person = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 0
recepcionista = [1]     
if __name__=="__main__": 
    for i in person:
        p = Persona(i-1) 
        p.start()

    #reserva()q