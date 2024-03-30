import { useParams } from "react-router-dom"

export default function MovieDetail() {

    const params = useParams()

    return (
        <div>
            <h1>Movie Detail</h1>
            <p>Movie ID: {params.movieId}</p>
        </div>
    )
}