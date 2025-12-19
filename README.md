# 🧠 NLP Project

A full‑stack **Natural Language Processing (NLP) Chatbot** project built with a **Flask REST API backend** and a **frontend chatbot interface**. The project demonstrates intent detection, text processing, and API‑based communication between frontend and backend.

---

## 🚀 Features

* 🤖 NLP‑based chatbot
* 🔌 RESTful API using Flask
* 🌐 Frontend chatbot UI
* 🔁 Real‑time message exchange
* 🧪 Health & statistics endpoints
* 🔒 CORS configured for frontend integration

---

## 📁 Project Structure

```
NLP-Project/
├── Backend/                 # Flask API backend
│   ├── app.py
│   ├── chatbot.py
│   ├── requirements.txt
│   └── ...
│
├── Frontend/
│   └── student-chatbot/     # Frontend (React / Vite)
│
├── .gitignore
└── README.md
```

---

## 🛠 Technologies Used

### Backend

* Python
* Flask
* Flask‑CORS
* NLP techniques (TF‑IDF, KNN, etc.)

### Frontend

* JavaScript
* React / Vite
* Fetch API

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abdelrhmanSobhy/NLP-Project.git
cd NLP-Project
```

---

### 2️⃣ Backend Setup

```bash
cd Backend
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

### 3️⃣ Run the Backend

```bash
python app.py
```

Backend will run at:

```
http://localhost:5000
```

---

## 📡 API Endpoints

| Endpoint        | Method | Description         |
| --------------- | ------ | ------------------- |
| `/`             | GET    | API info            |
| `/api/health`   | GET    | Health check        |
| `/api/greeting` | GET    | Time‑based greeting |
| `/api/chat`     | POST   | Chat with the bot   |
| `/api/intents`  | GET    | Available intents   |
| `/api/stats`    | GET    | Model statistics    |

### Example Request

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
```

---

## 🌐 Frontend Setup

```bash
cd Frontend/student-chatbot
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🔐 Environment Variables

Create a `.env` file if needed (do not commit it):

```
PORT=5000
```

---

## 📌 Notes

* `.gitignore` is configured to exclude:

  * `node_modules/`
  * `venv/`
  * `.env`
* `.nvmrc` can be used to define Node version

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📄 License

This project is open‑source and intended for **educational purposes**.

---

⭐ If you like this project, don’t forget to star the repository!
