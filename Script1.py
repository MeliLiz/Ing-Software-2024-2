import pymysql.cursors
import random
import datetime

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             db='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



############# Auxiliares ################

nombres = ["Fernando", "Valeria", "Luis", "Ricardo", "Sofia", "Luisa", "Monserrat", "Dalia", "Carolina","Cesar", "Melissa", "Lizbeth", "Gael", "Alejandro", "Ethan", "Rodrigo", "Mario", "Jorge", "Felix"]
apellidos = ["Ramirez", "Baeza", "Garcia", "Hernandez", "Lopez", "Perez", "Gonzalez", "Rodriguez", "Sanchez", "Torres", "Gomez", "Diaz", "Reyes", "Jimenez", "Vazquez", "Fernandez", "Blancas", "Aguirre", "Morales", "Salmeron", "Nava", "Cruz", "Carrillo"]
calificadores = ["El increíble", "El asombroso", "El maravilloso", "El fabuloso", "El fantástico", "El grandioso", "El magnífico", "El espectacular", "El sorprendente", "El extraordinario", "El genial", "El prodigioso", "El sensacional", "El estupendo", "El magnífico", "El portentoso", "El terrorífico", "El gran", "El espeluznante", "El oscuo"]
sustantivos = ["castillo", "dragón", "caballero", "reino","hechizo", "tesoro", "mago", "monstruo", "fantasma", "demonio", "hada", "elfo", "enano", "gigante", "vampiro", "secreto"]
lugares = ["del reino", "de la oscuridad", "de la luz", "de la magia", "de la fantasía", "de la realidad", "de la imaginación", "de la locura", "de la eternidad", "de la inmortalidad", "de la juventud", "de la verdad", "de la mentira", "de la justicia", "de la injusticia", "de la riqueza","de la alegría", "de la esperanza", "de la desconfianza", "de la confianza", "de la traición", "de la lealtad", "de la amistad", "del amor", "del odio", "de la pasión", "de la crueldad", "de la bondad", "de la maldad", "de la belleza", "de la fealdad", "de la perfección", "de la imperfección", "de la armonía", "del caos", "de la paz", "de la guerra", "de la victoria", "de la derrota", "de la fama", "de la fortuna", "de la desgracia", "de la suerte", "de la mala suerte", "de la eternidad", "de la inmortalidad"]

def genera_nombre():
    return random.choice(nombres)

def genera_apellido():
    return random.choice(apellidos)
    
def genera_email(nombre, apellido):
    correos = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com", "@live.com"]
    return nombre+ apellido +genera_password(3)+random.choice(correos)

def genera_password(num):
    password = ""
    for i in range(num):
        password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return password

def genera_titulo():
    return random.choice(calificadores) + " " + random.choice(sustantivos) + " " + random.choice(lugares)

def genero():
    return random.choice(["Accion", "Aventura", "Comedia", "Drama", "Fantasia", "Misterio", "Romance", "Terror"])
   
def duracion():
    return random.randint(60, 180) #En minutos

def fecha_renta():
    inicio = datetime.date(2019, 1, 1)
    fin = datetime.date(2024, 2, 18)
    dias = (fin - inicio).days
    return inicio + datetime.timedelta(days=random.randint(0, dias))
    
    
def fecha_devolucion(fecha_renta, dias):
    return fecha_renta + datetime.timedelta(days= dias)

def obtener_estatus(dias,fecha_renta):
    if datetime.date.today() > fecha_devolucion(fecha_renta, dias):
        return '0' #Devuelto
    else:
        return '1' #En renta
    
    
#########################################
   

#Una funcion que inserte al menos 1 registro en cada tabla cada vez que sea ejecutada, como se tiene una
#tabla con llaves foraneas, se tiene que tener en cuenta que existan los registros en las otras dos tablas.
def insertar_registro():
    with connection.cursor() as cursor:
        # Insertar en users
        sql = "INSERT INTO `usuarios` (`nombre`, `apPat`,  `apMat`, `password`, `email`, `superuser`) VALUES (%s, %s, %s, %s, %s, %s)"
        nombre = genera_nombre()
        apellido1 = genera_apellido()
        email = genera_email(nombre, apellido1)
        cursor.execute(sql, (nombre, apellido1, genera_apellido(), genera_password(8), email, random.randint(0, 1)))
        id_usuario = cursor.lastrowid #Obtener el ultimo ID de la tabla users para relacionarlo a sus demás
        
        # Insertar en peliculas
        sql1 = "INSERT INTO `peliculas` (`nombre`, `genero`,  `duracion`, `inventario`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql1, (genera_titulo(), genero(), duracion(), random.randint(1, 100)))
        id_pelicula = cursor.lastrowid #Obtener el ultimo ID de la tabla peliculas para relacionarlo a sus demás
        
        # Insertar en rentas
        sql2 = "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
        fecha= fecha_renta()
        cursor.execute(sql2, (id_usuario, id_pelicula, fecha, 15, obtener_estatus(15, fecha)))
        
    connection.commit()
    

#Una funcion que filtre a la tabla Usuario a todos los usuarios cuyo apellido termine en alguna cadena especificada por el usuario.

def filtrar(str):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `usuarios` WHERE `apPat` LIKE %s OR `apMat` LIKE %s"
        cursor.execute(sql, (f"%{str}", f"%{str}"))
        result = cursor.fetchall()
        print(result)
        return result
    
#Una funcion que dado el nombre de una pelıcula (entrada de funcion o entrada de usuario) y un genero, si dicha pelıcula existe, se le cambie el genero a dicha pelıcula.

def cambiar_genero(nombre, genero):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "UPDATE `peliculas` SET `genero`=%s WHERE `nombre`=%s"
        cursor.execute(sql, (genero, nombre))
        
        if cursor.rowcount == 0:
            print("No se encontró la pelicula")
        else:
            print("Se actualizó el genero de la pelicula")
        
    connection.commit()
    
#Una funcion que elimine todas las rentas anteriores a 3 dıas a la fecha en que se ejecuta la funcion, ejemplo,
#si la ejecuto el 23 de Enero de 2024, todas las rentas que tengan fecha anterior o igual al 19 de Enero de
#2024 deberan de ser eliminadas, hasta que dicha funcion se ejecute. 

def eliminar_rentas():
    with connection.cursor() as cursor:
        # Read a single record
        sql = "DELETE FROM `rentar` WHERE `fecha_renta` < %s"
        cursor.execute(sql, (datetime.date.today() - datetime.timedelta(days=3)))
        
    connection.commit()


############# CRUD ################

def insertar_renta():
    with connection.cursor() as cursor:
        # Insertar en rentas
        sql = "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
        fecha= fecha_renta()
        cursor.execute(sql, (30, 20, '2024-02-13', 15, obtener_estatus(15, fecha)))
        
    connection.commit()
    
        
if __name__== "__main__":
    insertar_registro()
    #filtrar("a")
    #cambiar_genero("El gran caballero de la derrota", "Aventura")
    #eliminar_rentas()
    #insertar_renta()
    connection.close()
    print("Conexión cerrada")