import { peliculas } from '../../../../../Data'
import '../../../CSS/Read.css'

export default function ReadMovies(){
    return(
        <div>
            <h1>Movies</h1>
            {peliculas && peliculas.length >0 ? 
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                            <th>Genero</th>
                            <th>Duracion</th>
                            <th>Inventario</th>
                        </tr>
                    </thead>
                    <tbody>
                        {peliculas.map((pelicula) => {
                            return(
                                <tr key={pelicula.idPelicula}>
                                    <td>{pelicula.idPelicula}</td>
                                    <td>{pelicula.nombre}</td>
                                    <td>{pelicula.genero}</td>
                                    <td>{pelicula.duracion}</td>
                                    <td>{pelicula.inventario}</td>
                                    <td>
                                        <button>Editar</button>
                                        <button>Eliminar</button>
                                    </td>
                                </tr>
                            ) }
                        )}
                    </tbody>
                </table> : <h2>No hay peliculas</h2>
            }
        </div>
    )
}