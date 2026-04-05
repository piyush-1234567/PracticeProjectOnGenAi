import './App.css'

function App() {
  const handleFile = (e) => {
    console.log(e.target.files[0]);
  };
  return (
    <div>
    <input type="text" name="type your queries" placeholder="type your queries..." id=""  />
    <input type="file" onChange={handleFile} />
    </div>
  )

  
}

export default App
