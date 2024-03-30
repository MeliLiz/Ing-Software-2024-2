import { useParams } from "react-router-dom"

export default function RentDetail(){
    const params = useParams()

    return (
        <div>
            <h1>Rent Detail</h1>
            <p>Rent ID: {params.rentId}</p>
        </div>
    )
}