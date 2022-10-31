import random
import queue
import threading
import time
#Karla Ruiz Diaz, 203440
bodega = queue.Queue(10)

def product():
    while True:
        valor = random.randint(1, 10)
        for x in range(valor):
            if bodega.qsize() < valor:
            #valor = random.randint(1, 10)
                bodega.put(x+1)
                print(f'Produciendo: {valor}')
                print(f'Buffer Actual: {list(bodega.queue)}')
                time.sleep(2)
            else:
                time.sleep(2)


def consu():
    while True:
        valor = random.randint(1, 10)
        for y in range(valor):
            if bodega.qsize() > valor:
                #valor = random.randint(1, 10)
                #valor = bodega.get()
                bodega.get(y+1)
                print(f'Consumiendo: {valor}')
                print(f'Buffer Actual: {list(bodega.queue)}')
                time.sleep(2)
            else:
                time.sleep(2)

def main():

    productor = threading.Thread(target=product)
    consumidor = threading.Thread(target=consu)

    productor.start()
    consumidor.start()

if __name__ == '__main__':
    main()
