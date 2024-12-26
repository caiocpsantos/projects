import axios from 'axios'; 
import React,{Component} from 'react'; 
import './laboratory.css'

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

class Labs extends Component { 
  
	state = { 
	selectedFile: null,
  reportName: "",
  sampleType: "",
  region: "",
	}; 
	
  submitLogout = event => {
    event.preventDefault();
    client.post(
      "/api/logout",
      {withCredentials: true}
    ).then(() => {
      window.location.assign("/");
    })
  };

	onFileChange = event => { 
	 
	this.setState({ selectedFile: event.target.files[0] }); 
	
	};
  
  onReportNameChange = event => {
  
    this.setState({ reportName: event.target.value });
  
  };

  onSampleTypeChange = event => {
  
    this.setState({ sampleType: event.target.value });

  };
  
  onRegionChange = event => {
  
    this.setState({ region: event.target.value });

  };  
	
	onFileUpload = () => { 
	
	const formData = new FormData(); 
	
	formData.append( 
		"data-file", 
		this.state.selectedFile, 
		this.state.selectedFile.name 
	);
  
  formData.append(
    "report_name", 
    this.state.reportName
  );

  formData.append(
    "sample_type",
    this.state.sampleType
  );
	
  formData.append(
    "region",
    this.state.region
  );

	console.log(this.state.selectedFile);
  console.log(this.state.reportName);
  console.log(this.state.sampleType); 
  console.log(this.state.region); 
	
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.post(`http://127.0.0.1:8000/laboratory/import/${this.state.sampleType}`, formData)
    .then(res => {
        console.log(res);

        // Faz o GET para exportar o CSV (sem enviar o formData)
        return axios.get(`http://127.0.0.1:8000/laboratory/export/${this.state.sampleType}`, {
            params: {
                report_name: this.state.reportName,
                sample_type: this.state.sampleType,
                region: this.state.region
            },
            responseType: 'blob' // Para tratar o download de arquivos
        });
    })
    .then(response => {
        // Processa o retorno do GET (download do arquivo)
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', `${this.state.reportName}_${this.state.sampleType}.xlsx`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    })
    .catch(err => console.log(err));
}; 

	
	fileData = () => { 
	
	if (!this.state.selectedFile) { 
            return ( 
            <div className='no-file'> 
                <h4>Escolha um arquivo antes de enviar</h4> 
            </div> 
            ); 
        } 
	}; 
	

	render() { 
        return ( 
            <div>  
              <nav className='topnav'>
                <a href="/laboratory/">Home</a>
                <a className='logout' href="#" onClick={this.submitLogout} >Log Out</a>

              </nav> 
            <div className='console'>
              <div className='input-space'>
                <label>Nome do Projeto:</label>
                    <input 
                        type="text" 
                        value={this.state.reportName} 
                        onChange={this.onReportNameChange} 
                        placeholder="Digite o nome do projeto" 
                    />
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
              <div className='input-space'>
                    <label>Região:</label>
                    <select value={this.state.region} onChange={this.onRegionChange}>
                        <option value="">Selecione a região</option>
                        <option value="sp">Estado de São Paulo</option>
                        <option value="br">Resto do Brasil</option>
                    </select>
              </div>
              <div className='input-space'>
                <input type="file" onChange={this.onFileChange} />
              </div>    
                <button onClick={this.onFileUpload}> 
                    Enviar
                </button>
 
                {this.fileData()} 
            </div> 
            </div>
        ); 
	} 
} 

export default Labs;   

