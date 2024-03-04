from alchemyClasses.peliculas import peliculas
from alchemyClasses import db

#CRUD: Create, Read, Update, Delete
#Crear un registro
def crear_pelicula(nombre, genero=None, duracion=None, inventario=1):
    nueva_pelicula = peliculas(nombre, genero, duracion, inventario)
    db.session.add(nueva_pelicula)
    db.session.commit()

#Ver los registros de una tabla
def ver_peliculas():
    return peliculas.query.all()
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_pelicula(id_pelicula):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        print(pelicula)
        return str(pelicula)
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")
 
 # Editar_pelicula completa
def editar_pelicula(id_pelicula, nombre_nuevo, genero_nuevo, duracion_nueva, inventario_nuevo):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        pelicula.nombre = nombre_nuevo
        pelicula.genero = genero_nuevo
        pelicula.duracion = duracion_nueva
        pelicula.inventario = inventario_nuevo
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")
        
 
        
# Update the name of a movie by its id
def cambiar_nombre_peli_por_id(id_pelicula, nombre_nuevo):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        pelicula.nombre = nombre_nuevo
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")
        
# Update el genero de una pelicula por su id
def cambiar_genero_peli_por_id(id_pelicula, genero_nuevo):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        pelicula.genero = genero_nuevo
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")
        
# Update la duracion de una pelicula por su id
def cambiar_duracion_peli_por_id(id_pelicula, duracion_nueva):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        pelicula.duracion = duracion_nueva
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")
 
 # Update el inventario de una pelicula por su id       
def cambiar_inventario_peli_por_id(id_pelicula, inventario_nuevo):
    pelicula = peliculas.query.filter(peliculas.idPelicula == id_pelicula).first()
    if pelicula is not None:
        pelicula.inventario = inventario_nuevo
        db.session.commit()
    else:
        print("La pelicula con id = "+ str(id_pelicula) + " no existe")

    
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