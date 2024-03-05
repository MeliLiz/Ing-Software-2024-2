from flask import Blueprint, request, render_template, flash, url_for, redirect
from model import model_rentar as mr
from datetime import datetime

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
        
        if dias_renta == "":
            dias_renta = 5
        
        if 'devuelta' in request.form:
            estatus = 1
        else:
            estatus = 0
        print(estatus)
        
        ret = mr.crear_renta(id_usuario, id_pelicula, fecha_renta, dias_renta, estatus)
        
        if ret == -1:
            return render_template("CrearRenta.html", mensaje="El id de usuario o el id de pelicula no existe", id_usuario = id_usuario, id_pelicula = id_pelicula, fecha_renta = fecha_renta, dias_renta = dias_renta)
        else:
            return render_template("Exito.html")
    
"""@renta_blueprint.route('/borrar', methods = ['GET', 'POST'])
def borrar_renta():
    if request.method == "GET":
        return render_template('BorrarRenta.html')
    else:
        id_renta = request.form["idRenta"]
        print(id_renta)
        mr.eliminar_renta(id_renta)
        
        return render_template("Exito.html")"""
        
@renta_blueprint.route('/edit', methods = ["GET","POST"])
def editar_estatus_renta():
    if request.method == "GET":
        return render_template("EditarRenta.html")
    else:
        id_renta = request.form["idRenta"]
        print(id_renta)
        
        res = mr.encontrar_renta(id_renta)
        
        if res == -1:
            return render_template("EditarRenta.html", mensaje="La renta con id = "+id_renta+" no existe")
        else:
            return redirect(url_for('renta.editar_estatus_renta_form', id_renta = id_renta))
    
    
@renta_blueprint.route('/edit/<id_renta>', methods = ["GET", "POST"])
def editar_estatus_renta_form(id_renta):
    if request.method == "GET":
        res = mr.encontrar_renta(id_renta)
        print(res)
        res = res.split(",")
        usuario = int(res[0])
        pelicula = int(res[1])
        fecha = datetime.strptime(res[2], "%Y-%m-%d %H:%M:%S")
        dias = res[3]
        if dias != "None":
            dias = int(dias)
        else:
            dias = None
        estatus = int(res[4])
        
        return render_template('EditarRentaForm.html', usuario=usuario, pelicula=pelicula, fecha=fecha, dias=dias, estatus=estatus)
    else:
        if 'devuelta' in request.form:
            estatus = 1
        else:
            estatus = 0
        print(estatus)
        
        mr.cambiar_estatus_renta_por_id(id_renta, estatus)
        
        return render_template("Exito.html")
    
@renta_blueprint.route('/rentas')
def mostrar_rentas():
    rentas = mr.ver_rentas()
    return render_template("MostrarRentas.html", rentas=rentas)