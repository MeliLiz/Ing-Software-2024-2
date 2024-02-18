from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db

from model.model_rentar import ver_rentas, encontrar_renta, cambiar_fecha_renta, eliminar_renta, eliminar_todas_las_rentas
from model.model_peliculas import ver_peliculas, encontrar_pelicula, cambiar_nombre_peli_por_id, cambiar_nombre_peli_por_nombre, eliminar_pelicula, eliminar_todas_las_peliculas
from model.model_usuarios import ver_usuarios, encontrar_usuario, cambiar_nombre_usuario_por_id, cambiar_nombre_usuario_por_nombre, eliminar_usuario, eliminar_todos_los_usuarios

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        
        ##Pruebas de usuarios
        
        #ver_usuarios()
        #encontrar_usuario(30)
        #cambiar_nombre_usuario_por_id(40, "Alan")
        #cambiar_nombre_usuario_por_nombre("Carlos", "Roberto")
        #eliminar_usuario(31)####
        #eliminar_todos_los_usuarios()
        
        ##Pruebas de peliculas
        #ver_peliculas()
        #encontrar_pelicula(17)
        #cambiar_nombre_peli_por_id(16, "El castillo vagabundo")
        #cambiar_nombre_peli_por_nombre("El sorprendente secreto de la paz", "Los amigos")
        #eliminar_pelicula(20)
        #eliminar_todas_las_peliculas()
        
        #Pruebas de rentas
        ver_rentas() #######
        #encontrar_renta(10)
        #cambiar_fecha_renta(10, "2021-10-10")
        #eliminar_renta(11)
        #eliminar_todas_las_rentas()