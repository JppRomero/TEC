"""
Instrucciones de como correr el programa:

Para ejecutar este programa, 
asegúrate de tener Python instalado en tu computadora.
Guarda el código en un archivo con extensión .py, 
por ejemplo, proyefinalrev.py.
Luego, abre una terminal o línea de comandos, 
navega hasta el directorio donde guardaste el a
archivo y ejecuta el siguiente comando:
python proyefinalrev.py
o también puedes usar:
programas como PyCharm, Visual Studio Code 
o cualquier otro IDE de Python.

"""



"""
Este programa recomienda películas a 
universitarios según sus gustos por género.
el cual recibe las preferencias del usuario, 
calcula un promedio de gusto por género, 
y sugiere películas de diferentes plataformas 
de streaming para el género elegido,
esta programa ayuda a los universitarios a 
decidir qué ver en sus ratos libres.
Para usar el programa, simplemente ejecútalo 
y responde las preguntas que te hará.
Autor: Juan Pablo Romero Anaya
"""

"""
Importamos las librerías necesarias para el programa,
estas librerías nos ayudarán a generar números 
aleatorios y a manejar tiempos de espera,
para mejorar la experiencia del usuario.
"""
import random
import time 



print("\n")
#La Bienvenida, la creamos como variable para poder modificarla.

bienv = ("Bienvenid@ Universitari@, "
              "Al Recomendador de Películas para Universitarios.")
print(bienv)
print("Descubre qué ver en tus ratos libres.")
print("Antes de Recomendarte una Película, responde unas preguntas")
# Aquí empieza el programa y le damos la bienvenida al usuario
print("\n")

# Preguntas de gusto por género
miedo_punt = int(input("Del 0 al 100, "
                       "¿Cuánto te gustan las películas de Miedo?: "))
comedia_punt = int(input("Del 0 al 100, "
                         "¿Cuánto te gustan las películas de Comedia?: "))


def punt(miedo_punt, comedia_punt):

    """
    Calcula el promedio de gusto por género entre miedo y comedia.
    Recibe dos parámetros: miedo_punt y comedia_punt.
    Responde con un mensaje personalizado 
    según el género que más le guste al usuario.
    """

    if ((0 <= miedo_punt <= 100) and (0 <= comedia_punt <= 100)):
        promediopunt = (miedo_punt + comedia_punt) / 2
        print(f"Tu promedio entre Miedo y Comedia es: {promediopunt}")
        if miedo_punt < comedia_punt:
            print("Ahhh, te gusta más la comedia!!!")
        else:
            print("Ahhh, te gusta más el miedo!!!")
    else:
        print("El valor tenía que ser de un rango"
              "del 0 al 100, para el miedo y comedia.")


punt(miedo_punt, comedia_punt)  
# Llamada a la función punt, para calcular el promedio de gusto por género


def mi_punt(md, cm):
    """
    Muestra los gustos del creador del programa.
    Recibe dos parámetros: md y cm.
    Responde con un mensaje personalizado 
    según el género que más le guste al creador.
    """
    if md < cm:
        return ("Fijate que al creador del programa" 
            "le Gusta más la Comedia!")
    else:
        return ("Fijate que al creador del programa"
            "le Gusta más el Miedoooo!")


print(mi_punt(20, 90)) 
# Llamada a la función mi_punt, para comparar 
# con los gustos del creador del programa
print("\n")
generos = ["acción", "comedia", "drama", "terror", "animación"]

def pelis(eleccion):

    """
    Responde según el género elegido por el usuario.
    Recibe un parámetro: eleccion.
    Responde con un mensaje personalizado para cada género.
    """

    if eleccion == "acción":
        return "Elegiste Acción, prepárate para lo chido!!!."
    elif eleccion == "comedia":
        return "Elegiste Comedia, te vas a reír mucho!!!."
    elif eleccion == "drama":
        return "Elegiste Drama, algo más serio y profundo, me encanta!!."
    elif eleccion == "terror":
        return "Elegiste Terror, ¡prepárate para asustarte, hahaha!!!"
    elif eleccion == "animación":
        return "Elegiste Animación, siempre divertidas."


