import { Link } from "react-router-dom"

export default function Rents(){
    return(
        <div>
            <h1>Rents</h1>
            <ul>
                <li>
                    <Link to='/rents/create'>Create</Link>
                </li>
                <li>
                    <Link to='/rents/read'>Read</Link>
                </li>
                <li>
                    <Link to='/rents/update'>Update</Link>
                </li>
            </ul>
        </div>
    )
}