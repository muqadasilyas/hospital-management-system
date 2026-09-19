# 🏥 Hospital Management System

A Django-based hospital management system with role-based access for Admins, Doctors, Patients, and Receptionists — patient records, doctor–department assignments, and appointment scheduling with status tracking, all in one place.

## ✨ Features

- 🧑‍⚕️ **Patients** — first/last name, gender, blood type, date of birth, phone; each patient is optionally linked to a Django `User` account
- 👨‍⚕️ **Doctors** — name, specialization, phone, linked to a `Department`; each doctor is optionally linked to a `User` account
- 🏢 **Departments** — name + description, doctors are grouped under them
- 📅 **Appointments** — date, time, reason, status (`Pending` / `Rejected` / `Completed`), tied to a doctor and a patient, with a dedicated `complete_appointment` permission for marking one done
- 🔐 **Role-based access control**, enforced in the view layer via Django's groups/permissions system:

  | Role | Access |
  |------|--------|
  | 👨‍⚕️ Doctor | Own appointments only (`doctor=user.doctor`) |
  | 🧑‍🦱 Patient | Own appointments only (`patient=user.patient`) |
  | 🗂️ Receptionist | All appointments |
  | 🛡️ Admin (superuser) | Full access to everything |

- 🔑 **Authentication** — session-based login/logout (`/auth/login/`, `/auth/logout/`), redirects to the patient list on login

## 🛠️ Tech Stack

- 🐍 **Backend:** Python, Django 6.1.1
- 🗄️ **Database:** SQLite (dev default)
- 📦 **Dependencies:** `asgiref`, `sqlparse`, `tzdata` (see `hms/requirements.txt`)

## 📂 Project Structure

```
hospital-management-system/
└── hms/
    ├── hms/                # project config: settings.py, urls.py, wsgi/asgi
    ├── authentication/     # login/logout views
    ├── department/         # Department model, CRUD views
    ├── patient/            # Patient model, CRUD views
    ├── doctor/             # Doctor model (FK → Department), CRUD views
    ├── appointments/       # Appointments model (FK → Doctor, Patient), role-filtered views
    ├── templates/          # base.html
    └── manage.py
```

Each app follows the same shape: `models.py`, `views.py` (class-based, generic `ListView`/`CreateView`/`DetailView`/`UpdateView`/`DeleteView`), `urls.py`, `admin.py`, and its own `templates/<app>/` folder.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. **Clone the repo** and enter the project folder:
   ```bash
   git clone https://github.com/muqadasilyas/hospital-management-system.git
   cd hospital-management-system/hms
   ```

2. **Create a virtual environment** and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run migrations and create an admin user:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Start the dev server:**
   ```bash
   python manage.py runserver
   ```

5. **Visit** `http://127.0.0.1:8000/admin/` to log in, create Departments, Doctors, and Patients, and create the `Doctors`, `Patient`, and `Receptionist` groups (with appropriate model permissions) to test role-based access.

> ⚠️ **Note:** `SECRET_KEY` and `DEBUG` are currently hardcoded in `hms/hms/settings.py` for local development. Before deploying, move these into environment variables and set `DEBUG = False`.

## 🌐 Routes

| Path | App |
|------|-----|
| `/admin/` | Django admin |
| `/patient/` | Patient CRUD |
| `/doctor/` | Doctor CRUD |
| `/department/` | Department CRUD |
| `/appointment/` | Appointment CRUD |
| `/auth/login/`, `/auth/logout/` | Authentication |


## 👤 Author

**Muqadas Ilyas**
- GitHub: [@muqadasilyas](https://github.com/muqadasilyas)
- Portfolio: [muqadas-ilyas-portfolio.vercel.app](https://muqadas-ilyas-portfolio.vercel.app)
