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

PERSONAS = 20

cant = float(10)
mesero = int(cant * rest.maxsize/100)
meseros = queue.Queue(maxsize=mesero)

class Persona(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def reserva(self):
        #cantidad de recepciones validas
        por = float(20)
        reception = int(por * bufferRest.maxsize/100)
        ciclo = True
        while ciclo == True:
            if not bufferRest.full():
                for x in range(reception):
                    bufferRest.put(self.id)
                    print("Hay una reservacion del cliente"+ str(self.id+1))
            ciclo = False

    def cocinar (self):
        ciclo = True
        while ciclo == True:
            if not bufferOrdenes.empty():
                if not bufferCook.full():
                    bufferOrdenes.get(self.id)
                    print("Cocinero prepara la comida del cliente: "+str(self.id+1))
                    bufferCook.put(self.id)
                #else:
                    #ordenar(self.id)   
            #else:
                #atendiendo(self.id)


    def ordenar(self):
        cant = float(10)
        mesero = int(cant * rest.maxsize/100)
        meseros = queue.Queue(maxsize=mesero)
        ciclo = True
        while ciclo == True:
            if not rest.empty():
                if not bufferOrdenes.full():
                    rest.get(self.id)
                    print("Mesero Tomando Orden del Cliente: "+str(self.id+1))
                    bufferOrdenes.put(self.id)
                    #cocinar(self.id)
                #else:
                    #cocinar(self.id) 
            #else:
                #atendiendo(self.id)
                    
    def atendiendo(self):
        ciclo = True
        while ciclo == True:
            if not bufferRest.empty():
                if not rest.full():     
                    bufferRest.get(self.id)
                    print("Atendiendo Cliente:" + str(self.id+1))
                    time.sleep(5)
                    rest.put(self.id)
                    print("Cliente: " +str(self.id+1)+ " ingreso al restaurante")
                    ord
                    #ordenar(self.id)
                    ciclo = False
                #else:
                    #ordenar(self.id)    
           # else:
                #ingresar(self.id)
            
    
    def ingresar(self):
        ciclo = True
        while ciclo == True:
            if not bufferRest.full():
                bufferRest.put(self.id)
                print("Hay un nuevo Cliente: " + str(self.id+1))
                #atendiendo(self.id)
                ciclo = False   
            #else:
                #atendiendo(self.id)


    def run(self):
        self.ingresar()
        self.atendiendo()
        self.ordenar()
        self.cocinar()

           
#person = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
recepcionista = [1]   
def main():
    personas = []

    for i in range(PERSONAS):
        personas.append(Persona(i))

    for p in personas:
        p.start()
    
    for p in personas:
        p.join()



if __name__ == "__main__":
    main()
