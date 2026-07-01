# 🏥 Shree Sahaj Naturopathy Clinic - Management Web Application

Shree Sahaj Naturopathy Clinic Management System is a full-stack Django application engineered to streamline patient record tracking, optimize administrative workflows, and manage clinic data securely. System users can register patients, modify case files, and find digital medical card details instantly, while administrators enjoy advanced search features and comprehensive database control tools.

## 🔗 Try it on

https://clinicwebsite.onrender.com

## ✨ Features

### 👤 Assistant / Staff Features
- Seamless dashboard interface for quick navigation between patient files
- Register new patient demographic information and digital clinical records
- View specialized patient detail cards with active treatment history
- Rapidly filter and load patient data files directly without full page reloads

### 🛡️ Admin Features
- Secure control panel to manage, edit, and safely delete patient logs
- Advanced multi-field live search parameters utilizing fields like `name` and `phone`
- Dynamic inline adjustments and clickable row shortcuts to eliminate redundant navigation clicks
- Access backend administration console safely through encrypted native login structures

### 🔧 Other Functionalities
- Automated configuration scripts to seamlessly initialize production database tables
- Custom background workflows to safely construct initial administrative superusers
- Production-grade Cross-Site Request Forgery (CSRF) protection built for strict domain handling
- High-performance relational schema layouts optimized to reduce query latencies

## 🧰 Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Django |
| Database | SQLite (Development), PostgreSQL (Production) |
| Security | CSRF Tokens, Secure Sessions, HTTPS Headers |
| DevOps & Tools | Git, GitHub, Render Cloud Platform, Linux/Bash Scripts |

## 📁 Project Structure

```bash
clinicwebsite/
├── clinic/                 # Primary Django application configurations
│   ├── migrations/         # Database structural state files
│   ├── templates/          # HTML structures and UI components
│   ├── static/             # Layout sheets, CSS files, and frontend scripts
│   │   ├── css/
│   │   └── js/
│   ├── models.py           # Patient and relational data schemas
│   ├── views.py            # Logical controllers and routing processes
│   └── urls.py             # App-level routing declarations
│
├── clinicwebsite/          # Master project ecosystem files
│   ├── settings.py         # Global variables, databases, and middleware
│   └── urls.py             # Root level network path controllers
│
├── scripts/                # Automated environment initialization tasks
├── manage.py               # Native Django system execution tool
└── requirements.txt        # Backend dependencies and modules Manifest

📡 API & Routing Overview
System Access
-GET /login/ — Load authentication entry platform

-POST /login/ — Submit credentials for validation token authorization

-GET /logout/ — Safely clear session configurations and redirect users

Patient Directory Management
-GET /patients/ — Display responsive master patient tracking dashboard

-POST /patients/add/ — Store newly compiled client parameters inside the dataset

-GET /patients/view/:id/ — Read unique data parameters corresponding to a clinical file identification

-POST /patients/edit/:id/ — Save dynamic text revisions into structural patient profiles

Enterprise Administrative Controls
-GET /admin/ — Load the native master administration panel portal

-GET /admin/clinic/patient/ — Filter systemic overview logs with advanced query tools

🎯 Use Case
This management application is designed for medical centers, therapy clinics, and health practitioners who need a fast, low-latency mechanism to securely digitize patient intakes, process lookup data profiles instantly on-site, and manage back-office clinical operational pipelines without administrative friction.

📝 License
This project is licensed under the MIT License.
