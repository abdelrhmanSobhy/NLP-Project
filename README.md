🧠 NLP-Project

A full-stack Natural Language Processing (NLP) web application consisting of a Flask REST API backend and a React/Vue frontend chatbot interface for handling user text queries and delivering intelligent responses.

🚀 Table of Contents

💡 About

⚙️ Features

📁 Project Structure

🛠 Technologies Used

🧩 Installation & Setup

▶️ Running the App

📌 API Endpoints

🤝 Contributing

📄 License

💡 About

This project demonstrates an NLP-powered chatbot with a backend API built on Flask and a frontend that interacts with users. It can be used as a learning tool or foundation for more advanced NLP integrations and chat interfaces.

⚙️ Features

✅ Chatbot API that takes user messages and returns responses
✅ NLP processing for intent detection and reply generation
✅ Health & stats endpoints for application monitoring
✅ Frontend UI for real-time interaction
✅ CORS configured for local development

📁 Project Structure
/NLP-Project
├── Backend/                        # Flask API backend
├── Frontend/student-chatbot/       # React chatbot UI
├── .gitignore
├── requirements.txt
└── README.md


Based on your repository contents. 
GitHub

🛠 Technologies Used

✔ Python (Flask)
✔ JavaScript (React)
✔ Flask-CORS
✔ NLP tooling (TF-IDF, KNN, or similar)
✔ REST API

🧩 Installation & Setup
Backend

Clone the repository:

git clone https://github.com/abdelrhmanSobhy/NLP-Project.git
cd NLP-Project/Backend


Create a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

▶️ Running the App
Start the Backend (Flask API)
python app.py


The server should start at:

http://localhost:5000

📌 API Endpoints
Endpoint	Method	Description
/api/health	GET	API health check
/api/greeting	GET	Get a greeting phrase
/api/chat	POST	Send user message & get bot response
/api/intents	GET	List available intents
/api/stats	GET	Stats about the model
/	GET	Basic API info

Example Request
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
