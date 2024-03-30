import { useParams } from "react-router-dom"
import { editRent, isRentRegistered } from "../../../../../DataFunctions"

export default function RentDetail(){
    const params = useParams()

    const id = parseInt(params.rentId)
    const rent = isRentRegistered(id)


    const handleSubmit = (e) => {
        e.preventDefault()
        editRent(id, e.target.status.checked ? 1 : 0)
    }

    return (
        <div>
            <h1>Rent Detail</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="idUsuario">User ID</label>
                <p>{rent.idUsuario}</p>
                <label htmlFor="idPelicula">Movie ID</label>
                <p>{rent.idPelicula}</p>
                <label htmlFor="fechaRenta">Rent Date</label>
                <p>{rent.fecha_renta.toUTCString()}</p>
                <label htmlFor="days">Days of rent</label>
                <p>{rent.dias_de_renta}</p>
                <label htmlFor="status">Returned</label>
                <input type="checkbox" id="status" name="status"  defaultChecked={rent.devuelta === 1}/>
                <button type="submit">Update Rent</button>
            </form>
        </div>
    )
}