import threading
import time
from tkinter import N


KONSUM = 5
PRODU = 5


class  bodega():
    aproduc = []
    aconsum = []

    def __init__(self,size=5):
        self.q = [None] * size      
        self.capacity = size        
        self.front = 0              
        self.rear = -1              
        self.count = 0             
    
    # Función para quitar un elemento a la queue
    def dequeue (self):
        # ver si se tiene un desbordamiento de la queue
        if self.isEmpty==0:
            print('Terminando el proceso...')
            exit(-1)
        x = self.q[self.front]
        print('consumiendo...')
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x
    
    # Función para agregar un elemento a la queue
    def enqueue(self):
        
        if self.isFull():
            print('Terminando...')
            exit(-1)
        value = self.q[self.front]
        print('Produciendo...')
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def size(self):
        return self.count

    # Función # para comprobar si la queue está vacía o no
    def isEmpty(self):
        return self.size() == 0

     # Función # para comprobar si la queue está llena o no
    def isFull(self):
        return self.size() == self.capacity

    def espera(self):
        time.sleep(0.50)

    def run(self):
        self.espera()
        self.enqueue()
        self.dequeue()
        self.isEmpty()
        self.isFull()

def lleno():   
    produ = []
    for x in range(KONSUM):
        bodega.dequeue(bodega())
        #print('Retirando produto'+str(x+1))
        time.sleep(0.50)

def nolleno():
    konsum = []
    for i in range(PRODU):
        bodega.enqueue(bodega())
        #print('agregando produto'+ str(i+1))
        time.sleep(0.50)


def main():
    q = bodega(10)
    lleno()
    if q.isEmpty():
        print('No Lleno')
        nolleno()
        main()
    else:
        print('Lleno')
        lleno()
        main()

if __name__ == '__main__':
    main()
 
    # crea una queue de capacidad 5

