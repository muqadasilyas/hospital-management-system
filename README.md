# Hospital Management System

A Django-based hospital management system with role-based access for
Admins, Doctors, Patients, and Receptionists.

## Features

- Patient records (create, view, update, delete) with age auto-calculated from date of birth
- Doctor records linked to departments
- Appointment scheduling with status tracking (Pending / Rejected / Completed)
- Role-based permissions — each user type sees and can act on only what's relevant to them:
  - **Doctors** see their own patients and appointments
  - **Patients** see their own record and appointments
  - **Receptionists** see and manage all patients, doctors, and appointments
  - **Admins** (superusers) have full access

## Setup

1. Clone the repo and enter the project folder:
```bash
   git clone https://github.com/muqadasilyas/hospital-management-system.git
   cd hospital-management-system/hms
```

2. Create a virtual environment and install dependencies:
```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
```

3. Set up your environment variables (see `.env.example` if present, or set `SECRET_KEY` and `DEBUG` in your shell).

4. Run migrations and create an admin user:
```bash
   python manage.py migrate
   python manage.py createsuperuser
```

5. Start the dev server:
```bash
   python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/admin/` to log in and set up Departments, Doctors, and Patients, and assign users to the `Doctors`, `Patient`, or `Receptionist` groups to test role-based access.

## Tech stack

- Python / Django 6.1
- SQLite (default dev database)
