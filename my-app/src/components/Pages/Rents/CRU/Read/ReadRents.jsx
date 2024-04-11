import { rentas } from "../../../../../Data"
import '../../../CSS/Read.css'
import './ReadRent.css'
import { useNavigate } from "react-router-dom"

export default function ReadRents(){

    const navigate = useNavigate()

    const handleEdit = (rentId) => {
        navigate(`/rents/${rentId}`)
    }

    const isTimedOut = (renta) => {
        let rentDate = new Date(renta.fecha_renta)
        let today = new Date()
        let diff = today - rentDate
        let days = Math.floor(diff/(1000*60*60*24))
        return days > renta.dias_de_renta
    }

    return(
        <div>
            <h1>Rents</h1>
            {rentas && rentas.length >0 ? 
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>User</th>
                            <th>Movie</th>
                            <th>Rent Date</th>
                            <th>Days Rented</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rentas.map((renta) => {
                            return(
                                <tr key={renta.idRentar} className={renta.estatus==0 && isTimedOut(renta)?'timedout':''}>
                                    <td>{renta.idRentar}</td>
                                    <td>{renta.idUsuario}</td>
                                    <td>{renta.idPelicula}</td>
                                    <td>{renta.fecha_renta.toUTCString()}</td>
                                    <td>{renta.dias_de_renta}</td>
                                    <td>{renta.estatus==1 ? 'Returned': 'Not returned'}</td>
                                    <td>
                                        <button onClick={()=> handleEdit(renta.idRentar)}>Edit</button>
                                    </td>
                                </tr>
                            ) }
                        )}
                    </tbody>
                </table> : <h2>No hay rentas</h2>
            }
        </div>
    )
}