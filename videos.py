import pytube 
import requests
from pprint import pprint
import json
import psycopg2
import time
import threading
import concurrent.futures

threading_local = threading.local()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)

def get_service(url):
    v1 = pytube.YouTube(url)
    v1.streams.first().download("/Users/karla/Documentos/programas/video")

if __name__ == "__main__":
    url_site = [
    "https://www.youtube.com/watch?v=fk4BbF7B29w",
    "https://www.youtube.com/watch?v=niG3YMU6jFk",
    "https://www.youtube.com/watch?v=cii6ruuycQA",
    "https://www.youtube.com/watch?v=gBRi6aZJGj4",
    "https://www.youtube.com/watch?v=ffcitRgiNDs"]
    init_time = time.time()
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)
