import './App.css';
import { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  // Handle file selection
  const handleFile = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    console.log("Selected file:", selected);
  };

  // Upload PDF
  const handleSubmit = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log("Upload response:", data);

      alert("File uploaded successfully");

    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  // Ask question
  const handleAsk = async () => {
    if (!query) {
      alert("Please enter a question");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: query }),
      });

      const data = await response.json();
      console.log("Answer:", data);

      setAnswer(data.answer);

    } catch (error) {
      console.error("Error asking question:", error);
      alert("Failed to get answer");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>PDF Q&A App</h2>

      {/* Upload Section */}
      <input 
        type="file" 
        onChange={handleFile} 
        className="fileInput"
      />

      <button onClick={handleSubmit} className="btn" disabled={loading}>
        {loading ? "Uploading..." : "Upload PDF"}
      </button>

      {/* Query Section */}
      <input 
        type="text" 
        placeholder="Ask something from PDF..." 
        className="input"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleAsk} className="btn" disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {/* Answer Section */}
      {answer && (
        <div className="answerBox">
          <h3>Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;