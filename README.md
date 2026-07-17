# 🎓 AI Student Support Chatbot

An AI-powered Student Support Chatbot developed using **Python, NLP, FAISS, RAG, and Google Gemini AI**. The chatbot helps students by answering queries related to college information such as fees, hostel, library, attendance, and scholarships using semantic search and Generative AI.

---

# 📌 Project Overview

Traditional chatbots rely on keyword matching, which often fails when users ask the same question in different ways.

This project uses **Natural Language Processing (NLP)** and **Retrieval-Augmented Generation (RAG)** to understand the meaning of a student's query, retrieve the most relevant information from the knowledge base using **FAISS**, and generate a natural, human-like response using **Google Gemini AI**.

---

# 🚀 Features

* AI-powered student support chatbot
* Natural Language Processing (NLP)
* Semantic Search using Sentence Transformers
* FAISS Vector Database for fast similarity search
* Google Gemini AI for response generation
* Streamlit-based interactive user interface
* Modular project architecture
* JSON-based knowledge base
* Intent Detection
* Entity Extraction
* Chat History Management

---

# 🛠 Technologies Used

* Python
* Streamlit
* spaCy
* Sentence Transformers
* FAISS
* NumPy
* Google Gemini API
* Python Dotenv

---

# 📂 Project Structure

```
StudentSupportChatbot/

│
├── chatbot.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── knowledge/
│      fees.json
│      hostel.json
│      library.json
│      attendance.json
│      scholarship.json
│
├── nlp/
│      preprocessing.py
│      intent.py
│      entities.py
│      sentiment.py
│
├── retrieval/
│      embedding.py
│      vector_store.py
│      search.py
│
├── genai/
│      grok.py
│      prompt.py
│
└── utils/
       helper.py
       chat_history.py
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd StudentSupportChatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

---

## 6. Configure Environment Variables

Create a **.env** file in the project root.

Example:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## 7. Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open automatically in your browser.

---

# 🧠 How It Works

1. User enters a question.
2. NLP preprocesses the text.
3. User query is converted into an embedding.
4. FAISS searches the most similar questions.
5. Relevant context is retrieved.
6. Prompt is created using retrieved context.
7. Google Gemini AI generates the final answer.
8. Response is displayed in the Streamlit interface.

---

# 🔄 Project Workflow

```
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
Sentence Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Relevant Knowledge Retrieval
      │
      ▼
Prompt Engineering
      │
      ▼
Google Gemini AI
      │
      ▼
Generated Response
```

---

# 💡 Sample Questions

* What is the MCA fee?
* What is the hostel fee?
* How many books can I borrow from the library?
* What is the attendance policy?
* Who is eligible for scholarships?
* When does the library open?
* How can I apply for a scholarship?
* What is the examination attendance requirement?

---

# 📈 Future Enhancements

* Database Integration (MongoDB/MySQL)
* Voice-Based Chatbot
* Multi-language Support
* Student Authentication
* Admin Dashboard
* PDF Knowledge Base
* Conversation Memory
* Fine-Tuned LLM
* REST API using FastAPI
* Cloud Deployment

---

# 📚 Concepts Implemented

* Natural Language Processing (NLP)
* Text Preprocessing
* Tokenization
* Stopword Removal
* Lemmatization
* Intent Detection
* Entity Extraction
* Sentence Embeddings
* Semantic Search
* Vector Database
* FAISS
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Generative AI
* Streamlit UI Development

---

# 👨‍💻 Author

**Vikrant Prajapati**

Internship Project

AI Student Support Chatbot

---

# 📄 License

This project is developed for educational and internship purposes only.
