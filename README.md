# Horus Tito Exam - User Management System

Proyek ini adalah solusi **Fullstack Web Application** untuk Horus Entry Exam. Aplikasi ini menyediakan sistem manajemen pengguna lengkap dengan autentikasi (Login/Register), operasi CRUD, pencarian data, serta proteksi halaman menggunakan JWT.

---

## 🚀 Teknologi yang Digunakan

Aplikasi dibangun dengan arsitektur **Separation of Concerns** (Backend dan Frontend terpisah).

---

## 🖥️ Backend (API) — Flask

- **Framework:** Flask (Python) — Application Factory Pattern  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Auth:** Flask‑JWT‑Extended  
- **Migration:** Flask‑Migrate (Alembic)  
- **Testing:** Postman Collection  

---

## 💻 Frontend (UI) — Vue.js

- **Framework:** Vue.js 3 (Composition API)  
- **Build Tool:** Vite  
- **State:** Pinia  
- **Router:** Vue Router (Dengan Guards)  
- **Styling:** Tailwind CSS  
- **HTTP:** Axios dengan Interceptors  

---

## 📂 Struktur Proyek

```
horus-tito-exam/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── migrations/
│   ├── init_db.py
│   └── run.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── stores/
│   │   ├── views/
│   │   └── services/
│
└── README.md
```

---

## 🛠️ Cara Menjalankan Aplikasi

Anda bisa menjalankan proyek ini menggunakan **Docker** atau **manual**.

---

## Opsi 1 — Docker (Direkomendasikan)

Pastikan Docker & Docker Compose sudah terinstall.

```
docker-compose up --build
```

Akses:  
- Frontend → http://localhost:5173  
- Backend → http://localhost:5000  
- Database → Port 5432  

---

## Opsi 2 — Instalasi Manual

### 1. Persiapan Database  
Buat database PostgreSQL bernama:

```
horus_tito_db
```

---

### 2. Setup Backend

```
cd backend
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

cp .env.example .env
# Edit file .env sesuai kredensial DB

python init_db.py
# atau:
# flask db upgrade

python run.py
```

Backend berjalan di: http://localhost:5000

---

### 3. Setup Frontend

```
cd frontend
npm install

cp .env.example .env
# Pastikan:
# VITE_API_BASE_URL=http://localhost:5000

npm run dev
```

Frontend berjalan di: http://localhost:5173

---

## ✅ Fitur Utama

### Autentikasi
- Register + Validasi  
- Login + JWT Token  
- Hashing password (werkzeug.security)

### Manajemen User
- CRUD lengkap  
- Pencarian real-time (nama, username, email)  
- Edit user dengan pre-filled data  
- Hapus dengan konfirmasi  

### Proteksi & Keamanan
- Backend: `@jwt_required`  
- Frontend: Router Guard  
- CORS diaktifkan  

---

## 🧪 Pengujian API (Postman)

Lokasi file:  
```
backend/horus-tito-backend-api.postman_collection.json
```

Cara pakai:
1. Buka Postman  
2. Import file di atas  
3. Jalankan request sesuai kebutuhan  

---

## 📝 Catatan Penting

- Password disimpan dalam bentuk **hash** (bukan plaintext)  
- Menggunakan **psycopg2-binary** untuk koneksi database  
- Struktur modular → mudah dikembangkan & scalable  

---

## ✨ Dibuat oleh
**Tito Zaki Saputro**
