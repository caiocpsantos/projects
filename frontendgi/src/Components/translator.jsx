import axios from 'axios'; 
import React,{Component} from 'react'; 

class LabToAgency extends Component { 
  
	state = { 
	selectedFile: null
	}; 
	
	onFileChange = event => { 
	 
	this.setState({ selectedFile: event.target.files[0] }); 
	
	}; 
	
	onFileUpload = () => { 
	
	const formData = new FormData(); 
	
	formData.append( 
		"data-file", 
		this.state.selectedFile, 
		this.state.selectedFile.name 
	); 
	 
	console.log(this.state.selectedFile); 
	
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.post("http://127.0.0.1:8000/regulatoryorgs/translatorwater", formData)
    .then(res => console.log(res)) 
    .catch(err => console.log(err))
	}; 
	
	fileData = () => { 
	
	if (!this.state.selectedFile) { 
            return ( 
            <div> 
                <br /> 
                <h4>Choose before Pressing the Upload button</h4> 
            </div> 
            ); 
        } 
	}; 
	
	render() { 
        return ( 
            <div> 
                <input type="file" onChange={this.onFileChange} /> 
                <button onClick={this.onFileUpload}> 
                    Upload! 
                </button>
                {this.fileData()} 
            </div> 
        ); 
	} 
} 

export default LabToAgency;