import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import axios from 'axios';


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});


const Home = () => {
 

    function submitLogout(e) {
        e.preventDefault();
        client.post(
          "/api/logout",
          {withCredentials: true}
        ).then(function() {
            window.location.reload();  
        });
      }
    
    return (
        <div>
          <Navbar bg="dark" variant="dark">
            <Container>
              <Navbar.Brand>Authentication App</Navbar.Brand>
              <Navbar.Toggle />
              <Navbar.Collapse className="justify-content-end">
                <Navbar.Text>
                  <form onSubmit={e => submitLogout(e)}>
                    <Button type="submit" variant="light">Log out</Button>
                  </form>
                </Navbar.Text>
              </Navbar.Collapse>
            </Container>
          </Navbar>
            <div className="center">
              <div >
                <a href="http://127.0.0.1:8000/laboratory" >
                  <button> Laboratório </button>
                </a>
              </div>
            </div>
          </div>
      );
    }

    export default Home;    

