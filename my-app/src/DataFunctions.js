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

export function editUser(idUser, name, apPat, apMat, password, email, superUser){
    const user = isUserRegistered(idUser)
    if(user){
        const index = usuarios.indexOf(user)
        const newUser = {
            idUsuario: idUser,
            nombre: name,
            apPat: apPat,
            apMat: apMat,
            password: password,
            email: email,
            profilePicture: null,
            superUser: superUser
        }
        usuarios[index] = newUser
        alert('User updated successfully')
    }else{
        alert('The user does not exist')
    }
}

export function editMovie(movieId,title, genre, length, stock){
    const movie = isMovieRegistered(movieId)
    if (movie){
        const index = peliculas.indexOf(movie)
        const newMovie = {
            idPelicula: movieId,
            nombre: title,
            genero: genre,
            duracion: length,
            inventario: stock
        }
        peliculas[index] = newMovie
        alert('Movie updated successfully')
    }else{
        alert('The movie does not exist')
    }
}

export function editRent(rentId, status){
    console.log(rentId)
    console.log(status)
    const rent = isRentRegistered(rentId)
    console.log(rent)
    if(rent){
        const index = rentas.indexOf(rent)
        rentas[index].estatus= status
        alert('Rent updated successfully')
    }else{
        alert('The rent does not exist')
    }
}

export function deleteMovie(movieId){
    const movie = isMovieRegistered(movieId)
    if(movie){
        const index = peliculas.indexOf(movie)
        peliculas.splice(index, 1)
        alert('Movie deleted successfully')
    }else{
        alert('The movie does not exist')
    }
}