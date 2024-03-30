import { NavLink, Outlet } from "react-router-dom";
import '../CSS/Category.css'

export function Movies() {
  return (
    <>
      <h1>Movies</h1>
      <div className="card-container">
        <div className="card">
          <NavLink to='create'>Register a movie</NavLink>
        </div>
        <div className="card">
          <NavLink to='read'>Our movies</NavLink>
        </div>
        <div className="card">
          <NavLink to='update'>Update a movie</NavLink>
        </div>
        <div className="card">
          <NavLink to='delete'>Delete a movie</NavLink>
        </div>

      </div>
      <div>
        <Outlet/>
      </div>
    </>
  );
}