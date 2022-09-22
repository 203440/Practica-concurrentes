from threading import Thread, Semaphore
from turtle import st
import pytube
semaforo = Semaphore(1) # Crea la v

def crito(threads_semaphore):
    threads_semaphore = pytube.YouTube(threads_semaphore)
    threads_semaphore.streams.first().download("/Users/karla/Documentos/programas/video")
    x=0
    print("Hilo =" +str(threads_semaphore)+ " =>" + str(x+1))

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        semaforo.release() #Libera un semáforo e incrementa la varibale semáforo


threads_semaphore = [
    Hilo("https://www.youtube.com/watch?v=fk4BbF7B29w"), 
    Hilo("https://www.youtube.com/watch?v=niG3YMU6jFk"), 
    Hilo("https://www.youtube.com/watch?v=cii6ruuycQA"), 
    Hilo("https://www.youtube.com/watch?v=gBRi6aZJGj4"), 
    Hilo("https://www.youtube.com/watch?v=ffcitRgiNDs")]
x=1;
for t in threads_semaphore:
    t.start()


#App para en el cual descargaran 10 recursos diferentes integrando en concepto de semaforiacion 