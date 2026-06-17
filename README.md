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
BEGINNER → EXPERT ROADMAP : PYTHON
==================================================

BEGINNER : Python Basics
Purpose : Learn syntax and fundamentals

ELEMENTARY : Functions & OOP
Purpose : Build structured programs

INTERMEDIATE : Libraries & APIs
Purpose : Work with real-world projects

ADVANCED : Frameworks & Optimization
Purpose : Develop scalable applications

EXPERT : System Design & AI Integration
Purpose : Build production-level systems
```

---


# Author

Developed using Python and Gemini AI.
