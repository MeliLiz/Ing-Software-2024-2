import '../../../CSS/Create.css'
import { createUser } from '../../../../../DataFunctions'

export default function CreateUser(){

    const handleSubmit = (e) => {
        e.preventDefault()
        createUser(e.target.name.value, e.target.apPat.value, e.target.apMat.value, e.target.password.value, e.target.email.value, e.target.superUser.checked ? 1 : 0)
    }

    return(
        <div>
            <h1>Register User</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name</label>
                <input type="text" id="name" name="name" required/>
                <label htmlFor="apPat">Last Name</label>
                <input type="text" id="apPat" name="apPat" required/>
                <label htmlFor="apMat">Second Last Name</label>
                <input type="text" id="apMat" name="apMat" required/>
                <label htmlFor="email">Email</label>
                <input type="email" id="email" name="email" required/>
                <label htmlFor="password">Password</label>
                <input type="password" id="password" name="password" required/>
                <label htmlFor="superUser">Super User</label>
                <input type="checkbox" id="superUser" name="superUser"/>
                <button type="submit">Register</button>
            </form>
        </div>
    )
}