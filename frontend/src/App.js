import React, {useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';



function App(props) {

  const [ users, getUsers] = useState('')  

  const url = 'http://127.0.0.1:8000'

  useEffect(() =>{
      getAllUsers()
  })


  const getAllUsers = () => {
  axios.get(`${url}/api/users`)
      .then((response) => {
          console.log(response.data)
          const allUsers = response.data
          getUsers(allUsers)
      })
      .catch(error => console.error(`Error: ${error}`)) 
  }


  return (
    <div className="App">
      <h1>Hello World</h1>
    </div>
  );
}

export default App;
