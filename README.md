# 🌍 Multilingual FAQ API - Django

Welcome to the **Multilingual FAQ API**! This Django-based project allows users to create, manage, and retrieve FAQs in multiple languages, complete with a WYSIWYG editor for rich-text formatting. 🚀

## 📌 Features
- ✅ **WYSIWYG Editor Support** (Using `django-ckeditor`)
- ✅ **Multi-language Translations** (Auto-generated via Google Translate API)
- ✅ **Efficient Caching** (Redis-backed translation caching)
- ✅ **REST API for FAQ Management**
- ✅ **Fast & Optimized Responses**
- ✅ **Admin Panel for Managing FAQs**
- ✅ **Unit Testing & Code Quality Checks**
- ✅ **Docker Support** 🐳

---

## 🚀 Getting Started
Follow these steps to set up and run the project locally.

### 1️⃣ Clone the Repository
```
git clone [https://github.com/kajol-9/myproject.git]
cd multilingual-faq-api
```

### 2️⃣ Create a Virtual Environment & Activate It
```
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
REDIS_URL=redis://localhost:6379/0
GOOGLE_TRANSLATE_API_KEY=your-google-api-key
```

### 5️⃣ Apply Migrations & Collect Static Files
```
python manage.py migrate
python manage.py collectstatic --noinput
```

### 6️⃣ Create a Superuser for Admin Panel
```
python manage.py createsuperuser
```

### 7️⃣ Run the Development Server
```
python manage.py runserver
```
Access the API at: `http://127.0.0.1:8000/api/faqs/` 📌  
Access the Admin Panel at: `http://127.0.0.1:8000/admin/` 🔑

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/faqs/` | Fetch all FAQs (default: English) |
| GET | `/api/faqs/?lang=hi` | Fetch FAQs in Hindi |
| GET | `/api/faqs/?lang=bn` | Fetch FAQs in Bengali |
| POST | `/api/faqs/` | Add a new FAQ |
| PUT | `/api/faqs/{id}/` | Update an FAQ |
| DELETE | `/api/faqs/{id}/` | Delete an FAQ |

---

## 🛠️ Running Tests
```
pytest
```

---

## 🛠️ Docker Setup 🐳

### 1️⃣ Build and Run the Docker Containers
```
docker-compose up --build
```

### 2️⃣ Stop the Containers
```
docker-compose down
```

---

## 📜 Contribution Guidelines
1. Fork the repository 🍴
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes:
```
git commit -m "feat: Add a new feature"
```
4. Push to the branch:
```
git push origin feature-branch
```
5. Open a Pull Request 🎉

---



