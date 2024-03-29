import { usuarios } from "../../../../../Data"
import '../../../CSS/Read.css'

export default function ReadUsers(){
    return(
        <div>
            <h1>Users</h1>
            {usuarios && usuarios.length >0 ? 
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                            <th>Apellido paterno</th>
                            <th>Apellido materno</th>
                            <th>Email</th>
                            <th>Superuser</th>
                        </tr>
                    </thead>
                    <tbody>
                        {usuarios.map((usuario) => {
                            return(
                                <tr key={usuario.idUsuario}>
                                    <td>{usuario.idUsuario}</td>
                                    <td>{usuario.nombre}</td>
                                    <td>{usuario.apPat}</td>
                                    <td>{usuario.apMat}</td>
                                    <td>{usuario.email}</td>
                                    <td>{usuario.superUser}</td>
                                    <td>
                                        <button>Editar</button>
                                        <button>Eliminar</button>
                                    </td>
                                </tr>
                            ) }
                        )}
                    </tbody>
                </table> : <h2>No hay usuarios</h2>
            }
        </div>
    )
        
}