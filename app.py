from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db

from model.model_rentar import ver_rentas, encontrar_renta, cambiar_fecha_random,cambiar_fecha_renta, eliminar_renta, eliminar_todas_las_rentas
from model.model_peliculas import ver_peliculas, encontrar_pelicula, cambiar_nombre_peli_random,cambiar_nombre_peli_por_id, cambiar_nombre_peli_por_nombre, eliminar_pelicula, eliminar_todas_las_peliculas
from model.model_usuarios import ver_usuarios, encontrar_usuario, cambiar_nombre_usuario_random,cambiar_nombre_usuario_por_id, cambiar_nombre_usuario_por_nombre, eliminar_usuario, eliminar_todos_los_usuarios

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        
        ##Pruebas de usuarios
        
        print("**Clon buster**")
        no_valido = True
        while no_valido:
            print("USUARIOS")
            print("1) Ver usuarios")
            print("2) Encontrar usuario por id")
            print("3) Cambiar nombre de usuario por id")
            print("4) Cambiar nombre de usuario por nombre")
            print("5) Cambiar nombre de usuario random")
            print("6) Eliminar usuario por id")
            print("7) Eliminar todos los usuarios")
            print("PELICULAS")
            print("8) Ver peliculas")
            print("9) Encontrar pelicula por id")
            print("10) Cambiar nombre de pelicula por id")
            print("11) Cambiar nombre de pelicula por nombre")
            print("12) Cambiar nombre de pelicula random")
            print("13) Eliminar pelicula por id")
            print("14) Eliminar todas las peliculas")
            print("RENTAS")
            print("15) Ver rentas")
            print("16) Encontrar renta por id")
            print("17) Cambiar fecha de renta por id")
            print("18) Cambiar fecha de renta random")
            print("19) Eliminar renta por id")
            print("20) Eliminar todas las rentas")
            entrada = input("\nIngresa el número de opción que prefieras: ")
            
            
            try:
                entrada = int(entrada)
                if entrada <1 or entrada >20:
                    print("El número ingresado no es válido")
                else:
                    no_valido = False
                    b = True
                    if entrada==1: #Ver registros de usuarios
                        ver_usuarios()
                    elif entrada==2: #Encontrar usuario por id
                        while b:
                            try:
                                id_usuario = input("Ingresa el id del usuario: ")
                                id_usuario = int(id_usuario)
                                b = False
                                encontrar_usuario(id_usuario)
                            except:
                                print("Debes ingresar un número")
                        
                    elif entrada==3: #Cambiar nombre de usuario por id
                        while b:
                            try:
                                id_usuario = input("Ingresa el id del usuario: ")
                                id_usuario = int(id_usuario)
                                b = False
                                nombre = input("Ingresa el nuevo nombre: ")
                                cambiar_nombre_usuario_por_id(id_usuario, nombre)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==4: #Cambiar nombre de usuario por nombre
                        nombre = input("Ingresa el nombre del usuario: ")
                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                        cambiar_nombre_usuario_por_nombre(nombre, nuevo_nombre)
                    elif entrada==5: #Cambiar nombre de usuario random
                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                        cambiar_nombre_usuario_random(nuevo_nombre)
                    elif entrada==6:
                        while b:
                            try:
                                id_usuario = input("Ingresa el id del usuario: ")
                                id_usuario = int(id_usuario)
                                b = False
                                eliminar_usuario(id_usuario)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==7:
                        eliminar_todos_los_usuarios()
                    elif entrada==8:
                        ver_peliculas()
                    elif entrada==9:
                        while b:
                            try:
                                id_peli = input("Ingresa el id de la película: ")
                                id_peli = int(id_peli)
                                b = False
                                encontrar_pelicula(id_peli)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==10:
                         while b:
                            try:
                                id_peli = input("Ingresa el id de la película: ")
                                id_peli = int(id_peli)
                                b = False
                                nombre = input("Ingresa el nuevo nombre: ")
                                cambiar_nombre_peli_por_id(id_peli, nombre)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==11:
                        nombre = input("Ingresa el nombre de la pelicula: ")
                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                        cambiar_nombre_peli_por_nombre(nombre, nuevo_nombre)
                    elif entrada==12:
                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                        cambiar_nombre_peli_random(nuevo_nombre)
                    elif entrada==13:
                        while b:
                            try:
                                id_peli = input("Ingresa el id de la película: ")
                                id_peli = int(id_peli)
                                b = False
                                eliminar_pelicula(id_peli)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==14:
                        eliminar_todas_las_peliculas()
                    elif entrada==15:
                        ver_rentas()
                    elif entrada==16:
                        while b:
                            try:
                                id_renta = input("Ingresa el id de la renta: ")
                                id_renta = int(id_renta)
                                b = False
                                encontrar_renta(id_renta)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==17:
                        while b:
                            try:
                                id_renta = input("Ingresa el id de la renta: ")
                                id_renta = int(id_renta)
                                fecha = input("Ingresa la nueva fecha en formato yyyy-mm-dd : ") 
                                #Verificar que la fecha tiene el formato correcto
                                if len(fecha.split('-')) != 3 or not (fecha[0:4].isdigit() and fecha[5:7].isdigit() and fecha[8:10].isdigit()):
                                    print("La fecha ingresada no tiene el formato correcto")
                                else:
                                    b = False
                                    cambiar_fecha_renta(id_renta, fecha)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==18:
                        while b:
                            try:
                                fecha = input("Ingresa la nueva fecha en formato yyyy-mm-dd : ") 
                                if len(fecha.split('-')) != 3 or not (fecha[0:4].isdigit() and fecha[5:7].isdigit() and fecha[8:10].isdigit()):
                                    print("La fecha ingresada no tiene el formato correcto")
                                else:
                                    b = False
                                    cambiar_fecha_random(fecha)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==19:
                        while b:
                            try:
                                id_renta = input("Ingresa el id de la renta: ")
                                id_renta = int(id_renta)
                                b = False
                                eliminar_renta(id_renta)
                            except:
                                print("Debes ingresar un número")
                    elif entrada==20:
                        eliminar_todas_las_rentas() 
            except:
                print("Debes ingresar un número")
                
            
                
        #ver_usuarios()
        #encontrar_usuario(30)
        #cambiar_nombre_usuario_por_id(40, "Alan")
        #cambiar_nombre_usuario_por_nombre("Carlos", "Roberto")
        #cambiar_nombre_usuario_random("Jimin")
        #eliminar_usuario(31)####
        #eliminar_todos_los_usuarios()
        
        ##Pruebas de peliculas
        #ver_peliculas()
        #encontrar_pelicula(17)
        #cambiar_nombre_peli_por_id(16, "El castillo vagabundo")
        #cambiar_nombre_peli_por_nombre("El sorprendente secreto de la paz", "Los amigos")
        #cambiar_nombre_peli_random("La leyenda de 1900")
        #eliminar_pelicula(20)
        #eliminar_todas_las_peliculas()
        
        #Pruebas de rentas
        #ver_rentas() #######
        #encontrar_renta(10)
        #cambiar_fecha_renta(10, "2021-10-10")
        #cambiar_fecha_random('2021-10-10')
        #eliminar_renta(11)
        #eliminar_todas_las_rentas()