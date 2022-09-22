from threading import Thread, Semaphore
from turtle import st
semaforo = Semaphore(1) # Crea la v

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        semaforo.release() #Libera un semáforo e incrementa la varibale semáforo

threads_semaphore = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5)]
x=1;
for t in threads_semaphore:
    t.start()


#App para en el cual descargaran 10 recursos diferentes integrando en concepto de semaforiacion 