def pedir_genero():

    """
    Esta función pide al usuario que elija un género de película 
    recibiendo su elección y validándola. 
    Devuelve la elección válida del usuario
    y si no es válida, le pide que intente de nuevo.
    """
    

    print("Hay 5 géneros de pelis elige la cuál te guste más: "
          "acción, comedia, drama, terror y animación !!")
    
    print("\n")
    while True:
        print("Escribe el género que prefieras: ")
        eleccionsinm = input("")
        eleccion = eleccionsinm.lower()
        if eleccion in generos:
            print(pelis(eleccion))
            return eleccion
        else:
            print("Opción No Válida, Intenta de Nuevo: ")
            print("Hay 5 géneros de pelis elige la cuál te guste más: "
                  "acción, comedia, drama, terror y animación !!")


eleccion = pedir_genero()

# Diccionarios con las películas recomendadas 
# por plataforma para cada género

accionb = {
    "️ ⚪️ DISNEY +": ["ROGUE ONE", "PIRATAS DEL CARIBE"],
    " 🔵 PRIME VIDEO": ["TOP GUN MAVERICK", "DANGER IN THE MOUNTAIN"],
    " 🔴 NETFLIX": ["THE KILLER", "RED NOTICE"],
    " 🟣️ HBO MAX": ["MAD MAX, FURY ROAD", "KONG, SKULL ISLAND"],
    " 🟠 PARAMOUNT +": ["TRANSFORMERS, AGE OF EXTINCTION", "BUMBLEBLEE"],
    " ⚫️ APPLE TV+": ["THE GORGE", "THE FAMILY PLAN"]
}

comediab = {
    " ⚪️️ DISNEY +": ["HOME ALONE", "THE PRINCESS DIARIES"],
    " 🔵 PRIME VIDEO": ["THE UNDERDOGGS", "ANYTHINGS POSSIBLE"],
    " 🔴 NETFLIX": ["DO REVENGE", "ME TIME"],
    " 🟣️ HBO MAX": ["FREE GUY", "THE 40-YEAR OLD VIRGIN"],
    " 🟠️ PARAMOUNT +": ["MEAN GIRLS", "HOW TO LOSE A GUY IN 10 DAYS"],
    " ⚫️ APPLE TV+": ["FLORA AND SON", "ON THE ROCKS"]
}

dramab = {
    " ⚪️️ DISNEY +": ["TITANIC", "BOHEMIAN RHAPSODY"],
    " 🔵️ PRIME VIDEO": ["PARASITE", "ARGENTINA - 1985"],
    " 🔴 NETFLIX": ["ROMA", "MARRIAGE STORY"],
    " 🟣️ HBO MAX": ["JOKER", "GOODFELLAS"],
    " 🟠️ PARAMOUNT +": ["GOOD WILL HUNTING", "AMERICAN BEAUTY"],
    " ⚫️ APPLE TV+": ["PALMER", "FINCH"]
}

terrorb = {
    " ⚪️ DISNEY +": ["LA SAGA DEL ALIEN", "THE EXORCIST"],
    " 🔵 PRIME VIDEO": ["TALK TO ME", "MIDSOMMAR"],
    " 🔴 NETFLIX": ["FEAR STREET", "EL HOYO"],
    " 🟣️ HBO MAX": ["THE CONJURING", "THE SHINING"],
    " 🟠️ PARAMOUNT +": ["SMILE", "SCREAM (CUALQUIERA)"],
    " ⚫️ APPLE TV+": ["SERVANT", "THE LOST BUS"]
}

