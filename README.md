# AI_Resume_Analyzer
# AI-Powered Resume Analyzer & CSV Generator using LangChain

## 📌 Project Overview
Recruiters and HR teams often receive resumes in bulk, usually as ZIP files containing multiple PDF or DOCX resumes.  
Manually reviewing and extracting information from these resumes is time-consuming, repetitive, and inconsistent.

This project automates **resume understanding and structured data extraction** using **LangChain, Prompt Templates, and Structured Output Parsers**, delivering clean, analyzable data in CSV format.

---

## 🚀 Features
- Upload a ZIP file containing multiple resumes
- Supports **PDF and DOCX** formats
- Automatically extracts resume text
- Converts unstructured text into structured information using LLMs
- Enforces a fixed schema using **TypedDict Output Parser**
- Aggregates all extracted data into a **CSV file**
- Download CSV directly from the Streamlit app

---

## ❗ Problem Statement
- HR teams struggle to analyze large volumes of resumes efficiently
- Resume formats vary widely (PDF, DOCX, layouts, fonts)
- Manual extraction of skills, links, and summaries is inconsistent
- No structured format for filtering or analytics

---

## 💡 Solution Approach
We build an **LLM-powered pipeline** using LangChain that:
1. Reads resumes from a ZIP file
2. Extracts raw text from PDF/DOCX files
3. Uses Prompt Templates to guide the LLM
4. Enforces a strict output schema using **TypedDict Structured Output Parser**
5. Stores all extracted resume data into a unified CSV file

---

## 🧠 Extracted Fields (Example)
- Full Name  
- Email  
- Phone Number  
- Skills  
- Work Experience Summary  
- Education  
- LinkedIn / GitHub Links  

*(Schema can be customized easily)*

---

## 🛠 Tech Stack
- **Python**
- **LangChain**
- **LLMs (Gemini / OpenAI compatible)**
- **Streamlit**
- **PDF & DOCX Parsing Libraries**
- **CSV Automation**

---

## 📂 Project Workflow
