import { NavLink, Outlet } from "react-router-dom"
import '../CSS/Category.css'

export default function Users(){
    return(
        <>
            <h1>Users</h1>
            <div className="card-container">
                <div className="card">
                    <NavLink to='create'>Register a user</NavLink>
                </div>
                <div className="card">
                    <NavLink to='read'>Our users</NavLink>
                </div>
                <div className="card">
                    <NavLink to='update'>Update a user</NavLink>
                </div>
                <div className="card">
                    <NavLink to='delete'>Delete a user</NavLink>
                </div>
            </div>
            <div>
                <Outlet/>
            </div>
        </>
    )
}