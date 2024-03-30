import '../../../CSS/Create.css'
import { peliculas } from '../../../../../Data'

export default function CreateMovie(){

    const handleSubmit = (e) => {
        e.preventDefault()
        peliculas.push({
            idPelicula: peliculas.length + 1,
            nombre: e.target.title.value,
            genero: e.target.genre.value,
            duracion: e.target.length.value,
            inventario: e.target.stock.value
        })
        alert('Movie registered successfully')
    }

    return(
        <div>
            <h1>Register a movie</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="title">Title</label>
                <input type="text" id="title" name="title" required/>
                <label htmlFor="genre">Genre</label>
                <input type="text" id="genre" name="genre" required/>
                <label htmlFor="length">Length (minutes)</label>
                <input type="number" id="length" name="length" required/>
                <label htmlFor="stock">Stock</label>
                <input type='number' id="stock" name="stock" required/>
                <button type="submit">Register</button>
            </form>
        </div>
    )
}