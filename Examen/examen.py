import threading
import time

#Karla Maricruz Ruiz Diaz, 203440
#Examen, 7B
palillo = [threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock(),threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock()]

mutex = threading.Lock()


def tener(id):
    res = 0
    #Palillo izq esta bloqueado o no
    if "unlocked" in str(palillo[id]):  
        palillo[id].acquire()
        if id == len(palillo)-1:
            palillo[0].release()
            #Palillo der esta bloqueado o no
            if "unlocked" in str(palillo[0]): 
                palillo[0].acquire()                
                res = 1
        else:
            #Palillo der bloqueado o no
            if "unlocked" in str(palillo[id+1]):  
                palillo[id+1].acquire()
                res = 1
    return res

def pasar(id):
    if id == len(palillo)-1:
        if "locked" in str(palillo[0]):  
            palillo[0].release()                       
    else:
        if "locked" in str(palillo[id+1]):  
            palillo[id+1].release()

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
    