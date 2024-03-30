import '../../../CSS/Update.css'
import { useState } from 'react'
import { deleteMovie } from '../../../../../DataFunctions'
import Card from '../../../../ConfirmationCard/Card.jsx'

export default function DeleteMovie(){
    const [confirm, setConfirm] = useState(false)
    const [movieId, setMovieId] = useState(0)


    const handleSubmit = (e) => {
        e.preventDefault()
        setMovieId(parseInt(e.target.movieId.value))
        setConfirm(true)
    }

    const handleConfirm = () => {
        deleteMovie(movieId)
        setConfirm(false)
    }

    const handleCancel = () => {
        setConfirm(false)
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
                <Card message='Are you sure you want to delete this movie?' handleConfirm={handleConfirm} handleCancel={handleCancel}/>
            }

        </div>
    )
}