import { rentas } from "../../../../../Data"
import '../../../CSS/Read.css'
import { useNavigate } from "react-router-dom"

export default function ReadRents(){

    const navigate = useNavigate()

    const handleEdit = (rentId) => {
        navigate(`/rents/${rentId}`)
    }

    return(
        <div>
            <h1>Rents</h1>
            {rentas && rentas.length >0 ? 
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Usuario</th>
                            <th>Pelicula</th>
                            <th>Fecha de renta</th>
                            <th>Días de renta</th>
                            <th>Estatus</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rentas.map((renta) => {
                            return(
                                <tr key={renta.idRentar}>
                                    <td>{renta.idRentar}</td>
                                    <td>{renta.idUsuario}</td>
                                    <td>{renta.idPelicula}</td>
                                    <td>{renta.fecha_renta.toUTCString()}</td>
                                    <td>{renta.dias_de_renta}</td>
                                    <td>{renta.estatus}</td>
                                    <td>
                                        <button onClick={()=> handleEdit(renta.idRentar)}>Editar</button>
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