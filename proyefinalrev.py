# Recomendador de Películas para Universitarios, programa en Python el cual recomienda películas según el género que el usuario prefiera.
# Juan Pablo Romero Anaya, A01715182, 10/10/25  
print("\n")
# La Bienvenida, la creamos como variable para poder modificarla fácilmente
bienvenida = "Bienvenid@ Universitari@, al Recomendador de Películas para Universitarios. "  
print ( bienvenida )

print ( "Descubre qué ver en tus ratos libres." )
print ( "Antes de Recomendarte una Película, responde unas preguntas" ) 
# Aquí empieza el programa y le damos la bienvenida al usuario
print("\n")

# Preguntas de gusto por género
miedo_punt = int(input( "Del 0 al 100, ¿Cuánto te gustan las películas de Miedo?: " ))
comedia_punt = int(input( "Del 0 al 100, ¿Cuánto te gustan las películas de Comedia?: " ))

def punt (miedo_punt, comedia_punt): # Función para calcular el promedio de gusto por género
    if (miedo_punt <= 100 and comedia_punt <= 100):
        promediopunt = float( miedo_punt + comedia_punt ) / 2
        print ( f" Tu promedio entre Miedo y Comedia es: {promediopunt} ")
        if miedo_punt < comedia_punt:
            print ( "Ahhh, te gusta más la comedia!!!" )
        else:
            print ( "Ahhh, te gusta más el miedo!!!" )
    else:
        print (" El valor tenía que ser de un rango del 0 al 100, para el miedo y comedia.")
punt (miedo_punt, comedia_punt) # Llamada a la función punt, para calcular el promedio de gusto por género


def mi_punt (md, cm): # Función para comparar con los gustos del creador del programa
    if md < cm:
        return "Fijate que al creador del programa le Gusta más la Comedia!"
    else:
        return "Fijate que al creador del programa le Gusta más el Miedoooo!"
    
print(mi_punt (20, 90) ) # Llamada a la función mi_punt, para comparar con los gustos del creador del programa
print("\n")

print ("Hay 5 géneros de pelis elige la cuál te guste más: acción, comedia, drama, terror y animación !! ") # Indicamos los géneros disponibles
print("\n")

generos = ["acción", "comedia", "drama", "terror", "animación"] # Lista de géneros disponibles

def pelis (generos): # Función para responder según el género elegido
    if (generos == "acción"):
        return "Elegiste Acción, prepárate para lo chido!!!."
    elif (generos == "comedia"):
        return "Elegiste Comedia, te vas a reír mucho!!!."
    elif (generos == "drama"):
        return "Elegiste Drama, algo más serio y profundo, me encanta!!!."
    elif (generos == "terror"):
        return "Elegiste Terror, ¡prepárate para asustarte, hahaha!!!"
    elif (generos == "animación"):
        return "Elegiste Animación, siempre divertidas."

i = 0 # Bucle para validar la entrada del usuario
while i < 2:
    eleccionsinm = input ("")
    eleccion = eleccionsinm.lower() # usamos la función predefinida lower para evitar errores de mayúsculas y minúsculas

    if eleccion in generos: # Validamos que la entrada esté en la lista de géneros
        print (pelis (eleccion))
        i = i + 3
    else:        # Si la entrada no es válida, pedimos que ingrese de nuevo
        print ("Opción No Valida, Intenta de Nuevo: ")
        i = i + 0

accionb = {  # Diccionario con las películas recomendadas por plataforma para cada género
    
    "️⚪️ DISNEY +" : ["ROGUE ONE", "PIRATAS DEL CARIBE"],
    "🔵 PRIME VIDEO" : ["TOP GUN MAVERICK", "DANGER IN THE MOUNTAIN"],
    "🔴 NETFLIX" : ["THE KILLER", "RED NOTICE"],
    "🟣️ HBO MAX" : ["MAD MAX, FURY ROAD", "KONG, SKULL ISLAND"],
    "🟠 PARAMOUNT PLUS" : ["TRANSFORMERS, AGE OF EXTINCTION", "BUMBLEBLEE"],
    "⚫️ APPLE TV+" : ["THE GORGE", "THE FAMILY PLAN"]
    }

comediab = {
    "⚪️️ DISNEY +" : ["HOME ALONE", "THE PRINCESS DIARIES"],
    "🔵 PRIME VIDEO" : ["THE UNDERDOGGS", "ANYTHINGS POSSIBLE"],
    "🔴 NETFLIX" : ["DO REVENGE", "ME TIME"],
    "🟣️ HBO MAX" : ["FREE GUY", "THE 40-YEAR OLD VIRGIN"],
    "🟠️ PARAMOUNT PLUS" : ["MEAN GIRLS", "HOW TO LOSE A GUY IN 10 DAYS"],
    "⚫️ APPLE TV+" : ["FLORA AND SON", "ON THE ROCKS"]
    }

