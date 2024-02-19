from alchemyClasses.peliculas import peliculas
from alchemyClasses import db

#Ver los registros de una tabla
def ver_peliculas():
    for pelicula in peliculas.query.all():
        print(pelicula)
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_pelicula(id_pelicula):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        print(pelicula)
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")
    
#Actualizar la columna nombre de un registro
def cambiar_nombre_peli_random(nombre_nuevo):
    pelis = peliculas.query.all()
    if len(pelis)>0:#Cambiar el nombre del usuario de en medio
        peli = pelis[len(pelis)//2]
        peli.nombre = nombre_nuevo
        db.session.commit()

def cambiar_nombre_peli_por_id(id_pelicula, nombre_nuevo):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        pelicula.nombre = nombre_nuevo
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")

    
def cambiar_nombre_peli_por_nombre(nombre, nombre_nuevo):
    pelicula = peliculas.query.filter(peliculas.nombre == nombre).first()
    if pelicula is not None:
        pelicula.nombre = nombre_nuevo
        db.session.commit()
    else:
        print("La pelicula con nombre = \""+ nombre + "\" no existe")

    
#Eliminar un registro por id
def eliminar_pelicula(id_pelicula):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        db.session.delete(pelicula)
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")

    
#Eliminar todos los registros
def eliminar_todas_las_peliculas():
    for pelicula in peliculas.query.all():
        db.session.delete(pelicula)
    db.session.commit()