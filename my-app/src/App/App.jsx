import './App.css';
import Root from '../components/Root/Root.jsx'
import { Home } from '../components/Pages/Home/Home.jsx';
import { Movies } from '../components/Pages/Movies/Movies.jsx';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';


const router = createBrowserRouter(
  [
    { 
      path: '/', 
      element: <Root />, 
      children: [
        {path: '/', element: <Home/>},
        {path: 'movies', element: <Movies /> }
      ]
    },
    
  ]
)

export default function App() {

  return <RouterProvider router={router}/>
}
