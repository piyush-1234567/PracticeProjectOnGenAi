import './App.css'
import {useState} from 'react';
function App() {
  const [file,setFile]  = useState(null);
  const handleFile = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    console.log("Submitted ",selected);
  };

  const handleSubmit = () => {
    console.log("Submitted ",file);
  };

  return (
    <div className="container">
      <h2>Upload Your File</h2>

      <input 
        type="text" 
        placeholder="Type your queries..." 
        className="input"
      />

      <input 
        type="file" 
        onChange={handleFile} 
        className="fileInput"
      />

      <button onClick={handleSubmit} className="btn">
        Submit
      </button>
    </div>
  );
}

export default App;