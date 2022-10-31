from threading import Thread 
import queue, time
import threading 
import random

Recepcionista = 1


bufferRest = queue.Queue(maxsize=20)

#cantidad de recepciones validas
por = float(20)
reception = float(por * bufferRest.maxsize/100)
cantrecep = queue.Queue(maxsize=reception)
#print(cantrecep.maxsize)

#cantidad de meseros
cant = float(10)
pormeseros = float(cant * bufferRest.maxsize/100)
meseros = queue.Queue(maxsize=pormeseros)
#print(pormeseros)

mutex = threading.Lock()


def insertar(id):
    while True:
        if not bufferRest.full():
            #id = random.randint(0, 20)
            bufferRest.put(id)
            print("Hay un nuevo Cliente: " + str(id+1))
                        
                #num = random.randint(2, 5)
                #print(num)
            grupo = []
            for i in range(random.randint(2, 5)):
                    #id = random.randint(0, 20)
                grupo.append(id)
                bufferRest.put(id)
                
            print("Hay nuevos Clientes:")
                
            print(grupo)
            time.sleep(5)

class Persona(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        insertar(self.id)
        mutex.release()
        
person = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   
      
if __name__=="__main__": 
    for i in person:
        p = Persona(i-1)
        p.start()
    