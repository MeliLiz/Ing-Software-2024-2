import '../../../CSS/Update.css'
import { useNavigate } from "react-router-dom"
import { isRentRegistered } from "../../../../../DataFunctions"

export default function UpdateRent(){
    const navigate = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        const rentId = parseInt(e.target.rentId.value)
        if(isRentRegistered(rentId)){
            navigate(`/movies/${rentId}`)
        }else{
            alert('Movie not found')
        }
    }

    return(
        <div>
            <h1>Update Rent</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="rentId">Rent Id</label>
                <input type="number" id="rentId" name="rentId" required/>
                <button type="submit">Search</button>
            </form>
        </div>
    )
}