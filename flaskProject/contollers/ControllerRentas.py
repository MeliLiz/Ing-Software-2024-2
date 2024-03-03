from flask import Blueprint, request, render_template, flash, url_for
from model import model_rentar as mr

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/registro', methods = ['GET', 'POST'])
def agregar_renta():
    if request.method == "GET":
        return render_template('CrearRenta.html')
    else: #Es POST
        id_usuario = request.form["inputIdCliente"]
        print(id_usuario)
        id_pelicula = request.form["inputIdPeli"]
        print(id_pelicula)
        fecha_renta = request.form["inputFechaPrestamo"]
        print(fecha_renta)
        dias_renta = request.form["inputDiasRenta"]
        print(dias_renta)
        
        if 'devuelta' in request.form:
            estatus = 1
        else:
            estatus = 0
        print(estatus)
        
        mr.crear_renta(id_usuario, id_pelicula, fecha_renta, dias_renta, estatus)
        
        return render_template("Exito.html")
    
@renta_blueprint.route('/borrar', methods = ['GET', 'POST'])
def borrar_renta():
    if request.method == "GET":
        return render_template('BorrarRenta.html')
    else:
        id_renta = request.form["idRenta"]
        print(id_renta)
        mr.eliminar_renta(id_renta)
        
        return render_template("Exito.html")