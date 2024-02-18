from alchemyClasses.rentar import rentar
from alchemyClasses import db

#Ver los registros de una tabla
def ver_rentas():
    for renta in rentar.query.all():
        print(renta)
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_renta(id_renta):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    print(renta)
    
#Modificar la fecha de la renta
def cambiar_fecha_renta(id_renta, fecha_nueva):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    renta.fecha_renta = fecha_nueva
    db.session.commit()
    
#Eliminar un registro por id
def eliminar_renta(id_renta):
    renta = rentar.query.filter(rentar.idRentar == id_renta).first()
    db.session.delete(renta)
    db.session.commit() 

#Eliminar todos los registros
def eliminar_todas_las_rentas():
    for renta in rentar.query.all():
        db.session.delete(renta)
    db.session.commit()