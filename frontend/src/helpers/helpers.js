import React, { useEffect, useState} from 'react';
import axios from 'axios'
import App from '../App';

export default function getUsers() {
  
//   const [ users, getUsers] = useState('')  

  const url = 'http://127.0.0.1:8000'

//   useEffect(() =>{
//       getAllUsers()
//   })


//   const getAllUsers = () => {
  axios.get(`${url}/api/users`)
      .then((response) => {
          console.log(response.data)
      })
      
//   }
}
