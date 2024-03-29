import {Link} from 'react-router-dom';
import './Home.css';

export function Home() {
  return (
    <div>
      <h1 className='title'>Welcome to ClonBuster</h1>
      <Link to='/movies'>Movies</Link>
    </div>
  );
}