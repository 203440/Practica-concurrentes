from threading import Thread
import threading
from time import sleep
import pytube

mutex = threading.Lock()

def crito(id):
    threads_semaphore = pytube.YouTube(threads_semaphore)
    threads_semaphore.streams.first().download("/Users/karla/Documentos/programas/video")
    x=0
    print("Hilo =" +str(threads_semaphore)+ " =>" + str(x+1))

class Hilo(threading.Thread):
    def __init__ (self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run (self):
        mutex.acquire()
        #sleep(3-self.id)
        crito(self.id)
        #print("varlor" +str(self.id))
        mutex.release

    

hilos = [
    Hilo("https://www.youtube.com/watch?v=fk4BbF7B29w"), 
    Hilo("https://www.youtube.com/watch?v=niG3YMU6jFk"), 
    Hilo("https://www.youtube.com/watch?v=cii6ruuycQA"), 
    Hilo("https://www.youtube.com/watch?v=gBRi6aZJGj4"), 
    Hilo("https://www.youtube.com/watch?v=ffcitRgiNDs")
    ]
x=1;
for h in hilos:
    h.start()