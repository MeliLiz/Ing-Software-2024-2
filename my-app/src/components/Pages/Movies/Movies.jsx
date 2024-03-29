import { Link, Outlet } from "react-router-dom";
import '../CSS/Category.css'

export function Movies() {
  return (
    <>
      <h1>Movies</h1>
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
        <div className="card">
          <Link to='delete'>Delete</Link>
        </div>

      </div>
      <div>
        <Outlet/>
      </div>
    </>
  );
}