# 🔐 Sensitive Data Detection & Compliance Assistant

An AI-powered document security and compliance application that detects sensitive information from **PDF, TXT, and CSV** files, classifies compliance risk, generates AI-powered security summaries using **Google Gemini**, supports document question answering, masks sensitive data, and generates downloadable PDF compliance reports.

---

## 📌 Project Overview

Organizations frequently store confidential information in resumes, employee records, financial documents, and business reports. Sharing these documents without proper inspection can expose sensitive information.

This application automatically analyzes uploaded documents, detects confidential information, evaluates security risk, and provides AI-powered compliance recommendations.

---

# ✨ Features

## 📄 Document Upload

Supports:

- PDF
- TXT
- CSV

---

## 🔍 Sensitive Data Detection

Detects:

- Email Addresses
- Phone Numbers
- Aadhaar Numbers
- PAN Numbers
- Credit Card Numbers
- Employee IDs
- API Keys
- Passwords
- IFSC Codes
- Confidential Keywords

---

## 🔒 Data Masking

Sensitive information is masked before being displayed.

Example:

| Original | Masked |
|----------|---------|
| keshriaditi01@gmail.com | ***********01@gmail.com |
| 7541979140 | ******9140 |
| ABCDE1234F | ******234F |
| 1234 5678 9012 | ********9012 |

---

## ⚠️ Risk Classification

Documents are automatically classified into:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

using a rule-based scoring engine.

---

## 🤖 AI Compliance Analysis

Powered by **Google Gemini**.

Generates:

- Compliance Summary
- Security Risks
- Suggested Remediation

---

## 💬 Question Answering

Users can ask questions about the uploaded document.

Example:

- How many email addresses are present?
- Does this document contain PAN?
- Summarize this document.
- What security risks are identified?

---

## 📄 PDF Report Generation

Generate downloadable compliance reports containing:

- Risk Level
- Detected Sensitive Data
- AI Compliance Summary
- Security Risks
- Recommendations

---

## 🎨 Professional Dashboard

- Bootstrap UI
- Responsive Design
- Detection Summary Cards
- Risk Classification Panel
- AI Analysis Panel
- Document Viewer

---

# 🏗 Architecture

```text
                User

                  │

          Upload Document

                  │

                  ▼

          Flask Backend

                  │

        ┌─────────┴──────────┐

        ▼                    ▼

Document Reader      Sensitive Data Detector

(PDF/TXT/CSV)            (Regex)

        │

        ▼

Risk Classification Engine

        │

        ▼

Google Gemini AI

        │

        ▼

AI Summary + Question Answering

        │

        ▼

PDF Report Generator

        │

        ▼

Bootstrap Dashboard
```

---

# 🧠 AI / ML Approach

## Rule-Based Detection

Sensitive information such as:

- Email
- Phone
- PAN
- Aadhaar
- IFSC
- Credit Card

is detected using **Regular Expressions (Regex)** because these patterns are deterministic and highly accurate.

---

## Risk Classification

A rule-based scoring model assigns weights to different sensitive data.

Example:

| Data Type | Weight |
|------------|---------|
| Aadhaar | 5 |
| Credit Card | 5 |
| Password | 5 |
| API Key | 5 |
| PAN | 3 |
| IFSC | 3 |
| Employee ID | 2 |
| Email | 1 |
| Phone | 1 |

Total score determines:

- Low Risk
- Medium Risk
- High Risk

---

## AI Integration

Google Gemini is used for:

- Compliance Summary
- Security Risk Analysis
- Suggested Remediation
- Document Question Answering

Prompt Engineering ensures Gemini answers only from the uploaded document.

---

# 🛠 Tech Stack

## Frontend

- HTML5
- CSS3
- Bootstrap 5

## Backend

- Flask

## AI

- Google Gemini API

## Document Processing

- pdfplumber
- pandas

## PDF Generation

- ReportLab

## Environment Management

- python-dotenv

## Language

- Python 3

---

# 📂 Project Structure

```text
Sensitive-Data-Detection-Compliance-Assistant/

│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── uploads/
├── reports/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── answer.html
│
├── static/
│
├── utils/
│   ├── detector.py
│   ├── classifier.py
│   ├── masking.py
│   ├── pdf_reader.py
│   ├── txt_reader.py
│   ├── csv_reader.py
│   ├── gemini_ai.py
│   ├── qa.py
│   └── pdf_report.py
│
└── sample_files/
```

---

# ⚙️ Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/Sensitive-Data-Detection-Compliance-Assistant.git
```

Move into project

```bash
cd Sensitive-Data-Detection-Compliance-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🚀 How It Works

1. Upload document
2. Extract text
3. Detect sensitive information
4. Mask detected values
5. Classify risk
6. Generate AI compliance summary
7. Ask questions about the document
8. Download PDF report

---

# 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/

home.png

dashboard.png

risk.png

qa.png

report.png
```

---

# 🧪 Sample Questions

- How many email addresses are present?
- Does this document contain PAN?
- Summarize this document.
- What security risks exist?
- Does this document contain confidential information?

---

# ⚠️ Challenges Faced

- Extracting text accurately from different PDF layouts.
- Preserving document formatting.
- Designing reliable Regex patterns.
- Integrating Google Gemini securely.
- Managing document state for AI Question Answering.
- Protecting sensitive information through masking.
- Generating professional PDF compliance reports.

---

# 🔮 Future Improvements

- OCR support for scanned PDFs
- Multi-document analysis
- ChromaDB / FAISS based RAG
- User authentication
- Role-Based Access Control
- Audit logging
- Docker support
- Cloud Deployment
- Compliance Score Dashboard
- Export to Word and Excel
- Real-time monitoring

---

# 📈 Skills Demonstrated

- Python
- Flask
- REST Concepts
- Regular Expressions
- Document Processing
- AI Integration
- Prompt Engineering
- Cyber Security
- Data Privacy
- Bootstrap
- Report Generation
- Software Architecture

---

# 👩‍💻 Author

**Aditi Kumari**

B.Tech – Computer Science & Engineering

GitHub: https://github.com/Aditi-keshri

---

# 📜 License

This project is developed for educational and assessment purposes.