import { usuarios } from "../../../../../Data"
import '../../../CSS/Read.css'
import { useNavigate } from "react-router-dom"
import { deleteUser } from "../../../../../DataFunctions"
import { useState } from "react"
import Card from "../../../../ConfirmationCard/Card"

export default function ReadUsers(){

    const navigate = useNavigate()

    const [confirm, setConfirm] = useState(false)
    const [userId, setUserId] = useState(0)

    const handleEdit = (userId) => {
        navigate(`/users/${userId}`)
    }

    const handleDelete = (userId) => {
        setUserId(userId)
        setConfirm(true)
    }

    const handleConfirm = () => {
        deleteUser(userId)
        setConfirm(false)
    }

    const handleCancel = () => {
        setConfirm(false)
        alert('Delete canceled')
    }

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
                                        <button onClick={() => handleEdit(usuario.idUsuario)}>Edit</button>
                                        <button onClick={() => handleDelete(usuario.idUsuario)}>Delete</button>
                                    </td>
                                </tr>
                            ) }
                        )}
                    </tbody>
                </table> : <h2>No hay usuarios</h2>
            }
            {confirm && <Card message='Are you sure you want to delete this user?' handleConfirm={handleConfirm} handleCancel={handleCancel}/>}
        </div>
    )
        
}