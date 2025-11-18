# Horus Tito Exam - User Management System

Proyek ini adalah solusi **Fullstack Web Application** untuk Horus Entry Exam. Sistem ini menyediakan manajemen pengguna lengkap: autentikasi (Login/Register), CRUD, pencarian data, serta proteksi halaman menggunakan JWT.

---

## 🚀 Teknologi yang Digunakan

Aplikasi dibangun dengan arsitektur **Separation of Concerns**, memisahkan Backend dan Frontend secara jelas.

---

## 🖥️ Backend (API) — Flask

- **Framework:** Flask (Application Factory Pattern)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Auth:** Flask‑JWT‑Extended
- **Migration:** Flask‑Migrate (Alembic)
- **Testing:** Postman Collection
- **Containerization:** Docker & Docker Compose

---

## 💻 Frontend (UI) — Vue.js

- **Framework:** Vue.js 3 (Composition API)
- **Build Tool:** Vite
- **State Management:** Pinia
- **Routing:** Vue Router (Dengan Guards)
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios (Interceptor Support)

---

## 📂 Struktur Proyek

```
horus-tito-exam/
├── backend/               # API & Database Logic
│   ├── app/
│   ├── migrations/
│   ├── docker-compose.yml
│   ├── init_db.py
│   └── run.py
│
├── frontend/              # User Interface
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

# 🛠️ Cara Menjalankan Aplikasi

Anda dapat menjalankan **Backend + Database** dengan Docker, dan **Frontend** secara lokal.

---

# Opsi 1 — Docker (Backend & DB) + Frontend Lokal  
**Direkomendasikan** karena tidak perlu instalasi PostgreSQL/Python secara manual.

---

## 1. Jalankan Backend & Database

Masuk ke folder backend:

```
cd backend
docker-compose up --build
```

Backend berjalan di: **http://localhost:5000**  
Database berjalan di: **port 5432**

### Inisialisasi Database (pertama kali)

```
docker-compose exec backend flask db upgrade
```

Atau alternatif:

```
docker-compose exec backend python init_db.py
```

---

## 2. Jalankan Frontend

```
cd frontend
npm install
npm run dev
```

Frontend berjalan di: **http://localhost:5173**

---

# Opsi 2 — Instalasi Manual (Tanpa Docker)

---

## 1. Persiapan Database

Pastikan PostgreSQL sudah terinstall dan buat database:

```
horus_tito_db
```

---

## 2. Setup Backend

```
cd backend

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Edit konfigurasi database dalam file .env

python init_db.py

python run.py
```

Backend berjalan di: **http://localhost:5000**

---

## 3. Setup Frontend

```
cd frontend
npm install

cp .env.example .env
# Pastikan:
# VITE_API_BASE_URL=http://localhost:5000

npm run dev
```

---

# ✅ Fitur Utama

## Autentikasi
- Register user baru dengan validasi lengkap
- Login dengan JWT Token
- Password di-hash menggunakan `werkzeug.security`

## Manajemen User
- **Create** — Registrasi akun
- **Read** — Dashboard user (list/pagination)
- **Update** — Edit user (nama, email, username)
- **Delete** — Hapus user dengan konfirmasi
- **Search** — Pencarian realtime (nama, username, email)

## Proteksi & Keamanan
- Backend: `@jwt_required`
- Frontend: Navigation Guard (proteksi Dashboard)
- Mencegah user menghapus akun sendiri saat sedang login

---

# 🧪 Pengujian API (Postman)

File berada di:

```
backend/horus-tito-backend-api.postman_collection.json
```

Cara pakai:
1. Buka Postman
2. Import file tersebut
3. Jalankan request sesuai kebutuhan

---

# ✨ Dibuat oleh  
**Tito Zaki Saputro**