animacionb = {
    " ⚪️️ DISNEY +": ["COCO", "INSIDE OUT 2"],
    " 🔵 PRIME VIDEO": ["GHOST IN THE SHELL", "RANGO"],
    " 🔴 NETFLIX": ["PINOCHO (GUILLERMO DEL TORO)",
                     "MITCHELLS CONTRA LAS MÁQUINAS"],
    " 🟣️ HBO MAX": ["EL VIAJE DE CHIHIRO", "PRINCESA MONONOKE"],
    " 🟠️ PARAMOUNT +": ["BOB ESPONJA", "LOS PINGÜINOS DE MADAGASCAR"],
    " ⚫️ APPLE TV+": ["WOLFWALKERS", "LUCK"]
}
""" 
Condicionales para mostrar las recomendaciones 
de películas según el género elegido 
recibiendo la elección del usuario y mostrando las películas 
de cada plataforma para el género elegido,
tambien incluye tiempos de espera para 
mejorar la experiencia del usuario.
"""

if eleccion == "acción":
    time.sleep(3)
    for plataformas, pelis_lista in accionb.items():
        time.sleep(0.5)
        print(f"\n {plataformas}:")
        for peli in pelis_lista:
            print(f"\n - {peli}")

elif eleccion == "comedia":
    time.sleep(3)
    for plataformas, pelis_lista in comediab.items():
        time.sleep(0.5)
        print(f"\n {plataformas}:")
        for peli in pelis_lista:
            print(f"\n - {peli}")

elif eleccion == "drama":
    time.sleep(3)
    for plataformas, pelis_lista in dramab.items():
        time.sleep(0.5) 
        print(f"\n {plataformas}:")
        for peli in pelis_lista:
            print(f"\n - {peli}")

elif eleccion == "terror":
    time.sleep(3)
    for plataformas, pelis_lista in terrorb.items():
        time.sleep(0.5) 
        print(f"\n {plataformas}:")
        for peli in pelis_lista:
            print(f"\n - {peli}")

elif eleccion == "animación":
    time.sleep(3)
    for plataformas, pelis_lista in animacionb.items():
        time.sleep(0.5)
        print(f"\n {plataformas}:")
        for peli in pelis_lista:
            print(f"\n - {peli}")

# Aquí terminan las recomendaciones de películas según el género elegido

calificacion = int(input("\n Del 0 al 100, "
                         "¿Qué calificación le das a "
                         "este recomendador de pelis?: "))


def calif(calificacion):
    """
    Responde según la calificación 
    dada por el usuario.
    Recibe un parámetro: calificacion.
    Responde con un mensaje personalizado s
    egún la calificación dada.
    """
    if 0 <= calificacion <= 100:
        return f"Gracias por calificar con un {calificacion},"
    else:
        return "El valor tenía que ser de un rango del 0 al 100."


print(calif(calificacion))  
# Llamada a la función calif, para responder según la calificación dada

mi_fav = [["Acción"], ["Avengers Endgame"]]  
# Lista con el género y película favorita del creador del programa

print(f"Por cierto, mi género favorito y peli es: \
      \n {mi_fav[0][0]} y {mi_fav[1][0]}.")
print("\n")

# Modificamos la variable bienvenida para el mensaje final
final = bienv.replace("Bienvenid@ Universitari@, Al", "Gracias por usar el")
print(final)

def despedida():

    """ 
    Esta función elige aleatoriamente 
    una despedida para el usuario, 
    recibiendo un valor aleatorio entre 0 y 1 
    Y devolviendo un mensaje personalizado.
    """
    
    valor = random.random()
    if valor < 0.5:
        return "Nos vemos pronto!!"
    else:
        return "Hasta la próxima!!"
    
print("Hoy mi mood me dice que me despida así: ", despedida())

print("Juan Pablo Romero Anaya, "
      "TEC DE MONTERREY, 10/10/25, A01715182")
print("Te gustaria revisar otro género?, vuelve a correr el programa!!")
print("Fin del Programa")
# faltaria el tema de archivos

# Aquí termina el programa
