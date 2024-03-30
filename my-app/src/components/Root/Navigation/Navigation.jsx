import './Navigation.css'
import { NavLink } from 'react-router-dom';

export default function Navigation(){
    return(
        <>
        <div id="sidebar">
          <h1><img src='https://images.vexels.com/media/users/3/321274/isolated/preview/711dbd37f96170b5832d201e88b59787-movie-tickets-icon.png'/>ClonBuster</h1>
          <div></div>
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