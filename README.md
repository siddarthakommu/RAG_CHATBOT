---

#  Agentic RAG Chatbot (Streamlit + Gemini + ChromaDB + MCP)

A Retrieval-Augmented Generation (RAG) chatbot built with Streamlit, HuggingFace embeddings, ChromaDB, and Gemini 1.5 Flash. It uses an **agent-based architecture** and **Model Context Protocol (MCP)** to manage message passing between components.

---

##  Features

*  Multi-file document ingestion (PDF, DOCX, PPTX, CSV, TXT, MD)
*  Chunking and embedding using `all-MiniLM-L6-v2`
*  Semantic search with ChromaDB vector store
*  Gemini 1.5 Flash for contextual answer generation
*  Streamlit chat interface with chat history
*  Agent-based modular architecture with MCP-style messaging
*  Shows top-3 retrieved chunks as sources for transparency

---

##  Project Structure

```
.
├── app.py                  # Streamlit UI
├── main.py                 # Pipeline entry
├── agents/
│   ├── ingestion_agent.py
│   ├── retrieval_agent.py
│   └── llm_agent.py
├── utils/
│   ├── file_loader.py
│   ├── chunker.py
│   └── mcp.py
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/siddarthakommu/RAG_CHATBOT
```

### 2. Create & Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv ev
source ev/bin/activate       # Linux/Mac
ev\Scripts\activate          # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Create a `.env` file:

```ini
GEMINI_API_KEY=your_google_gemini_api_key_here
```

Or you can export it in your terminal session:

```bash
export GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

##  Run the Chatbot

```bash
streamlit run app.py
```

---

##  Message Control Protocol (MCP)

Each message between agents follows a structured format:

```json
{
  "sender": "IngestionAgent",
  "receiver": "RetrievalAgent",
  "type": "INGESTION_RESULT",
  "trace_id": "uuid4-string",
  "payload": {
    "chunks": [...],
    "file": "example.pdf"
  }
}
```

---

---

## Tech Stack

* Python, Streamlit
* HuggingFace Transformers
* ChromaDB
* Google Gemini 1.5 Flash
* FAISS (optional if replacing ChromaDB)
* dotenv

---

##  Known Limitations

* ChromaDB is in-memory by default. Use persistent storage if needed.
* Gemini API usage may have quota limits.

---

##  Future Scope

* Add user authentication
* Support voice query input
* Store chat logs in a database
* Add real-time analytics dashboard

---


