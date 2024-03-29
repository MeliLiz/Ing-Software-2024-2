import { Link } from "react-router-dom"

export default function Users(){
    return(
        <div>
            <h1>Users</h1>
            <ul>
                <li>
                    <Link to='/users/create'>Create</Link>
                </li>
                <li>
                    <Link to='/users/read'>Read</Link>
                </li>
                <li>
                    <Link to='/users/update'>Update</Link>
                </li>
                <li>
                    <Link to='/users/delete'>Delete</Link>
                </li>
            </ul>
        </div>
    )
}