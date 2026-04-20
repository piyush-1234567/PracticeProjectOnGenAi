import './App.css'
import { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  const handleFile = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    console.log("Submitted ", selected);
  };

  const handleSubmit = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log("Response: ", data);

      alert("File uploaded successfully");
    } catch (error) {
      console.error("Error uploading file: ", error);
      alert("Upload failed");
    }
  };

  const handleAsk = async () => {
    if (!query) {
      alert("Enter a question");
      return;
    }

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/ask?query=${encodeURIComponent(query)}`
      );

      const data = await response.json();
      console.log(data);

      if (data.answer) {
        setAnswer(data.answer);
      } else {
        setAnswer("No answer received");
      }
    } catch (error) {
      console.error("Ask error:", error);
      setAnswer("Error fetching answer");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">📚 Study Sage</h1>
        <p className="subtitle">Upload your file and ask questions instantly</p>

        <div className="section">
          <h2>Ask a Question</h2>
          <input
            type="text"
            placeholder="Type your question..."
            className="input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button onClick={handleAsk} className="btn primary">
            Ask Question
          </button>
        </div>

        <div className="section">
          <h2>Upload File</h2>
          <input
            type="file"
            onChange={handleFile}
            className="fileInput"
          />
          <button onClick={handleSubmit} className="btn secondary">
            Upload File
          </button>
        </div>

        <div className="answerBox">
          <h3>Answer</h3>
          <p>{answer || "Your answer will appear here..."}</p>
        </div>
      </div>
    </div>
  );
}

export default App;