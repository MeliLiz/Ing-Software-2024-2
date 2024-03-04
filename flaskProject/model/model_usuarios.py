from alchemyClasses.usuarios import usuarios
from alchemyClasses import db

#CRUD

#Crear un nuevo registro
def crear_usuario(nombre, apPat, password, apMat=None, email=None, profilePicture=None, superUser=None):
    nuevo_usuario = usuarios(nombre, apPat, password, apMat, email, profilePicture, superUser)
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return 0
    except:
        return -1

#Ver los registros de una tabla
def ver_usuarios():
    return usuarios.query.all()
        
#Filtrar los registros de una tabla por id (solo que sea exactamente igual a)
def encontrar_usuario(id_usuario):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        print(usuario)
        return str(usuario)
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        return -1

# Actualizar un usuario completo
def editar_usuario(id_usuario, nombre_nuevo, apPat_nuevo, password_nuevo, apMat_nuevo, email_nuevo, profilePicture_nuevo, superUser_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.nombre = nombre_nuevo
        usuario.apPat = apPat_nuevo
        usuario.password = password_nuevo
        usuario.apMat = apMat_nuevo
        usuario.email = email_nuevo
        usuario.profilePicture = profilePicture_nuevo
        usuario.superUser = superUser_nuevo
        db.session.commit()
        return 0
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        return -1
        
# Actualizar el nombre de un usuario por su id
def cambiar_nombre_usuario_por_id(id_usuario, nombre_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.nombre = nombre_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        
# Actualizar el apellido paterno de un usuario por su id
def cambiar_apPat_usuario_por_id(id_usuario, apPat_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.apPat = apPat_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        
# Actualizar el apellido materno de un usuario por su id
def cambiar_apMat_usuario_por_id(id_usuario, apMat_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.apMat = apMat_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        
# Actualizar el password de un usuario por su id
def cambiar_password_usuario_por_id(id_usuario, password_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.password = password_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        
# Actualizar el email de un usuario por su id
def cambiar_email_usuario_por_id(id_usuario, email_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.email = email_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        
# Actualizar el profilePicture de un usuario por su id

# Actualizar el superUser de un usuario por su id
def actualizar_superuser(id_usuario, superUser_nuevo):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        usuario.superUser = superUser_nuevo
        db.session.commit()
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")

    
#Eliminar un registro por id
def eliminar_usuario(id_usuario):
    usuario = usuarios.query.filter(usuarios.idUsuario == id_usuario).first()
    if usuario is not None:
        db.session.delete(usuario)
        db.session.commit()
        return 0
    else:
        print("El usuario con id = "+ str(id_usuario) + " no existe")
        return -1
    
#Eliminar todos los registros
def eliminar_todos_los_usuarios():
    for usuario in usuarios.query.all():
        db.session.delete(usuario)
    db.session.commit()