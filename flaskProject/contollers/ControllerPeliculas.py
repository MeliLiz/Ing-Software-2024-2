from flask import Blueprint, request, render_template, flash, url_for
from model import model_peliculas as mp

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')


@pelicula_blueprint.route('/registro', methods = ['GET', 'POST'])
def agregar_pelicula():
    if request.method == "GET":
        return render_template('CrearPelicula.html')
    else: #Es POST
        nombre = request.form["inputNombre"]
        print(nombre)
        genero = request.form["genero"]
        print(genero)
        duracion = request.form["inputDuracion"]
        print(duracion)
        inventario = request.form["inputInventario"]
        print(inventario)
        
        mp.crear_pelicula(nombre, genero, duracion, inventario)
        
        return render_template("Exito.html")
    
@pelicula_blueprint.route('/borrar', methods = ['GET', 'POST'])
def eliminar_pelicula():
    if request.method == "GET":
        return render_template('BorrarPelicula.html')
    else:
        id_pelicula = request.form["idPeli"]
        print(id_pelicula)
        mp.eliminar_pelicula(id_pelicula)
        
        return render_template("Exito.html")