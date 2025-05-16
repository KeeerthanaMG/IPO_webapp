# 📘 IPO WebApp Backend - Django REST API

Welcome to the backend of the IPO (Initial Public Offering) Management WebApp. This project exposes a RESTful API for managing company IPOs, company logos, and associated documents like RHP and DRHP PDFs.

---

## 🚀 Tech Stack

| Category       | Tech                     |
|----------------|--------------------------|
| Language       | Python 3.10+             |
| Framework      | Django 5.0 + Django REST Framework |
| Database       | PostgreSQL               |
| ORM            | Django ORM               |
| API Layer      | Django REST Framework    |
| File Uploads   | Pillow + Media Settings  |
| Filtering/Sort | django-filter            |
| Version Control| Git + GitHub             |

---

## 📁 Folder Structure (Cleaned)

```
IPO_webapp/
├── ipo_project/             # Django project settings & URLs
│   └── settings.py
│   └── urls.py
│
├── ipo/                    # Main app containing APIs & models
│   ├── models.py           # Company, IPO, Document models
│   ├── serializers.py      # DRF serializers for JSON conversion
│   ├── admin.py            # Register models to admin panel
│   ├── views/
│   │   ├── company_views.py
│   │   ├── ipo_views.py
│   │   └── document_views.py
│   ├── urls/
│   │   └── api_urls.py     # API endpoints (routers)
│   ├── utils/              # Optional helpers
│   └── tests/              # Unit tests (TBD)
│
├── media/                  # Uploaded files like PDFs and logos
├── requirements.txt        # Project dependencies
├── manage.py               # Django CLI
└── .env                    # (Optional) Environment configs
```

---

## 💡 Project Overview

This backend provides REST APIs for:

- 🔹 Managing Companies and Logos
- 🔹 Managing IPO data (dates, price bands, returns)
- 🔹 Uploading RHP/DRHP documents
- 🔹 Viewing & Filtering IPO listings

---

## 🛠️ How to Run This Backend (Beginner Friendly)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/IPO_webapp.git
cd IPO_webapp
```

### Step 2: Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

If you don’t have requirements.txt, install manually:
```bash
pip install django djangorestframework django-filter Pillow psycopg2-binary
```

### Step 4: Configure Database

PostgreSQL must be installed and running. In ipo_project/settings.py:
```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'ipo_db',
    'USER': 'ipo_user',
    'PASSWORD': 'your_password',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}
```

Create DB using pgAdmin or terminal:
```sql
CREATE DATABASE ipo_db;
CREATE USER ipo_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ipo_db TO ipo_user;
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Run the Server

```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/api/

---

## 📨 Available API Endpoints (For Frontend Team)

| Endpoint               | Method | Description                 |
|------------------------|--------|-----------------------------|
| /api/companies/        | GET    | List all companies          |
| /api/companies/        | POST   | Create new company (form)   |
| /api/companies/{id}/   | PUT    | Update company              |
| /api/ipos/             | GET    | List all IPOs               |
| /api/ipos/?status=Open | GET    | Filter IPOs by status       |
| /api/ipos/             | POST   | Create new IPO (JSON)       |
| /api/documents/        | GET    | List all documents          |
| /api/documents/        | POST   | Upload RHP/DRHP PDFs        |

> Use /api/ endpoints in Postman or frontend app to send/receive JSON or form data.

---

## 📷 File Uploads (Logos & PDFs)

Media files are uploaded to:
- Company logos → /media/logos/
- RHP PDFs → /media/docs/rhp/
- DRHP PDFs → /media/docs/drhp/

No frontend UI is required for testing file uploads — use Postman.

---

## 🔧 Admin Panel (Optional)

Create a superuser:
```bash
python manage.py createsuperuser
```

Visit http://127.0.0.1:8000/admin/ and login to visually add/edit IPO data.

---

## 🧪 Postman Ready

All APIs are tested using Postman. Frontend devs can:
- Use GET to fetch IPO/Company data
- Use POST to upload data
- Use filtering & sorting with URL params

Need the exported Postman collection? Ask the backend team.

---

## 🙌 Contributing

This is a backend-only repo. For frontend integration:
- Use the base URL: http://127.0.0.1:8000/api/
- Connect using Axios, fetch, or Postman

Feel free to report issues or request enhancements.

---

Happy Coding! 🎉
