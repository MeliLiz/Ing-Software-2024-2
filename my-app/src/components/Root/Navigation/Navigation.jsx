import './Navigation.css'
import { NavLink } from 'react-router-dom';

export default function Navigation(){
    return(
        <>
        <div id="sidebar">
          <h1>ClonBuster</h1>
          <div>
            <form id="search-form" role="search">
              <input
                id="q"
                aria-label="Search contacts"
                placeholder="Search"
                type="search"
                name="q"
              />
              <div
                id="search-spinner"
                aria-hidden
                hidden={true}
              />
              <div
                className="sr-only"
                aria-live="polite"
              ></div>
            </form>
            <form method="post">
              <button type="submit">New</button>
            </form>
          </div>
          <nav>
            <ul>
              <li>
                <NavLink to='/'>Home</NavLink>
              </li>
              <li>
                <NavLink to='movies'>Movies</NavLink>
              </li>
              <li>
                <NavLink to='users'>Users</NavLink>
              </li>
              <li>
                <NavLink to='rents'>Rents</NavLink>
              </li>
            </ul>
          </nav>
        </div>
      </>
    )
}