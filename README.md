# 🤖 U-Pustaka Q&A Chatbot

An intelligent chatbot built to assist users of the U-Pustaka platform by answering queries with real-time, context-aware responses using a Retrieval-Augmented Generation (RAG) pipeline powered by **Gemini LLM**.

## 📽️ Project Demo

[![Watch the Demo](https://img.youtube.com/vi/AzconfIjaYI/0.jpg)](https://www.youtube.com/watch?v=AzconfIjaYI)

> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=AzconfIjaYI)

---

## 🧠 Features

- ✨ **Natural Q&A**: Uses LangChain and Gemini LLM for accurate and contextual answers.
- ⚡ **Real-time Responses**: Integrated WebSocket for dynamic streaming of responses.
- 💾 **Session Memory**: Conversation sessions are stored in MongoDB for persistent interaction history.
- 🧱 **Modular Architecture**: Clean and scalable FastAPI backend with separate frontend interface.

---

## 🛠️ Tech Stack

| Layer       | Technology                  |
|------------|------------------------------|
| Frontend   | HTML, CSS, JavaScript        |
| Backend    | FastAPI                      |
| LLM        | Gemini LLM via LangChain     |
| Retrieval  | RAG Pipeline (custom corpus) |
| Database   | MongoDB                      |
| Streaming  | WebSocket                    |

---

## 📂 Project Structure

```bash
.
├── backend/
│   ├── app.py                # FastAPI app with WebSocket support
│   ├── chatbot_logic.py      # LangChain + Gemini LLM integration
│   └── database.py           # MongoDB session storage
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/u-pustaka-chatbot.git
cd u-pustaka-chatbot
```

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the Server

```bash
uvicorn app:app --reload
```

### 4. Open `index.html` in your browser


## 🤝 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Gemini API](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [U-Pustaka](https://www.u-pustaka.gov.my/)

## 📬 Contact

**Developer:** Kasheng  
📧 *your-email@example.com*  
🌐 *LinkedIn / Portfolio links if any*
