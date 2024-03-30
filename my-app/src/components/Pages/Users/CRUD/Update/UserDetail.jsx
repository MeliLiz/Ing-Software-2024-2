import { useParams } from "react-router-dom"
import { isUserRegistered, editUser } from "../../../../../DataFunctions"

export default function UserDetail(){
    const params = useParams()

    const id = parseInt(params.userId)
    const user = isUserRegistered(id)

    console.log(user)

    const handleSubmit = (e) => {
        e.preventDefault()
        editUser(id,e.target.name.value, e.target.apPat.value, e.target.apMat.value, e.target.password.value, e.target.email.value, e.target.superUser.checked ? 1 : 0)

    }

    return (
        <div>
            <h1>User Detail</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name</label>
                <input type="text" id="name" name="name" defaultValue={user.nombre} required/>
                <label htmlFor="apPat">Last Name</label>
                <input type="text" id="apPat" name="apPat" defaultValue={user.apPat} required/>
                <label htmlFor="apMat">Second Last Name</label>
                <input type="text" id="apMat" name="apMat" defaultValue={user.apMat} required/><br />
                <label htmlFor="email">Email</label>
                <input type="email" id="email" name="email" defaultValue={user.email} required/>
                <label htmlFor="password">Password</label>
                <input type="password" id="password" name="password" defaultValue={user.password} required/>
                <label htmlFor="superUser">Super User</label>
                <input type="checkbox" id="superUser" name="superUser"/>
                <button type="submit">Edit</button>
            </form>
        </div>
    )
}