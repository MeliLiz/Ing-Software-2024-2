import '../../../CSS/Create.css'
import { createRent } from '../../../../../DataFunctions';

export default function CreateRent(){

    const handleSubmit = (e) => {
        e.preventDefault();
        createRent(e.target.idUsuario.value, e.target.idPelicula.value, e.target.fechaRenta.value, e.target.days.value, e.target.status.checked ? 1 : 0)
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