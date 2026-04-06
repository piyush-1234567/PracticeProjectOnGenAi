import './App.css'

function App() {
  const handleFile = (e) => {
    console.log(e.target.files[0]);
  };

  const handleSubmit = () => {
    console.log("Submitted");
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