#  Resume Matcher — Deep Learning–Powered Resume Evaluation System

**Resume Matcher** is a deep learning–driven web application that evaluates how well a candidate’s resume aligns with a job description.  
It leverages **Large Language Models (LLMs)**, specifically **Google Gemini 2.5 Flash**, to perform **semantic understanding**, **skill extraction**, and **resume–JD alignment scoring**, providing detailed suggestions for improvement.

---

## Project Overview

Recruiters often spend hours manually reviewing resumes for open positions. Traditional keyword-based matching systems fail to capture **contextual relevance**, semantic relationships between skills, and overall fit.  

This project uses **state-of-the-art LLMs** to automate and enhance resume evaluation, enabling:

- Intelligent **semantic matching** between resumes and job descriptions  
- Automated **skill gap detection**  
- **Actionable feedback** for candidates  

It demonstrates **real-world application of deep learning in NLP**, combining AI reasoning with structured evaluation.

---

## 🚀 Features

- 🧾 **Resume Upload**: Supports PDF and DOCX files  
- 💬 **Job Description Input**: Simple text box for pasting JD  
- 🧠 **AI-Powered Evaluation**: Uses Google Gemini 2.5 Flash for contextual analysis  
- 📊 **Section Scoring**: Skills, experience, projects, education, and certifications  
- 📝 **Missing Items Detection**: Highlights missing skills, experience, and responsibilities  
- 💡 **Actionable Suggestions**: Personalized tips to improve resume alignment  
- 🌐 **Cross-Platform Deployment**: Works locally, on Render (backend), and Vercel (frontend)  

---

## Deep Learning / NLP Pipeline

| Stage | Description | Technology |
|-------|-------------|-----------|
| **Text Extraction** | Extracts structured text from resumes and JDs | `pdfminer.six`, `python-docx` |
| **Preprocessing** | Cleans and normalizes text for AI input | Python NLP preprocessing |
| **Embedding & Semantic Analysis** | Converts text into embeddings for semantic matching | Google Gemini 2.5 Flash |
| **Evaluation & Scoring** | Computes match scores and identifies missing items | LLM reasoning and scoring logic |
| **Output Generation** | Produces structured JSON with scores and suggestions | Flask API |

---

## 🧰 Tech Stack

### **AI / Deep Learning**
- Google Gemini 2.5 Flash (LLM for evaluation)  
- Python (NumPy, JSON handling)  
- PDF/DOCX parsing (`pdfminer.six`, `python-docx`)  

### **Backend**
- Flask (Python 3.13)  
- Gunicorn WSGI server  
- Flask-CORS for cross-origin requests  
- Hosted on **Render**

### **Frontend**
- React + Vite  
- TailwindCSS for responsive UI  
- Axios for API requests  
- Hosted on **Vercel**


