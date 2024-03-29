import { Link, Outlet } from "react-router-dom"
import '../CSS/Category.css'

export default function Rents(){
    return(
        <>
            <h1>Rents</h1>
            <div className="card-container">
                <div className="card">
                    <Link to='create'>Create</Link>
                </div>
                <div className="card">
                    <Link to='read'>Read</Link>
                </div>
                <div className="card">
                    <Link to='update'>Update</Link>
                </div>
            </div>
            <div>
                <Outlet/>
            </div>
        </>
    )
}