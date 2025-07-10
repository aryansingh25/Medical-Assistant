# 🩺 RAG-Based Medical Assistant

A **Retrieval-Augmented Generation (RAG)** powered **Medical Assistant** that allows users to upload medical PDFs and query them in natural language. Built using **LangChain**, it combines document retrieval with powerful language models to deliver accurate and context-aware answers.

---

## ✨ Features

- 📄 **Upload medical PDFs** and automatically extract information
- 🔍 **Query using natural language**, get accurate answers from documents
- 🧠 **RAG architecture** for real-time context-aware answers
- 🧬 **LLM:** LLaMA (via Groq API)
- 🌐 **Embeddings:** Google Gemini
- 📂 **Vector DB:** Pinecone
- 🌟 **Frontend:** Streamlit UI for ease of use

---

## 🧱 Tech Stack

| Layer         | Tech Used               |
|---------------|--------------------------|
| LLM           | Groq API (LLaMA)         |
| Embeddings    | Google Gemini            |
| Vector Store  | Pinecone                 |
| Framework     | LangChain (RAG Chain)    |
| Frontend      | Streamlit                |
| Backend       | FastAPI / Python         |

---

## 🚀 How It Works

1. **Upload PDF** via Streamlit interface
2. **Text is extracted** and chunked
3. **Embeddings generated** using Google Gemini
4. **Chunks stored in Pinecone** for vector retrieval
5. On query:
   - Similar chunks are retrieved
   - Sent along with the query to Groq's LLaMA via LangChain
   - Answer is generated and shown to the user

---

## 🖥️ Local Setup
Clone the repository:
   ```bash
   git clone https://github.com/aryansingh25/Medical-Assistant.git
   cd Medical-Assistant
   ```
