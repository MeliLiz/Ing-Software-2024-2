from alchemyClasses.peliculas import peliculas
from alchemyClasses import db

#Ver los registros de una tabla
def ver_peliculas():
    for pelicula in peliculas.query.all():
        print(pelicula)
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_pelicula(id_pelicula):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    print(pelicula)
    
#Actualizar la columna nombre de un registro
def cambiar_nombre_peli_por_id(id_pelicula, nombre_nuevo):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    pelicula.nombre = nombre_nuevo
    db.session.commit()
    
def cambiar_nombre_peli_por_nombre(nombre, nombre_nuevo):
    pelicula = peliculas.query.filter(peliculas.nombre == nombre).first()
    pelicula.nombre = nombre_nuevo
    db.session.commit()
    
#Eliminar un registro por id
def eliminar_pelicula(id_pelicula):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    db.session.delete(pelicula)
    db.session.commit()
    
#Eliminar todos los registros
def eliminar_todas_las_peliculas():
    for pelicula in peliculas.query.all():
        db.session.delete(pelicula)
    db.session.commit()