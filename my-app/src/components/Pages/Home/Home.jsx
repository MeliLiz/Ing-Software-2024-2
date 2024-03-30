import './Home.css';

export function Home() {
  return (
    <div className='cont'>
      <h1 className='title'>Welcome to ClonBuster</h1>
      <p>The best way to manage your video-store!</p>
      <img src='https://images.vexels.com/media/users/3/321274/isolated/preview/711dbd37f96170b5832d201e88b59787-movie-tickets-icon.png'/>
      <div className='container'>
        <p>Start managing your video store right now. Register new clients, add movies to your inventory and keep track of rentals made.</p>
      </div>
      <footer>
      <p>Do you need help? Contact us at support@clonbuster.com.</p>
      </footer>
    </div>
  );
}