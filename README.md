# Medical Chatbot

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---
## Demo
This project is a Medical Chatbot designed to assist users with healthcare-related queries using AI-powered responses.<br>
**Link to Demo:** [Medical-Chatbot](#) 





![Poem-Classification](https://i.imgur.com/xvEnaoQ.jpeg)

---

## Overview
The Medical Chatbot leverages Large Language Models (LLMs) to provide accurate and helpful medical insights. It can assist with symptom checking, preliminary diagnosis suggestions, and general health-related inquiries. This chatbot does not replace professional medical advice but serves as a supplementary tool for users.

Key Features:

- Uses meta-llama/Llama-2-7b-chat-hf for generating responses.

- NLP-powered chatbot with real-time medical query handling.

- cure and privacy-focused.

- loyed as a web application for accessibility.
---

## Motivation


The need for an AI-powered medical chatbot arises from the increasing demand for instant healthcare guidance. Many users require quick, preliminary medical information before consulting a professional. This chatbot provides general healthcare advice while emphasizing the importance of consulting licensed medical practitioners for critical concerns.

---

## Technical Aspect

1️⃣ Model & AI Framework

- Llama 2 (Meta-Llama/Llama-2-7b-chat-hf) – Core LLM for medical responses
 - LangChain – Efficient LLM integration and chaining

2️⃣ Retrieval & Storage
- Pinecone – Vector database for storing and retrieving medical knowledge
- FAISS (Alternative) – For local vector search

 3️⃣ Backend & Web Framework
- Flask – Web API for chatbot
- FastAPI (Planned) – High-performance alternative

4️⃣ Frontend
- HTML + CSS + JavaScript – Basic UI
- Streamlit (Planned) – Interactive UI for real-time chat

5️⃣ Deployment
- Render / Hugging Face Spaces / AWS (TBD)



---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```

## Deployment on Render

To deploy the Flask web app on Render:
- Push your code to GitHub.
- Log in to Render and create a new web service.
- Connect the GitHub repository.
- Configure environment variables (if any).
- Deploy and access your app live.

## Directory Tree 
```
medical-chatbot/
├── .github/                   📁 GitHub workflows & configurations  
├── data/                      📁 Dataset storage (medical-related data)  
├── Experiments/               📁 Model training & experimentation logs  
├── logs/                      📁 Application logs  
├── medical_chatbot.egg-info/  📁 Package metadata (if using setuptools)  
├── src/                       📁 Source code for the chatbot  
│   ├── __init__.py            📄 Package initialization  
│   ├── chatbot.py             🤖 Core chatbot logic  
│   ├── preprocess.py          🔄 Data preprocessing functions  
│   ├── model.py               🧠 Model loading & inference  
│   ├── utils.py               🛠️ Utility functions  
├── static/                    📁 Static files (CSS, JS, images)  
├── templates/                 📁 HTML templates for UI  
│   ├── index.html             🖥️ Main chatbot UI  
├── venv/                      🐍 Virtual environment (dependencies)  
├── .env                       🌍 Environment variables  
├── .gitignore                 🚫 Files & folders to ignore in Git  
├── LICENSE                    📜 License file  
├── app.py                     🚀 Flask application entry point  
├── README.md                  📖 Project documentation  
├── requirements.txt           📦 Python dependencies  
├── setup.py                   🔧 Installation setup  
└── template.py                📜 Extra script (if needed)  

```

## To Do

- xpand medical knowledge base.

- Improve chatbot response accuracy.

- Integrate a symptom checker module.

- Enhance the UI with interactive visualization features.


## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used
- Python 3.10 🐍 – Core programming language
- Flask 🧩 – Web framework for building the chatbot API
- LangChain 🦜🔗 – LLM orchestration and prompt management
- Pinecone 🌲 – Vector database for fast medical knowledge retrieval



![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://images.seeklogo.com/logo-png/61/1/langchain-logo-png_seeklogo-611654.png" width=170>](https://python.langchain.com/docs/introduction/) 
[<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 

[<img target="_blank" src="https://seeklogo.com/images/P/pinecone-logo-C2C73F6C10-seeklogo.com.png" width=170>](https://docs.pinecone.io/guides/get-started/overview) 

---

## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|

**Bablu Kumar Pandey**

- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
- **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.

## Credits

Special thanks to the contributors of meta-llama/Llama-2-7b-chat-hf and other open-source projects that made this chatbot possible.


