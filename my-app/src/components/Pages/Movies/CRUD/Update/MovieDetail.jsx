import { useParams } from "react-router-dom"
import { isMovieRegistered, editMovie } from "../../../../../DataFunctions"

export default function MovieDetail() {

    const params = useParams()
    const id = parseInt(params.movieId)

    const movie = isMovieRegistered(id)

    const handleSubmit = (e) => {
        e.preventDefault()
        editMovie(id, e.target.title.value, e.target.genre.value, e.target.length.value, e.target.stock.value)
    }

    return (
        <div>
            <h1>Movie Detail</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="title">Title</label>
                <input type="text" id="title" name="title" required defaultValue={movie.nombre}/>
                <label htmlFor="genre">Genre</label>
                <input type="text" id="genre" name="genre" required defaultValue={movie.genero}/>
                <label htmlFor="length">Length (minutes)</label>
                <input type="number" id="length" name="length" required defaultValue={movie.duracion}/>
                <label htmlFor="stock">Stock</label>
                <input type='number' id="stock" name="stock" required defaultValue={movie.inventario}/>
                <button type="submit">Update</button>
            </form>
        </div>
    )
}