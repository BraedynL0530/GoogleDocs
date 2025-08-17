# 📝 GoogleDocs Clone

A full-featured **real-time collaborative editor**, inspired by Google Docs — built with WebSockets and love.

[🌐 **Live Demo:**](https://realtimecollaborativeeditor.onrender.com)

---

## 🚀 Features

- ✍️ Real-time collaborative editing (WebSockets + Operational Transforms)  
- 🧑‍🤝‍🧑 Multi-user presence: live cursors, editing locks, viewer/editor modes  
- 🔒 Optional user authentication  
- 💾 Auto-save drafts & recover lost work  
- 🔁 Version control (coming soon!)

---

## ⚙️ Tech Stack

**Frontend**  
- Vanilla JS, HTML, CSS 

**Backend**  
- Django + Django Channels (ASGI) for WebSockets  


**Database**  
- MongoDB / PostgreSQL
- Redis for WebSocket layer + autosave cache

---

## 🧪 Local Setup

Clone the repo and get the backend up and running:

```bash
git clone https://github.com/BraedynL0530/GoogleDocs.git
cd GoogleDocs


## Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

## 📄 Set Up .env

Create a .env file in the backend folder with the following:

SECRET_KEY=your_super_secret_django_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,your-render-url.com

# Redis
REDIS_URL=redis://localhost:6379

Built by BraedynL0530
