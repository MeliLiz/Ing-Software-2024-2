import { peliculas } from '../../../../../Data'
import '../../../CSS/Read.css'
import { useNavigate } from 'react-router-dom'

export default function ReadMovies(){

    const navigate = useNavigate()

    const handleEdit = (movieId) => {
        navigate(`/movies/${movieId}`)
    }

    const handleDelete = () => {}

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
                                        <button onClick={() => handleEdit(pelicula.idPelicula)}>Editar</button>
                                        <button onClick={() => handleDelete(pelicula.idPelicula)}>Eliminar</button>
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