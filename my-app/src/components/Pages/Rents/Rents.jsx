import { NavLink, Outlet } from "react-router-dom"
import '../CSS/Category.css'

export default function Rents(){
    return(
        <>
            <h1>Rents</h1>
            <div className="card-container">
                <div className="card">
                    <NavLink to='create'>Register a rent</NavLink>
                </div>
                <div className="card">
                    <NavLink to='read'>Our rents</NavLink>
                </div>
                <div className="card">
                    <NavLink to='update'>Update a rent</NavLink>
                </div>
            </div>
            <div>
                <Outlet/>
            </div>
        </>
    )
}