import '../../../CSS/Update.css'
import { useNavigate } from "react-router-dom"
import { isUserRegistered } from "../../../../../DataFunctions"


export default function UpdateUser(){

    const navigate = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        const userId = parseInt(e.target.userId.value)
        if(isUserRegistered(userId)){
            navigate(`/users/${userId}`)
        }else{
            alert('User not found')
        }
    }

    return(
        <div>
            <h1>Update User</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="userId">User Id</label>
                <input type="number" id="userId" name="userId" required/>
                <button type="submit">Search</button>
            </form>
        </div>
    )
}