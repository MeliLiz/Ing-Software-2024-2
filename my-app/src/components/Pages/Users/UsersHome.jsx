import '../CSS/HomeComponents.css'

export default function HomeUsers(){
    return(
        <>
        <h1> Welcome to the Users Page </h1> 

        <div className="home">
            <p> Here you can manage your user inventory. Add new users, see them, edit them, or delete them. </p>
            <img src="http://www.clker.com/cliparts/F/5/r/V/G/b/single-user-yellow-md.png" alt="user" className='userImage'/>
        </div>
        </>
    )
}