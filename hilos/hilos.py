from xml.dom.expatbuilder import theDOMImplementation
import pytube
import requests
import threading
import time
import psycopg2
import json
#Karla Maricruz Ruiz Diaz
#203440, 7B

#Descargar videos
def get_service1():
    path = "/Users/karla/Documentos/programas/video"
    
    print('Descargando Video 1')
    v1 = pytube.YouTube("https://www.youtube.com/watch?v=fk4BbF7B29w")
    v1.streams.first().download(path)
    print('Descargando Video 2')
    v2 = pytube.YouTube("https://www.youtube.com/watch?v=niG3YMU6jFk")
    v2.streams.first().download(path)
    print('Descargando Video 3')
    v3 = pytube.YouTube("https://www.youtube.com/watch?v=cii6ruuycQA")
    v3.streams.first().download(path)
    print('Descargando Video 4')
    v4 = pytube.YouTube( "https://www.youtube.com/watch?v=gBRi6aZJGj4")
    v4.streams.first().download(path)
    print('Descargando Video 5')
    v5 = pytube.YouTube("https://www.youtube.com/watch?v=ffcitRgiNDs")
    v5.streams.first().download(path)


#Base de datos 2000 registros
def BD():
    conn = psycopg2.connect(host='localhost', user='postgres', password='203440',  dbname='Pokeapi')
    return conn

def guardar(data):
    conn = BD()
    cursor = conn.cursor()
    cursor.execute('insert into pokemon(pokemons) values(%s)', (data,))
    conn.commit()
    conn.close()

def get_service():
	resp = requests.get('https://pokeapi.co/api/v2/pokemon?limit=2000')
	if resp.status_code==200:
		resp_json =json.loads(resp.text)
		for i in resp_json["results"]:
			nombre= i["name"]
			write_db(nombre)


def write_db(nombre):
    print('Guardando Datos')
    json_a_guardar = json.dumps(nombre)
    guardar(json_a_guardar)
   
    

#Solicitudes random
def get_services(x=0):
    print(f'Data input ={x}')
    time.sleep(100)
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)

if __name__ == '__main__':
    print('Listando Datos')
    x=0
    for _ in range(0,50):
        print(x)
        th1 = threading.Thread(target = get_services, args=[x])
        th1.start()
    
    th2 = threading.Thread(target = get_service1)
    th2.start()
    th3 = threading.Thread(target= get_service)
    th3.start()