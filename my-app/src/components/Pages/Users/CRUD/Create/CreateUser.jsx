import '../../../CSS/Create.css'
import { usuarios } from '../../../../../Data'

export default function CreateUser(){

    const handleSubmit = (e) => {
        e.preventDefault()
        usuarios.push({
            idUsuario: usuarios.length + 1,
            nombre: e.target.name.value,
            apPat: e.target.apPat.value,
            apMat: e.target.apMat.value,
            password: e.target.password.value,
            email: e.target.email.value,
            profilePicture: null,
            superUser: e.target.superUser.checked ? 1 : 0
        })
        alert('User registered successfully')
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