import './App.css';
import Root from '../components/Root/Root.jsx'
import { Home } from '../components/Pages/Home/Home.jsx';
import { Movies } from '../components/Pages/Movies/Movies.jsx';
import  Users from '../components/Pages/Users/Users.jsx';
import  Rents  from '../components/Pages/Rents/Rents.jsx';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import CreateMovie from '../components/Pages/Movies/CRUD/Create/CreateMovie.jsx';
import ReadMovies from '../components/Pages/Movies/CRUD/Read/ReadMovies.jsx';
import UpdateMovies from '../components/Pages/Movies/CRUD/Update/Update.jsx';
import DeleteMovies from '../components/Pages/Movies/CRUD/Delete/DeleteMovie.jsx';
import CreateUser from '../components/Pages/Users/CRUD/Create/CreateUser.jsx';
import ReadUsers from '../components/Pages/Users/CRUD/Read/ReadUsers.jsx';
import UpdateUsers from '../components/Pages/Users/CRUD/Update/UpdateUser.jsx';
import DeleteUsers from '../components/Pages/Users/CRUD/Delete/DeleteUser.jsx';
import CreateRent from '../components/Pages/Rents/CRU/Create/CreateRent.jsx';
import ReadRents from '../components/Pages/Rents/CRU/Read/ReadRents.jsx';
import UpdateRents from '../components/Pages/Rents/CRU/Update/UpdateRent.jsx';
import Error from '../components/Error.jsx';
import Default from '../components/Pages/Movies/Default.jsx';





const router = createBrowserRouter(
  [
    { 
      path: '/', 
      element: <Root />, 
      errorElement: <Error/>,
      children: [
        {path: '/', element: <Home/>},
        {path: 'movies', 
        element: <Movies />,
        children: [
          {path: 'create', element: <CreateMovie/>},
          {path: 'read', element: <ReadMovies/>},
          {path: 'update', element: <UpdateMovies/>},
          {path:'delete', element: <DeleteMovies/>}

        ]
       },
        {path: 'users', 
        element: <Users />,
        children: [
          {path: 'create', element: <CreateUser/>},
          {path: 'read', element: <ReadUsers/>},
          {path: 'update', element: <UpdateUsers/>},
          {path: 'delete', element: <DeleteUsers/>},
        ]
      },
        {path: 'rents', 
        element: <Rents />,
        children: [
          {path: "create", element: <CreateRent/>},
          {path: "read", element: <ReadRents/>},
          {path: "update", element: <UpdateRents/>}
        ]
      },
        
        
        
      ]
    },
    
    
  ]
)

export default function App() {

  return <RouterProvider router={router}/>
}
