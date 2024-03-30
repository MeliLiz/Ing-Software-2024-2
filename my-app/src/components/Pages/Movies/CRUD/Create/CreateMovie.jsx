import '../../../CSS/Create.css'
import { createMovie } from '../../../../../DataFunctions'
export default function CreateMovie(){

    const handleSubmit = (e) => {
        e.preventDefault()
        createMovie(e.target.title.value, e.target.genre.value, e.target.length.value, e.target.stock.value)
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