from alchemyClasses.rentar import rentar
from alchemyClasses import db

#Ver los registros de una tabla
def ver_rentas():
    for renta in rentar.query.all():
        print(renta)
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_renta(id_renta):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        print(renta)
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")

    
#Modificar la fecha de la renta
def cambiar_fecha_random(fecha_nueva):
    rentas = rentar.query.all()
    if len(rentas) >0:#Cambiar el nombre del usuario de en medio
        renta = rentas[len(rentas)//2]
        renta.fecha_renta = fecha_nueva
        db.session.commit()

def cambiar_fecha_renta(id_renta, fecha_nueva):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    if renta is not None:
        renta.fecha_renta = fecha_nueva
        db.session.commit()
    else:
        print("La renta con id = "+ str(id_renta) + " no existe")

        
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