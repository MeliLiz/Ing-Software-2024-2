from flask import Blueprint, request, render_template, flash, url_for, redirect
from model import model_usuarios as mu

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')


@usuario_blueprint.route('/registro', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == "GET":
        return render_template('CrearUser.html')
    else:
        
        nombre = request.form["inputNombre"]
        print(nombre)
        apellidoP = request.form["inputApellidoPaterno" ]
        print(apellidoP)
        apellidoM = request.form["inputApellidoMaterno"]
        print(apellidoM)
        correo = request.form["inputEmail"]
        print(correo)
        password = request.form["password"]
        print(password)
        
        if 'superuser' in request.form:
            superuser = 1
        else:
            superuser = 0
        print(superuser)
            
        
        retorno = mu.crear_usuario(nombre, apellidoP, password, apellidoM, correo, None, superuser)
        
        if retorno == -1:
            return render_template("CrearUser.html", mensaje="El correo ingresado ya existe, intente con otro correo", nombre = nombre, apellidoP = apellidoP, apellidoM = apellidoM, superuser = superuser, password = password)
        else:
            return render_template("Exito.html")
    
@usuario_blueprint.route('/borrar', methods=['GET', 'POST'])
def borrar_usuario():
    if request.method == "GET":
        return render_template('BorrarUser.html')
    else:
        id_usuario = request.form["idCliente"]
        print(id_usuario)
        mu.eliminar_usuario(id_usuario)
        return render_template("Exito.html")


@usuario_blueprint.route('/edit', methods=['GET', 'POST'])
def editar_usuario():
    if request.method == "GET":
        return render_template('EditarUser.html')
    else:
        id_usuario = request.form["idCliente"]
        print(id_usuario)
        
        return redirect(url_for('usuario.editar_usuario_form', id_usuario = id_usuario))
        
  
    
@usuario_blueprint.route('/edit/<id_usuario>', methods=['GET', 'POST'])
def editar_usuario_form(id_usuario):
    if request.method == "GET":
        res = mu.encontrar_usuario(id_usuario)
        print(res)
        res = res.split(",")
        nombre = res[0]
        apellidoP = res[1]
        apellidoM = res[2]
        email = res[3]
        superuser = int(res[4])
        password = res[5]
        return render_template('EditarUserForm.html', nombre = nombre, apellidoP = apellidoP, apellidoM = apellidoM, email = email, superuser = superuser, password = password)
    else:
        nombre = request.form["inputNombre"]
        print(nombre)
        apellidoP = request.form["inputApellidoPaterno" ]
        print(apellidoP)
        apellidoM = request.form["inputApellidoMaterno"]
        print(apellidoM)
        correo = request.form["inputEmail"]
        print(correo)
        password = request.form["password"]
        print(password)
        
        if 'superuser' in request.form:
            superuser = 1
        else:
            superuser = 0
        print(superuser)
        
        mu.editar_usuario(id_usuario, nombre, apellidoP, password, apellidoM, correo, None, superuser)
        
        return render_template("Exito.html")
    
    
@usuario_blueprint.route('/usuarios')
def mostrar_usuarios():
    usuarios = mu.ver_usuarios()
    return render_template("MostrarUsuarios.html", usuarios=usuarios)