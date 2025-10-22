print ( "Bienvenid@ Universitari@, al Recomendador de Películas para Universitarios. " )
print ( "Descubre qué ver en tus ratos libres." )


print ( "Antes de Recomendarte una Película, responde unas preguntas" )

miedo_punt = int(input( "Del 0 al 100, ¿Cuánto te gustan las películas de Miedo?: " ))
comedia_punt = int(input( "Del 0 al 100, ¿Cuánto te gustan las películas de Comedia?: " ))

if (miedo_punt <= 100 and comedia_punt <= 100):
    promediopunt = ( miedo_punt + comedia_punt ) / 2
    print ( f" Tu promedio entre Miedo y Comedia es: {promediopunt} ")
    if miedo_punt < comedia_punt:
        print ( "Ahhh, te gusta más la comedia!!!" )
    else:
        print ( "Ahhh, te gusta más el miedo!!!" )
else:
    print (" El valor tenía que ser de un rango del 0 al 100, para el miedo y comedia.")
    

def mi_punt (md, cm):
    if md < cm:
        return "Fijate que al creador del programa le Gusta la Comedia!"
    else:
        return "Fijate que al creador del programa le Gusta el Miedoooo!"
print(mi_punt (20, 90) )

print ("Hay 5 géneros de pelis elige la cuál te guste más: acción, comedia, drama, terror y animación !! ")

generos = ["acción", "comedia", "drama", "terror", "animación"]

def pelis (generos):
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

i = 0
while i < 2:
    eleccion = input ("")
    if eleccion in generos:
        print (pelis (eleccion))
        i = i + 3
    else:
        print ("Opción No Valida")
        i = i + 0

acciónb = {
    
    "️⚪️ DISNEY +" : ["ROGUE ONE", "PIRATAS DEL CARIBE"],
    "🔵 PRIME VIDEO" : ["TOP GUN MAVERICK", "DANGER IN THE MOUNTAIN"],
    "🔴 NETFLIX" : ["THE KILLER", "RED NOTICE"],
    "🟣️ HBO MAX" : ["MAD MAX, FURY ROAD", "KONG, SKULL ISLAND"],
    "🟠 PARAMOUNT PLUS" : ["TRANSFORMERS, AGE OF EXTINCTION", "BUMBLEBLEE"],
    "⚫️ APPLE TV+" : ["THE GORGE", "THE FAMILY PLAN"]
    }

comediab = {
    "⚪️️ DISNEY +" : ["HOME ALONE", "THE PRINCESS DIARIES"],
    "🔵 PRIME VIDEO" : ["THE UNDERDOGGS", "ANYTHING´S POSSIBLE"],
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
    


if (eleccion == "acción"):
    for plataformas, pelis in acciónb.items():
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
            
    
print ("Juan Pablo Romero Anaya, TEC DE MONTERREY, 03/10/25, A01715182")    
