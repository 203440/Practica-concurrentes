import random
import queue
import threading
import time

bodega = queue.Queue(15)

def product():
    while True:
        valor = random.randint(1, 15)
        for x in range(valor):
            if bodega.qsize() < valor:
                bodega.put(x+1)
                print('Produciendo:'+str(valor))
                print(f'Bodega Actual: {list(bodega.queue)}')
                time.sleep(2)
            else:
                time.sleep(2)


def consu():
    while True:
        valor = random.randint(1, 15)
        for y in range(valor):
            if bodega.qsize() > valor:
                bodega.get(y+1)
                print('Consumiendo: {valor}')
                print(f'Bodega Actual: {list(bodega.queue)}')
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
