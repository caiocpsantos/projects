import Login from './Components/login'
import Home from './Components/home'
import Lab from './Components/laboratory'
import RegulatoryOrgs from './Components/regulatory_orgs'
import { BrowserRouter, Routes, Route} from 'react-router-dom'
import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import LabToAgency from './Components/translator'



axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

function App() {
  
  const [currentUser, setCurrentUser] = useState();
  
  
  useEffect(() => {
    client.get("/api/user")
    .then(function(res) {
      setCurrentUser(true);
    })
    .catch(function(error) {
      setCurrentUser(false);
    });
  }, []);

  if (currentUser) {
    return (
    
      <div className="content">
          <BrowserRouter>
            <Routes>
              <Route Component={ Lab } path="/" exact />
              <Route Component={ Lab } path="login/" exact />
              <Route Component={ Lab } path="laboratory/" exact />
              <Route Component={ RegulatoryOrgs } path="regulatoryorgupload/" exact />
              <Route Component={ LabToAgency } path="labtoagencyupload/" exact />
            </Routes>
          </BrowserRouter>

      </div>
    );
  };
  return (
    
    <div className="content">
        <BrowserRouter>
          <Routes>
            <Route Component={ Login } path="/" exact />
            <Route Component={ Login } path="login/" exact />
            
          </Routes>
        </BrowserRouter>

    </div>
  );
}
export default App;
