import threading
import time

#Karla Maricruz Ruiz Diaz, 203440
#Examen, 7B
palillos = [threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock(),threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock()]
palillo = [threading.Lock()]

mutex = threading.Lock()


def pasar(id):
    if id == len(palillos)-1:
        if "locked" in str(palillo[0]):  
            palillo[0].release()                       
    else:
        if "locked" in str(palillos[id+1]):  
            palillos[id+1].release()

def tener(id):
    datito = 0
    if "unlocked" in str(palillos[id]):  
        palillos[id].acquire()
        if id == len(palillos)-1:
            palillos[0].release()
            if "unlocked" in str(palillo[0]): 
                palillo[0].acquire()                
                datito = 1
        else:
            if "unlocked" in str(palillos[id+1]):  
                palillos[id+1].acquire()
                datito = 1
    return datito

def comiendo(id):
    ciclo = True
    while ciclo == True:
        comer = tener(id)
        time.sleep(0.5)
        if comer == 1: 
            print("Persona "+str(id+1)+" esta comiendo")
            time.sleep(5)
            print("Pancita llena, corazon contento")
            pasar(id)
            ciclo = False
                     
class Persona(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        comiendo(self.id)
        mutex.release()
        
person = [1,2,3,4,5,6,7,8]         
if __name__=="__main__": 
    for i in person:
        p = Persona(i-1)
        p.start()
    