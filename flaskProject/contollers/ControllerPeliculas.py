from flask import Blueprint, request, render_template, flash, url_for, redirect
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
        ret = mp.eliminar_pelicula(id_pelicula)
        
        if ret == -1:
            return render_template("BorrarPelicula.html", mensaje="La pelicula con id = "+id_pelicula+" no existe")
        else:
            return render_template("Exito.html")
    
@pelicula_blueprint.route('/edit', methods = ["GET","POST"])
def editar_pelicula():
    if request.method == "GET":
        return render_template("EditarPelicula.html")
    else:
        id_pelicula = request.form["idPeli"]
        print(id_pelicula)
        res = mp.encontrar_pelicula(id_pelicula)
        if res == -1:
            return render_template("EditarPelicula.html", mensaje="La pelicula con id = "+id_pelicula+" no existe")
        else:
            return redirect(url_for('pelicula.editar_pelicula_form', id_pelicula = id_pelicula))
    
    
@pelicula_blueprint.route('/edit/<id_pelicula>', methods = ["GET", "POST"])
def editar_pelicula_form(id_pelicula):
    if request.method == "GET":
        res = mp.encontrar_pelicula(id_pelicula)
        print(res)
        res = res.split(",")
        nombre = res[0]
        genero = res[1]
        duracion = int(res[2])
        inventario = int(res[3])
        
        return render_template('EditarPeliculaForm.html', nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
    else:
        nombre = request.form["inputNombre"]
        print(nombre)
        genero = request.form["genero"]
        print(genero)
        duracion = request.form["inputDuracion"]
        print(duracion)
        inventario = request.form["inputInventario"]
        print(inventario)
        
        mp.editar_pelicula(id_pelicula, nombre, genero, duracion, inventario)
        
        return render_template("Exito.html")


@pelicula_blueprint.route('/peliculas')
def mostrar_peliculas():
    peliculas = mp.ver_peliculas()
    return render_template("MostrarPeliculas.html", peliculas=peliculas)
        