# 🎥 RAG-Based YouTube Transcript Chat System

An intelligent **Retrieval-Augmented Generation (RAG)** system built with **LangChain** and **Python**, enabling users to **interactively chat with YouTube videos** using their **transcripts**.  

The system retrieves relevant transcript segments based on user queries and generates context-aware answers.

---

## 🚀 Features

- 🧠 **Retrieval-Augmented Generation (RAG):** Combines semantic search with generative responses
- 🎬 **YouTube Transcript Integration:** Fetches and processes video transcripts
- 🧩 **LangChain Components:** Uses Document Loaders, Text Splitters, Vector Stores, and Retrievers
- 💬 **Conversational Memory:** Maintains context across chat turns
- ⚡ **Modular Structure:** Clean folder-based architecture for easy scaling

---


---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AneesFayyaz/yt_chatbot.git
cd yt_chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

In `config/settings.py`:

```python
OPENAI_API_KEY = "your_openai_api_key_here"
```

---

## ▶️ Usage

Run the chatbot:

```bash
python main.py
```

### Example Interaction

```
You: What is the main idea of this video?
Bot: The speaker discusses how consistency leads to long-term success.

You: Can you elaborate on that?
Bot: ...

Type 'exit' to stop the chat.
```

---

## 🧩 Technologies Used

- **Python 3.10+**
- **LangChain** - Framework for building LLM applications
- **FAISS ** - Vector database for semantic search
- **OpenAI API** - Language model for generation
- **YouTube Transcript API** - Fetching video transcripts

---

