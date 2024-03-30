import '../../../CSS/Create.css'
import { rentas } from '../../../../../Data'

export default function CreateRent(){

    const handleSubmit = (e) => {
        e.preventDefault();
        rentas.push({
            idRentar: rentas.length + 1,
            idUsuario: e.target.idUsuario.value,
            idPelicula: e.target.idPelicula.value,
            fecha_renta: new Date(e.target.fechaRenta.value),
            dias_de_renta: e.target.days.value,
            estatus: e.target.status.checked ? 1 : 0
        })
        alert('Rent registered successfully')
    }

    return(
        <div>
            <h1>Create Rent</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="idUsuario">User ID</label>
                <input type="number" id="idUsuario" name="idUsuario" required/>
                <label htmlFor="idPelicula">Movie ID</label>
                <input type="number" id="idPelicula" name="idPelicula" required/>
                <label htmlFor="fechaRenta">Rent Date</label>
                <input type="date" id="fechaRenta" name="fechaRenta" required/>
                <label htmlFor="days">Days of rent</label>
                <input type="number" id="days" name="days" required/>
                <label htmlFor="status">Returned</label>
                <input type="checkbox" id="status" name="status"/>
                <button type="submit">Register Rent</button>
            </form>
        </div>
    )
}