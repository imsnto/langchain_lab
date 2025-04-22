# LangChain Lab

LangChain Lab is a comprehensive exploration of LangChain's core components and capabilities. This project demonstrates practical implementations of LangChain features such as prompts, memory, RAG pipelines, LLMs, and tool customization.

---

## 📁 Project Structure

```
langchain_lab/
├── embeddings/         # Implementations for text embeddings
├── llms/               # Large Language Model configurations
├── memory/             # Memory components and examples
├── rag/                # Retrieval Augmented Generation
│   ├── 01.rag_pipeline.py
│   └── sample_doc.txt
├── settings/           # Project configurations and settings
├── tools/              # LangChain tools implementations
│   ├── 01.default_tools.py
│   ├── 02.customize_default_tools.py
│   ├── 03.custom_tool.py
│   └── utility.py
└── vector_store/       # Vector storage implementations
```

---

## ✨ Features

### 🔹 1. Prompt and Chain Operations
- Chat prompt templates
- Sequential and custom chains
- Output parsing and formatting

### 🔹 2. Memory Systems
- Conversational memory implementations
- Message history management
- Various memory types and storage backends

### 🔹 3. RAG (Retrieval Augmented Generation)
- Complete RAG pipeline setup
- Document ingestion and retrieval
- Augmented generation using vector search

### 🔹 4. Tools
- Using default LangChain tools
- Creating and customizing tools
- Utility functions for tool enhancement

### 🔹 5. LLM Integration
- Integration with **Groq LLM**
- Model used: `llama-3.3-70b-versatile`
- Custom prompt engineering examples

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/imsnto/langchain_lab.git
   cd langchain_lab
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the root directory
   - Add necessary API keys and configurations

---

### ➔ Memory Example
Demonstrates how to implement and use chat memory to maintain context across interactions.

### ➔ RAG Example
Includes an end-to-end RAG pipeline showcasing document retrieval and generation capabilities.

---

