print ( "Bienvenid@ Universitari@, al Recomendador de Películas para Universitarios. " )
print ( "Descubre qué ver en tus ratos libres." )


print ( "Antes de Recomendarte una Película, responde unas preguntas" )

miedo_punt = int(input( "Del 0 al 100, ¿Cuánto te gustan las películas de Miedo?: " ))
comedia_punt = int(input( "Del 0 al 100, ¿Cuánto te gustan las películas de Comedia?: " ))

if miedo_punt < comedia_punt:
        print ( "Ahhh, te gusta más la comedia!!!" )
else:
        print ( "Ahhh, te gusta más el miedo!!!" )


promediopunt = ( miedo_punt + comedia_punt ) / 2
print ( f" Tu promedio entre Miedo y Comedia es: {promediopunt} ")

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
