from alchemyClasses.usuarios import usuarios
from alchemyClasses import db

#Ver los registros de una tabla
def ver_usuarios():
    for usuario in usuarios.query.all():
        print(usuario)
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_usuario(id_usuario):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    print(usuario)
    
#Actualizar la columna nombre de un registro
def cambiar_nombre_usuario_por_id(id_usuario, nombre_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    usuario.nombre = nombre_nuevo
    db.session.commit()
    
def cambiar_nombre_usuario_por_nombre(nombre, nombre_nuevo):
    usuario = usuarios.query.filter(usuarios.nombre == nombre).first()
    usuario.nombre = nombre_nuevo
    db.session.commit()
    
#Eliminar un registro por id
def eliminar_usuario(id_usuario):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    db.session.delete(usuario)
    db.session.commit()
    
#Eliminar todos los registros
def eliminar_todos_los_usuarios():
    for usuario in usuarios.query.all():
        db.session.delete(usuario)
    db.session.commit()