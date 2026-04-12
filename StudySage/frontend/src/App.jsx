import './App.css'
import {useState} from 'react';
function App() {
  const [file,setFile]  = useState(null);
  const handleFile = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    console.log("Submitted ",selected);
  };

  const handleSubmit = async () => {
    if(!file){
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file",file);
    try{
      const response = await fetch("http://127.0.0.1:8000/upload",{
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      console.log("Response: ",data);

      alert("File uploaded successfully");
    }catch(error){
      console.error("Error uploading file: ",error);
      alert("Upload failed");
    }
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