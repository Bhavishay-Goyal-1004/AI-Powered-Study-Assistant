# AI Powered Study Assistant

An AI-based CLI Study Assistant built using Python and the Gemini API.
This project generates a Beginner → Expert roadmap for any topic and also answers follow-up study questions interactively.

---

# Features

* Generates structured learning roadmaps
* Beginner → Expert progression
* Interactive follow-up question support
* Compact AI-generated study guidance
* Session history tracking
* Gemini API integration
* Environment variable support using `.env`

---

# Technologies Used

* Python
* Gemini API
* google-genai
* python-dotenv

---

# Project Structure

```bash
AI-Powered-Study-Assistant/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---
## Prompt Design Questions

### 1. What role did you assign in your system prompt, and why did you choose that framing?

The system prompt assigns the role **"Master Learning Strategist and Curriculum Designer."**
This framing was chosen to make the AI behave like an expert educator who creates structured and progressive learning roadmaps. It helps the model focus on skill progression, concise planning, and practical topic sequencing instead of giving random or overly detailed explanations.

---

### 2. What format did you specify for the study plan output, and how did you enforce it in the prompt?

The output format was divided into four learning stages:

* Beginner
* Intermediate
* Advanced
* Expert

Each stage contains:

* A short purpose statement
* A limited list of topics

The format was enforced using strict instructions such as:

* “Use ONLY the exact format provided”
* “Do not add extra sections”
* “Limit each section to 3–6 topics maximum”
* “Do not write paragraphs”
* “Do not exceed 250 words total”

These constraints ensured the response stayed structured, compact, and consistent.

---

### 3. What happens if you remove the system prompt entirely — how does the output change?

Without the system prompt, the AI generates a much less structured response and often gives long explanations instead of a concise roadmap. The learning stages become inconsistent, formatting changes, and the output may include unnecessary details or motivational text.

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Bhavishay-Goyal-1004/AI-Powered-Study-Assistant.git
```

## 2. Move Into Project Folder

```bash
cd AI-Powered-Study-Assistant
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Required Libraries

```text
google-genai
python-dotenv
```

---

# Setup API Key

Create a `.env` file in the project folder.

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Run the Program

```bash
python main.py
```

---

# How It Works

1. User enters a study topic
2. AI generates a Beginner → Expert roadmap
3. User can ask follow-up questions
4. AI responds briefly with study guidance
5. Session statistics are displayed at the end

---

# Example Output

```text
==================================================
            AI POWERED STUDY ASSISTANT            
==================================================

Enter Topic to Study: SQL

Generating roadmap...

SQL:

BEGINNER
Topics:
• Introduction to Databases — Understand tables, rows, columns, and data types.
• Basic Querying (SELECT, FROM, WHERE) — Retrieve specific data from tables.
• Data Manipulation (INSERT, UPDATE, DELETE) — Add, modify, and remove records.
• Constraints (PRIMARY KEY, FOREIGN KEY) — Enforce data integrity and relationships.

INTERMEDIATE
Topics:
• JOIN Operations (INNER, LEFT, RIGHT) — Combine data from multiple tables.
• Aggregate Functions (COUNT, SUM, AVG) & GROUP BY — Perform calculations on grouped data.
• Subqueries — Nested queries for complex data retrieval.
• Ordering & Limiting (ORDER BY, LIMIT/OFFSET) — Sort results and control output size.

ADVANCED
Topics:
• Window Functions (ROW_NUMBER, RANK) — Perform calculations across a set of table rows related to the current row.
• Common Table Expressions (CTEs) — Define temporary, named result sets.
• Indexing & Views — Improve query performance and simplify complex queries.
• Stored Procedures & Triggers — Automate database tasks and enforce business rules.

EXPERT
Topics:
• Database Design & Normalization (1NF, 2NF, 3NF) — Structure databases efficiently to reduce redundancy.
• Query Optimization & Performance Tuning — Analyze and improve query execution speed.
• Transactions & ACID Properties — Ensure data integrity and reliability in multi-step operations.
• Advanced Data Modeling (Star/Snowflake Schema) — Design for analytical and data warehousing needs.

LEARNING ORDER
Beginner → Intermediate → Advanced → Expert

COMMON MISTAKES
• Misunderstanding JOIN types.
• Forgetting to use appropriate indexes.
• Not using `GROUP BY` correctly with aggregate functions.

You can now ask follow-up questions.
Type 'exit' or 'quit' to end.


Ask Question(or type 'exit'/'quit'): different software & languages for SQL

Different software for SQL refers to Relational Database Management Systems (RDBMS) that use SQL.

*   **RDBMS Software:**
    *   **PostgreSQL:** Open-source, powerful, feature-rich.
    *   **MySQL:** Widely used open-source, popular for web applications.
    *   **Microsoft SQL Server:** Commercial, robust for enterprise solutions.
    *   **Oracle Database:** Commercial, very powerful, often used in large enterprises.
    *   **SQLite:** Embedded database, serverless, file-based, simple.

*   **SQL Language:** SQL (Structured Query Language) is a standard. However, each RDBMS implements its own *dialect* of SQL, with minor variations in syntax or added proprietary features (e.g., `LIMIT` vs. `TOP`). The core commands (SELECT, INSERT, etc.) are largely consistent.

Ask Question(or type 'exit'/'quit'): exit
==================================================
                 SESSION SUMMARY                  
==================================================
Session Summary:
*   SQL learning roadmap (Beginner to Expert).
*   Explained different SQL software (RDBMS) and language dialects.

Questions Asked : 1

Thank you for using AI Study Assistant!
```
---


# Author

Bhavishay Goyal
