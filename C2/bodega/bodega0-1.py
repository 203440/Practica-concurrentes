from threading import Thread 
import time, random
import queue
from tkinter import NONE

bodega = queue.Queue(maxsize=20)

class Productor(Thread):
    def __init__(self, array1):
        self.array1 = array1

    def run(self):
        while True:
            if not bodega.full():
                array1 = random.randint(0, 20)
                bodega.put(array1)
                print("Se agrego un nuevo intem: " + str(array1))
                time.sleep(5)

class Consumidor(Thread):
    def __init__(self, array1):
        self.array1 = array1

    def run(self):
        while True:
            if bodega.full():
                array1 = random.randint(0, 20)
                #array1 = bodega.get()
                bodega.get(array1)
                print('Consumiendo:'+ str(array1))
                time.sleep(5)


def main():
    hilo_productor = Productor()
    hilo_consumidor = Consumidor()

    hilo_productor.start()
    hilo_consumidor.start()


main()
