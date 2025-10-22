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
