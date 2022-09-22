import requests
from pprint import pprint
import json
import psycopg2
import time
import threading
import concurrent.futures

#Karla Maricruz Ruiz Diaz, 203440
#Actividad 03, 7B

threading_local = threading.local()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
        
def BD():
    conn = psycopg2.connect(host='localhost', user='postgres', password='203440',  dbname='Pokeapi')
    return conn

def guardar(data):
    conn = BD()
    cursor = conn.cursor()
    cursor.execute('insert into pokemon(pokemons) values(%s)', (data,))
    conn.commit()
    conn.close()

def get_service(url):
	resp = requests.get(url)
	if resp.status_code==200:
		resp_json =json.loads(resp.text)
		for i in resp_json["results"]:
			nombre= i["name"]
			write_db(nombre)

def write_db(nombre):
	json_a_guardar = json.dumps(nombre)
	guardar(json_a_guardar)

if __name__ == "__main__":
    url_site = ["https://pokeapi.co/api/v2/pokemon?limit=5000"]
    init_time = time.time()
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)


# 	App para desargar videos de 5 url diferentes 