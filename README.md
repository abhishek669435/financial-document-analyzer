📊 Financial Document Analyzer API
An AI-powered backend system that analyzes financial documents and generates structured investment insights using FastAPI and CrewAI.

This project demonstrates strong debugging skills, AI agent orchestration, structured prompt engineering, and backend API development.

🚀 Project Overview
The Financial Document Analyzer API enables users to:

Upload financial documents (TXT format)

Automatically extract key financial insights

Generate structured investment analysis

Store analysis results in a database

Access results via REST API

The system uses a CrewAI agent configured as a professional financial analyst to evaluate documents and provide investment recommendations.

System Architecture:-
Client (Swagger / API Request)
↓
FastAPI Backend
↓
CrewAI Agent (Financial Analyst)
↓
Task (Structured Financial Analysis Instructions)
↓
Tool (Document Reader)
↓
SQLite Database (Stores Results)
↓
JSON API Response

Tech Stack
Python 3.11

FastAPI

CrewAI

SQLAlchemy

SQLite

Uvicorn

Pydantic v2

🔧 Bugs Identified & Fixed
During debugging and system migration, the following issues were identified and resolved:

Dependency conflicts between CrewAI and OpenAI versions.

Import errors due to CrewAI API structure changes.

Tool validation errors (BaseTool required instead of raw functions).

Pydantic v2 strict validation failures.

Incorrect usage of .get() on Crew kickoff result.

Missing python-multipart dependency for file uploads.

Agent configuration mismatches.

Task validation errors due to incorrect tool references.

Runtime internal server errors during document processing.

All issues were successfully resolved, and the application now runs without runtime errors.

Prompt Engineering Improvements
The financial analysis task was enhanced to:

Extract revenue, expenses, and net profit

Identify financial strengths

Detect risks and red flags

Provide a structured investment recommendation

Return output in clearly defined sections:

Summary

Key Metrics

Risk Assessment

Investment Recommendation

This improves output reliability, structure, and professional quality.

📦 Installation & Setup
1️⃣ Clone the Repository
Code

git clone <your-repository-url>
cd financial-document-analyzer
2️⃣ Create Virtual Environment
Windows:

Code

python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
Code

pip install -r requirements.txt
pip install python-multipart
pip install sqlalchemy
4️⃣ Run the Server
Code

uvicorn main:app --reload
Server runs at:

Code

http://127.0.0.1:8000
Swagger UI:

Code

http://127.0.0.1:8000/docs
📌 API Endpoints
🔹 GET /
Health check endpoint.

Response:

Code

{
  "message": "Financial Document Analyzer API is running"
}
🔹 POST /analyze
Uploads and analyzes a financial document.

Request Type:

Code

multipart/form-data
Parameters:

file → Financial document (.txt)

query → Analysis instruction

Example Response:

Code

{
  "analysis": "Summary: ... Key Metrics: ... Risk Assessment: ... Investment Recommendation: ..."
}
💾 Database Integration (Bonus Feature)
All analysis results are stored in a local SQLite database:

Code

analysis.db
Stored Fields:

ID

Filename

Analysis Result

This enables:

Persistent storage

Audit tracking

Future analytics integration

🔮 Future Improvements
Redis-based queue worker for asynchronous processing

PDF parsing support

Financial ratio automation

React frontend dashboard

Authentication & user management

🎯 Key Skills Demonstrated
AI Agent Architecture (CrewAI)

Structured Prompt Engineering

FastAPI Backend Development

Debugging Complex Dependency Conflicts

Pydantic Validation Handling

Database Integration with SQLAlchemy

REST API Design

Production-Ready Backend Structure

Author
Abhishek Sahay