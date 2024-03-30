import {peliculas, usuarios, rentas} from './Data.js'

export function createMovie(title, genre, length, stock){
    peliculas.push({
        idPelicula: peliculas.length + 1,
        nombre: title,
        genero: genre,
        duracion: length,
        inventario: stock
    })
    alert('Movie registered successfully')
}

export function createUser(name, apPat, apMat, password, email, superUser){
    usuarios.push({
        idUsuario: usuarios.length + 1,
        nombre: name,
        apPat: apPat,
        apMat: apMat,
        password: password,
        email: email,
        profilePicture: null,
        superUser: superUser
    })
    alert('User registered successfully')
}

export function createRent(idUsuario, idPelicula, fechaRenta, days, status){
    rentas.push({
        idRentar: rentas.length + 1,
        idUsuario: idUsuario,
        idPelicula: idPelicula,
        fecha_renta: new Date(fechaRenta),
        dias_de_renta: days,
        estatus: status
    })
    alert('Rent registered successfully')
}

export function isMovieRegistered(idMovie){
    return peliculas.find(movie => movie.idPelicula === idMovie)
}

export function isUserRegistered(idUser){
    return usuarios.find(user => user.idUsuario === idUser)
}

export function isRentRegistered(idRent){
    return rentas.find(rent => rent.idRentar === idRent)
}