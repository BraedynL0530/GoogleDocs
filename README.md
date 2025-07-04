# GoogleDocs Clone

A full-featured real-time collaborative editor, inspired by Google Docs.

DEMO LINK: https://realtimecollaborativeeditor.onrender.com/

## 🚀 Features
- ✍️ Real-time editing with operational transforms (OT)
- 👥 Multi-user presence (cursors, read-only constraints)
- 🔑 Optional authentication integration
- 💾 Autosave & recover draft functionality
- 🛠️ Rich-text formatting: headings, bold/italic, lists

## 🛠️ Tech Stack
- Frontend: React + [SlateJS/Quill/ProseMirror]
- Backend: Node/Express + WebSocket (or Django Channels)
- Database: MongoDB/PostgreSQL for document storage

## 🔧 Getting Started
```bash
git clone https://github.com/BraedynL0530/GoogleDocs.git
cd GoogleDocs
# Backend
cd backend && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver
# Frontend
cd frontend && npm install && npm start