dramab = {
    "⚪️️ DISNEY +" : ["TITANIC", "BOHEMIAN RHAPSODY"],
    "🔵️ PRIME VIDEO" : ["PARASITE", "ARGENTINA - 1985"],
    "🔴 NETFLIX" : ["ROMA", "MARRIAGE STORY"],
    "🟣️ HBO MAX" : ["JOKER", "GOODFELLAS"],
    "🟠️ PARAMOUNT PLUS" : ["GOOD WILL HUNTING", "AMERICAN BEAUTY"],
    "⚫️ APPLE TV+" : ["PALMER", "FINCH"]
    }

terrorb = {
    "⚪️ DISNEY +" : ["LA SAGA DEL ALIEN", "THE EXORCIST"],
    "🔵 PRIME VIDEO" : ["TALK TO ME", "MIDSOMMAR"],
    "🔴 NETFLIX" : ["FEAR STREET", "EL HOYO"],
    "🟣️ HBO MAX" : ["THE CONJURING", "THE SHINING"],
    "🟠️ PARAMOUNT PLUS" : ["SMILE", "SCREAM (CUALQUIERA)"],
    "⚫️ APPLE TV+" : ["SERVANT", "THE LOST BUS"]
    }

animaciónb = {
    "⚪️️ DISNEY +" : ["COCO", "INSIDE OUT 2"],
    "🔵 PRIME VIDEO" : ["GHOST IN THE SHELL", "RANGO"],
    "🔴 NETFLIX" : ["PINOCHO (GUILLERMO DEL TORO)", "MITCHELLS CONTRA LAS MÁQUINAS"],
    "🟣️ HBO MAX" : ["EL VIAJE DE CHIHIRO", "PRINCESA MONONOKE"],
    "🟠️ PARAMOUNT PLUS" : ["BOB ESPONJA", "LOS PINGÜINOS DE MADAGASCAR"],
    "⚫️ APPLE TV+" : ["WOLFWALKERS", "LUCK"]
    }
    

# Condicionales para mostrar las películas recomendadas según el género elegido
if (eleccion == "acción"): 
    for plataformas, pelis in accionb.items():
        print (f"\n {plataformas}:")
        for peli in pelis:
            print (f"\n - {peli}")
            
elif (eleccion == "comedia"):
    for plataformas, pelis in comediab.items():
        print(f"\n {plataformas}:")
        for peli in pelis:
            print (f"\n - {peli}")
            
elif (eleccion == "drama"):
    for plataformas, pelis in dramab.items():
        print(f"\n {plataformas}:")
        for peli in pelis:
            print (f"\n - {peli}")

elif (eleccion == "terror"):
    for plataformas, pelis in terrorb.items():
        print(f"\n {plataformas}:")
        for peli in pelis:
            print (f"\n - {peli}")
            
elif (eleccion == "animación"):
    for plataformas, pelis in animaciónb.items():
        print(f"\n {plataformas}:")
        for peli in pelis:
            print (f"\n - {peli}")
 # Aquí terminan las recomendaciones de películas según el género elegido
            
calificacion = int(input( "\n Del 0 al 100, ¿Qué calificación le das a este recomendador de pelis?: " )) # Preguntamos la calificación del usuario

def calif (calificacion): # Función para responder según la calificación dada
    if (calificacion <= 100):
        return f"Gracias por calificar con un {calificacion}, seguiremos mejorando!!"
    else:
        return "El valor tenía que ser de un rango del 0 al 100."
print (calif (calificacion) ) # Llamada a la función calif, para responder según la calificación dada

mi_fav = [["Acción"], ["Avengers Endgame"]] # Lista con el género y película favorita del creador del programa

print ( f"Por cierto, mi género favorito y peli es: \n {mi_fav[0][0]} y {mi_fav[1][0]}. ") # Mostramos el género y película favorita del creador del programa
print("\n")

# Modificamos la variable bienvenida para el mensaje final
final = bienvenida.replace( "Bienvenid@ Universitari@, al", "Gracias por usar el" ) #usamos la función predefinida replace para modificar la variable bienvenida 
print ( final ) 
print ( "Juan Pablo Romero Anaya, TEC DE MONTERREY, 10/10/25, A01715182" )    # Créditos del programa
print ( "Fin del Programa" ) 
# faltaria el tema de archivos

# Aquí termina el programa


    