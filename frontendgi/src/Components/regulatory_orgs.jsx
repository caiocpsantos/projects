import axios from 'axios'; 
import React,{Component} from 'react'; 

class RegulatoryOrgs extends Component { 
  
	state = { 
    sampleType: "",    
	selectedFile: null
	};
     
    onSampleTypeChange = event => {
  
        this.setState({ sampleType: event.target.value });
    
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
    
    formData.append(
        "sample_type",
        this.state.sampleType
    );
	 
	console.log(this.state.selectedFile); 
	
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.post(`http://127.0.0.1:8000/regulatoryorgs/${this.state.sampleType}`, formData)
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
            <div> 
                <input type="file" onChange={this.onFileChange} /> 
                <button onClick={this.onFileUpload}> 
                    Upload! 
                </button>
                {this.fileData()} 
            </div> 
            <div className='input-space'>
                    <label>Tipo de Amostra:</label>
                    <select value={this.state.sampleType} onChange={this.onSampleTypeChange}>
                        <option value="">Selecione o tipo de amostra</option>
                        <option value="water">Água</option>
                        <option value="industrialsoil">Solo Industrial</option>
                        <option value="residentialsoil">Solo Residencial</option>
                        <option value="agriculturalsoil">Solo Agrícola</option>
                        <option value="residentialsteam">Vapor Residencial</option>
                        <option value="industrialsteam">Vapor Industrial</option>
                    </select>
              </div>
        </div>
        ); 
	} 
} 

export default RegulatoryOrgs; 