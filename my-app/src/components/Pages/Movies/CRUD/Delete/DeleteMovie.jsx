import '../../../CSS/Update.css'
import { useNavigate} from "react-router-dom"
import { useState } from 'react'
import './DeleteMovie.css'
import { deleteMovie } from '../../../../../DataFunctions'

export default function DeleteMovie(){
    const navigate = useNavigate()
    const [confirm, setConfirm] = useState(false)
    const [movieId, setMovieId] = useState(0)


    const handleSubmit = (e) => {
        e.preventDefault()
        setMovieId(parseInt(e.target.movieId.value))
        setConfirm(true)
    }

    const handleConfirm = () => {
        console.log(movieId)
        deleteMovie(movieId)
    }

    const handleCancel = () => {
        alert('Delete canceled')
    }

    return(
        <div>
            <h1>Delete Movie</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="movieId">Movie Id</label>
                <input type="number" id="movieId" name="movieId" required/>
                <button type="submit">Delete</button>
            </form>

            {confirm &&
                <div className='confirmation-card'>
                    <p>Are you sure you want to delete this movie?</p>
                    <button onClick={handleConfirm}>Confirm</button>
                    <button onClick={handleCancel}>Cancel</button>
                </div>
            }

        </div>
    )
}