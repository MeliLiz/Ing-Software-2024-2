from flask import Blueprint, request, render_template, flash, url_for
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
            
        
        mu.crear_usuario(nombre, apellidoP, password, apellidoM, correo, None, superuser)
        
        return render_template("Exito.html")
    

