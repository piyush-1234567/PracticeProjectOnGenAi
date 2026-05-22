# 📄 PDF Q&A System

An intelligent **PDF Question-Answering System** that allows users to upload documents and ask questions in natural language. The system uses **AI + NLP + semantic search** to retrieve accurate answers from document content.

---

## 🚀 Features

- 📂 Upload and process PDF documents  
- 🔍 Extract and clean text from PDFs  
- 🧠 Semantic search using embeddings  
- 💬 Ask questions in natural language  
- ⚡ Get context-aware answers instantly  
- 🗂 Multi-PDF support *(optional)*  

---

## 🏗️ Tech Stack

### Frontend
- React.js  

### Backend
- FastAPI (Python)  
- Uvicorn  

### AI / NLP
- OpenAI  
- Hugging Face  
- LangChain  

### Vector Database
- FAISS  
- Pinecone *(optional)*  
- ChromaDB *(optional)*  

### PDF Processing
- PyPDF  
- pdfplumber  

---

## ⚙️ How It Works

1. User uploads a PDF  
2. Text is extracted from the document  
3. Text is split into smaller chunks  
4. Embeddings are generated for each chunk  
5. Stored in a vector database  
6. User asks a question  
7. Relevant chunks are retrieved  
8. LLM generates the final answer  

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/piyush-1234567/PracticeProjectOnGenAi.git
cd pdf-qna
```

---

### 2. Backend Setup

Install dependencies:

```bash
pip install fastapi uvicorn python-multipart huggingface_hub pymupdf sentence-transformers chromadb

```

Set your API key:

```bash
export HF_TOKEN="your_api_key"
```

Run backend:

```bash
uvicorn main:app --reload
```

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```
### 4. Backend Setup
```bash
source pymupdf-venv/bin/activate
export HF_TOKEN="api_key"
uvicorn main:app --reload
```
---

## 📸 Demo

Upload a PDF → Ask questions → Get answers instantly 🚀  

---

## 🧪 Example Queries

- "Summarize this document"  
- "What are the key points?"  
- "Explain section 3"  
- "Who is the author?"  

---

## 📁 Project Structure

```
pdf-qna/
│
├── backend/
│   ├── main.py
│   ├── utils/
│   ├── services/
│
├── frontend/
│   ├── src/
│   ├── components/
│
└── README.md
```

---

## 🔮 Future Improvements

- 🔐 User authentication  
- 🌐 Multi-language support  
- 📊 Highlight answers inside PDF  
- 📚 Multi-document comparison  
- 🧠 Improved context understanding  

---

## 📚 Libraries Used

- FastAPI  
- Uvicorn  
- CORS Middleware  
- HuggingFace Hub  
- LangChain  
- FAISS  

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests.

---

## 🙌 Acknowledgements

- OpenAI  
- Hugging Face  
- LangChain  
- FAISS & vector database tools  

---

⭐ If you like this project, consider giving it a star!
