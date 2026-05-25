# 🚀 `README.md` FOR YOUR LATEST AI HRMS PROJECT

Create/update:

```text id="u6t0n5"
README.md
```

Paste this COMPLETE content 👇

````md
# 🚀 NeuroHR AI — AI Powered HRMS System

NeuroHR AI is a modern AI-powered Human Resource Management System (HRMS) built using Python, Streamlit, Flask, SQLite, and AI integrations.

The platform provides:

- Employee Management
- Secure Attendance System
- AI Resume Screening
- AI HR Chatbot
- Payroll & Payslip Generation
- Dashboard Analytics
- Check-In / Check-Out System

This project was built as a full-stack AI-powered HRMS platform for hackathons, portfolio projects, and real-world HRMS learning.

---

# 🌟 Features

## 👨‍💼 Employee Management

- Add Employees
- Auto-generate Employee IDs
- Secure PIN generation
- Persistent database storage
- Duplicate employee prevention

---

## 📅 Attendance Management

### Secure Attendance System

Employees can mark attendance only if:

- Employee ID matches
- Secret PIN matches

### Check-In / Check-Out

- One check-in per day
- One check-out per day
- Prevent duplicate attendance
- Track check-in/check-out time

---

## 📊 Dashboard Analytics

Dashboard displays:

- Total Employees
- Attendance Count
- Department Distribution
- Recent Attendance Records
- Real-time analytics

---

## 🤖 AI Resume Screening

Upload resume PDFs and compare with Job Description.

### AI Features

- PDF resume extraction
- Resume text parsing
- AI similarity matching
- Candidate scoring

---

## 🤖 AI HR Chatbot

Employees can ask HR-related questions such as:

- Leave policy
- Payroll queries
- HR policies
- Company guidelines

Powered using OpenAI APIs.

---

## 💰 Payroll Management

Generate professional PDF payslips with:

- Employee Details
- Salary Breakdown
- HRA
- Bonus
- Tax Deductions
- PF Deductions
- Net Salary

Downloadable PDF format.

---

# 🏗️ System Architecture

```text
User
 ↓
Streamlit Frontend
 ↓
Business Logic
 ↓
SQLite Database
 ↓
AI Modules / Payroll Engine
```

---

# 📂 Project Structure

```text
ai_hrms/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── frontend/
│   ├── __init__.py
│   │
│   └── pages/
│       ├── __init__.py
│       ├── dashboard.py
│       ├── employees.py
│       ├── recruitment.py
│       ├── payroll.py
│       ├── attendance.py
│       └── chatbot.py
│
├── backend/
│   ├── __init__.py
│   │
│   └── database/
│       ├── __init__.py
│       └── db.py
│
├── ai_modules/
│   ├── __init__.py
│   ├── resume_screening.py
│   ├── chatbot.py
│   ├── employee_prediction.py
│   └── interview_analyzer.py
│
└── uploads/
```

---

# ⚙️ Tech Stack

# 🖥️ Frontend

- Streamlit

---

# 🔧 Backend

- Flask
- Python

---

# 🗄️ Database

- SQLite

---

# 🤖 AI / ML

- OpenAI API
- NLP-based Resume Matching
- AI HR Assistant

---

# 📊 Data Visualization

- Plotly
- Pandas

---

# 📄 PDF Processing

- pdfplumber
- reportlab

---

# 🔐 Authentication Logic

- Employee ID
- Secret PIN Verification

---

# ☁️ Deployment

- Streamlit Community Cloud
- GitHub

---

# 📦 Python Libraries Used

```text
streamlit
flask
pandas
numpy
plotly
pdfplumber
reportlab
python-dotenv
openai
requests
sqlite3
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Thejas-babu/ai_hrms.git
```

---

## 2️⃣ Navigate to Project

```bash
cd ai_hrms
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 🚀 Deployment

The application is deployed using:

- Streamlit Community Cloud
- GitHub Integration

---

# 📸 Application Modules

## 📊 Dashboard

- Real-time analytics
- Employee insights
- Attendance reports

---

## 👨‍💼 Employee Management

- Add employee
- Auto Employee ID generation
- Secret PIN generation

---

## 📅 Attendance System

- Secure check-in/check-out
- One attendance per day
- Attendance tracking

---

## 🤖 AI Recruitment

- Resume PDF upload
- Resume scoring
- Candidate matching

---

## 💰 Payroll System

- Generate PDF payslip
- Download payslip
- Salary breakdown

---

# 🔥 Future Enhancements

- Login Authentication
- Role-Based Access Control
- Leave Management System
- AI Attrition Prediction
- Email Notifications
- Face Recognition Attendance
- Cloud Database Integration
- Employee Performance Analytics

---

# 🏆 Project Highlights

✅ AI Powered HRMS  
✅ Secure Attendance System  
✅ Professional Payroll Module  
✅ AI Resume Screening  
✅ Interactive Dashboard  
✅ Full Stack Python Application  
✅ Deployment Ready  
✅ Modular Architecture  

---

# 👨‍💻 Author

Developed by:

## Hemanth D

AI/ML & Full Stack Enthusiast

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
````
