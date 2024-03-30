import { useParams } from "react-router-dom"

export default function UserDetail(){
    const params = useParams()

    return (
        <div>
            <h1>User Detail</h1>
            <p>User ID: {params.userId}</p>
        </div>
    )
}