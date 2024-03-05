from alchemyClasses.rentar import rentar
from alchemyClasses import db

#CRUD

#Crear un registro
def crear_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
    try:
        nueva_renta = rentar(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
        db.session.add(nueva_renta)
        db.session.commit()
        return 0
    except:
        return -1
    
#Ver los registros de una tabla
def ver_rentas():
    return rentar.query.all()
        
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_renta(id_renta):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        print(renta)
        return str(renta)
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")
        return -1

# Actualizar el id de usuario de una renta por su id
def cambiar_id_usuario_renta_por_id(id_renta, id_usuario_nuevo):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        renta.idUsuario = id_usuario_nuevo
        db.session.commit()
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")
        
# Actualizar el id de pelicula de una renta por su id
def cambiar_id_pelicula_renta_por_id(id_renta, id_pelicula_nuevo):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        renta.idPelicula = id_pelicula_nuevo
        db.session.commit()
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")
        
# Actualizar los dias de renta de una renta por su id
def cambiar_dias_de_renta_renta_por_id(id_renta, dias_de_renta_nuevos):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        renta.dias_de_renta = dias_de_renta_nuevos
        db.session.commit()
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")
        
# Actualizar el estatus de una renta por su id
def cambiar_estatus_renta_por_id(id_renta, estatus_nuevo):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        renta.estatus = estatus_nuevo
        db.session.commit()
        return 0
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")
        return -1
        
#Eliminar un registro por id
def eliminar_renta(id_renta):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        db.session.delete(renta)
        db.session.commit() 
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")


#Eliminar todos los registros
def eliminar_todas_las_rentas():
    for renta in rentar.query.all():
        db.session.delete(renta)
    db.session.commit()