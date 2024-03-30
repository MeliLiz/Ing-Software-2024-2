import '../../../CSS/Update.css'
import { useState } from 'react'
import { deleteUser } from '../../../../../DataFunctions'
import Card from '../../../../ConfirmationCard/Card.jsx'

export default function DeleteUser(){

    const [confirm, setConfirm] = useState(false)
    const [userID, setUserID] = useState(0)


    const handleSubmit = (e) => {
        e.preventDefault()
        setUserID(parseInt(e.target.userId.value))
        setConfirm(true)
    }

    const handleConfirm = () => {
        deleteUser(userID)
        setConfirm(false)
    }

    const handleCancel = () => {
        setConfirm(false)
        alert('Delete canceled')
    }

    return(
        <div>
            <h1>Delete User</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="userId">User Id</label>
                <input type="number" id="userId" name="userId" required/>
                <button type="submit">Delete</button>
            </form>
            {confirm && <Card message='Are you sure you want to delete this user?' handleConfirm={handleConfirm} handleCancel={handleCancel}/>}
        </div>
    )
}