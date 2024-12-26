import './login.css' ;
import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import Logo from '../../public/logo_geo.png';



axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

const Login = () => {
    const [currentUser, setCurrentUser] = useState();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
  
    useEffect(() => {
      client.get("/api/user")
      .then(function(res) {
        setCurrentUser(true);
      })
      .catch(function(error) {
        setCurrentUser(false);
      });
    }, []);
  

  
    function submitLogin(e) {
      e.preventDefault();
      client.post(
        "/api/login",
        {
          email: email,
          password: password
        }
      ).then(function(res) {
        setCurrentUser(true);
      }).then(function() {
        window.location.reload();
        });
 
    }
  
  
    return (
      
        <div className="center">
            <form onSubmit={e => submitLogin(e)}>
              <img src={Logo} alt="login" />
              <div className='input-space'>
              <label for='email'>Seu email:</label>
              <input type='email' id='email'placeholder='email' value={email} onChange={e => setEmail(e.target.value)} />
              </div>
              <div className='input-space'>
              <label for='password'>Senha:</label>
              <input type='password' id='password' placeholder='senha' value={password} onChange={e => setPassword(e.target.value)}/>
              </div>
              <button>Entrar</button>
            </form> 
        </div>
  
    );
  }
  

export default Login;