import requests
import sched
import time
#203440, Karla Ruiz

def ver(x):
        print ("url"+ str(x))
        page = requests.get(x)
        if page.status_code == 200 :
            print(200)
        else:
            print(400)


class main ():
    while True:
        cada_cuanto =  sched.scheduler(time.time,time.sleep)
        cada_cuanto.enterabs(time.time()+240,1,print,argument=("",))
        url=[
        "https://www.google.com",
        "https://drive.google.com/drive/u/0/my-drive",
        "https://mail.google.com/mail/u/0/?pli=1#inbox",
        "https://www.youtube.com/",
        "https://calendar.google.com/calendar/u/0/r",
        "https://classroom.google.com/u/0/","https://docs.google.com/document/u/0/?hl=es&tgif=d",
        "https://subes.becasbenitojuarez.gob.mx/","https://pokeapi.co/",
        "https://platinum.upchiapas.edu.mx/alumnos/login","https://app.netlify.com/teams/203440/overview",
        "https://es.wordpress.org/","https://www.tiendanube.com.mx/",
        "https://www.ionos.mx/digitalguide/servidores/know-how/maquina-virtual/", "https://www.tiendanube.com/blog/mx/ejemplos-de-paginas-web/",
        "https://www.figma.com/files/recent?fuid=1025121804957052974",
        "https://www.facebook.com/?_rdc=2&_rdr"
        ]
        init_time = time.time()
        for x in url :
            ver(x)
        cada_cuanto.run()
        end_time = time.time() - init_time
        print(end_time)
