"# django-chatapplication-" 
# 📝 Django Real-Time Chat Application

A **real-time chat application** built with Django and WebSockets using Django Channels. This project allows users to **sign up, log in, chat with other registered users**, and store chat history in a database.

## 🚀 Features
- ✅ **User Authentication** (Sign Up, Login, Logout)
- ✅ **Real-time Messaging** using **WebSockets**
- ✅ **Chat History Storage** in **SQLite**
- ✅ **Collapsible User List** to start a conversation
- ✅ **Asynchronous Communication** with Django Channels & Redis (optional)
- ✅ **Responsive Chat Interface** (HTML, CSS, JavaScript)

---

## 📂 Project Structure

---

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
