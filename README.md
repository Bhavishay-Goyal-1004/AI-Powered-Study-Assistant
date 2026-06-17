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

The output format was divided into five learning stages:

* Beginner
* Elementary
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

```txt
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

```bash
==================================================
            AI POWERED STUDY ASSISTANT            
==================================================

Enter Topic to Study: Python

Generating roadmap...

BEGINNER
Purpose : Learn foundational Python syntax and basic programming constructs.
Topics :
• Installing Python & IDE
• Variables and Data Types and Operators
• Conditional Statements (if/else)
• Loops (for/while)
• Functions

ELEMENTARY
Purpose : Understand how to organize code and work with common data structures.
Topics :
• Lists, Tuples, Dictionaries, Sets
• String Manipulation
• File I/O
• Modules and Packages
• Error Handling (try-except)

INTERMEDIATE
Purpose : Develop more robust and efficient Python applications.
Topics :
• Object-Oriented Programming (OOP)
• Decorators and Generators
• Context Managers
• Regular Expressions
• Database Interaction (SQLite)

ADVANCED
Purpose : Explore advanced concepts for performance, concurrency, and specialized tasks.
Topics :
• Concurrency (threading, multiprocessing)
• Asynchronous Programming (async/await)
• Metaclasses
• C Extensions (ctypes, Cython basics)
• Web Frameworks (e.g., Flask/Django basics)

EXPERT
Purpose : Master high-performance Python, system-level programming, and contribute to the ecosystem.
Topics :
• Performance Optimization
• Distributed Systems
• Advanced Design Patterns
• Contributing to Open Source
• Building Custom Interpreters/Tools

COMMON MISTAKES
• Misunderstanding scope (global vs. local)
• Mutable default arguments in functions
• Ignoring virtual environments
• Inefficient use of data structures
• Not writing tests

================================
Mastery Flow : Beginner → Expert
================================

You can now ask follow-up questions.
Type 'exit' or 'quit' to end.
```
---


# Author

Developed using Python and Gemini AI.
