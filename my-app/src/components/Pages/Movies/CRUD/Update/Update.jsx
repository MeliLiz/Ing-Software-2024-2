import '../../../CSS/Update.css'
import { useNavigate } from "react-router-dom"
import { isMovieRegistered } from "../../../../../DataFunctions"

export default function UpdateMovie(){

    const navigate = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        const movieId = parseInt(e.target.movieId.value)
        if(isMovieRegistered(movieId)){
            navigate(`/movies/${movieId}`)
            /*localStorage.setItem('movie', JSON.stringify(movie))
            window.location.href = '/movies/update/movieDetail'*/
        }else{
            alert('Movie not found')
        }
    }

    return(
        <div>
            <h1>Update Movie</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="movieId">Movie Id</label>
                <input type="number" id="movieId" name="movieId" required/>
                <button type="submit">Search</button>
            </form>
        </div>
    )
}