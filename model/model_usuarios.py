from alchemyClasses.usuarios import usuarios
from alchemyClasses import db

#Ver los registros de una tabla
def ver_usuarios():
    for usuario in usuarios.query.all():
        print(usuario)
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_usuario(id_usuario):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        print(usuario)
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
    
#Actualizar la columna nombre de un registro
def cambiar_nombre_usuario_random(nombre_nuevo):
    users = usuarios.query.all()
    if len(users)>0:#Cambiar el nombre del usuario de en medio
        user = users[len(users)//2]
        user.nombre = nombre_nuevo
        db.session.commit()
            
        

def cambiar_nombre_usuario_por_id(id_usuario, nombre_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.nombre = nombre_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")

    
def cambiar_nombre_usuario_por_nombre(nombre, nombre_nuevo):
    usuario = usuarios.query.filter(usuarios.nombre == nombre).first()
    if usuario is not None:
        usuario.nombre = nombre_nuevo
        db.session.commit()
    else:
        print("El usuario con nombre = "+ nombre + " no existe")

    
#Eliminar un registro por id
def eliminar_usuario(id_usuario):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        db.session.delete(usuario)
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")

    
#Eliminar todos los registros
def eliminar_todos_los_usuarios():
    for usuario in usuarios.query.all():
        db.session.delete(usuario)
    db.session.commit()