# 🔧 Dhaka Threads — Backend API

The RESTful backend powering the **Dhaka Threads** e-commerce platform. Built with Django REST Framework, it handles product management, user authentication, cart logic, reviews, and secure JWT-based sessions.

🌐 **Live Demo:** [dhaka-threads-client.vercel.app](https://dhaka-threads-client.vercel.app/)
&nbsp;|&nbsp;
🖥️ **Frontend Repo:** [github.com/jjannat04/dhaka-threads-client](https://github.com/jjannat04/dhaka-threads-client)
&nbsp;|&nbsp;
🔧 **Backend Repo:** [github.com/jjannat04/dhaka-threads-backend](https://github.com/jjannat04/dhaka-threads-backend)

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend Framework | Django, Django REST Framework (DRF) |
| Database | PostgreSQL / SQLite |
| Auth | JWT via `djangorestframework-simplejwt` |
| API Style | RESTful JSON API |
| Deployment | Render |

---

## ✨ API Features

- 🔐 **JWT Authentication** — Secure token-based login, register, refresh, and logout endpoints
- 🛍️ **Product API** — Full CRUD for products with category, price, and stock management
- 🔍 **Filtering & Search** — Query products by category, price range, and keywords
- ⭐ **Reviews & Ratings** — Authenticated users can post, edit, and delete reviews per product
- 🛒 **Cart & Wishlist** — User-scoped cart and wishlist endpoints with persistent server-side storage
- 👤 **User Profile** — Profile retrieval and update endpoints

---

## 📦 Dependencies

```txt
Django>=4.2
djangorestframework
djangorestframework-simplejwt
django-cors-headers
Pillow
psycopg2-binary
gunicorn
whitenoise
python-decouple
```

> Full list in [`requirements.txt`](./requirements.txt)

---

## 🚀 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/jjannat04/dhaka-threads-backend.git
cd dhaka-threads-backend
```

### 2. Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

API available at 👉 `http://127.0.0.1:8000/api/`
Admin panel at 👉 `http://127.0.0.1:8000/admin/`

---

## 🔗 Relevant Links

| Resource | Link |
|----------|------|
| 🌐 Live Demo | [dhaka-threads-client.vercel.app](https://dhaka-threads-client.vercel.app/) |
| 🖥️ Frontend Repo | [github.com/jjannat04/dhaka-threads-client](https://github.com/jjannat04/dhaka-threads-client) |
| 🔧 Backend Repo | [github.com/jjannat04/dhaka-threads-backend](https://github.com/jjannat04/dhaka-threads-backend) |
| 👤 Developer | [linkedin.com/in/jannatul-ferdous-b504831b3](https://www.linkedin.com/in/jannatul-ferdous-b504831b3/) |

---

## 👩‍💻 Author

**Jannatul Ferdous**
CSE Undergraduate @ CUET | Django & React Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jannatul-ferdous-b504831b3/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/jjannat04)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=flat&logo=codeforces&logoColor=white)](https://codeforces.com/profile/jjasperruby)

---

> ⭐ If you found this project useful, consider giving it a star!
