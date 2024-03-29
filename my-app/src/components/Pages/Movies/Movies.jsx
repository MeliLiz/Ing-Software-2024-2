import { Link } from "react-router-dom";

export function Movies() {
  return (
    <div>
      <h1>Movies</h1>
      <ul>
        <li>
          <Link to='/movies/create'>Create</Link>
        </li>
        <li>
          <Link to='/movies/read'>Read</Link>
        </li>
        <li>
          <Link to='/movies/update'>Update</Link>
        </li>
        <li>
          <Link to='/movies/delete'>Delete</Link>
        </li>
      </ul>
    </div>
  );
}