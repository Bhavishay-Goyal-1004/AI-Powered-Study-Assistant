from google import genai
from dotenv import load_dotenv
import os
from google.genai import types


# Loading Environment Variables
load_dotenv()

# Loading API KEY
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("API Key not found!")
    exit()

# Gemini Client
client = genai.Client(api_key=API_KEY)

# System Prompts

ROADMAP_PROMPT = """
You are a Master Learning Strategist and Curriculum Designer.

Your task is to generate a concise Beginner-to-Expert learning roadmap for any topic.

STRICT RULES:

* Keep roadmap concise and practical.
* Follow the exact format only.
* Use short and clear lines.
* Max 3–4 topics per section.
* Add 1-line description for each topic.
* Keep purpose to 1 sentence.
* Maintain proper learning order.
* No paragraphs or long explanations.
* No extra or repeated topics.
* No motivational text.
* Max 200 words total.
* Include important formulas, laws, or real-world applications only when relevant.

OUTPUT FORMAT:

BEGINNER
Topics:
• Topic — 1 line purpose/use

INTERMEDIATE
Topics:
• Topic — 1 line purpose/use

ADVANCED
Topics:
• Topic — 1 line purpose/use

EXPERT
Topics:
• Topic — 1 line purpose/use

LEARNING ORDER
Beginner → Intermediate → Advanced → Expert

COMMON MISTAKES
• Mistake 1
• Mistake 2
• Mistake 3

"""


# Follow-up Prompt
FOLLOWUP_PROMPT = """
You are an Expert AI Assistant.

Provide concise, accurate, and well-structured answers.

RULES:

* Maximum 100 words.
* Use simple and clear language.
* Keep sentences short.
* Focus only on the user's question.
* Avoid unnecessary details.
* Do not repeat information.
* Use 3–5 bullet points maximum.
* Prefer practical explanations.
* Avoid long paragraphs.

SPECIAL INSTRUCTIONS:
* Coding:
  * Give short syntax/examples only when needed.
  * Explain only the important logic.

* Comparisons:
  * Show key differences only.
  * Keep comparisons compact.

* Theory:
  * Explain core concepts only.
  * Include formulas only if important.

* Step-by-step Questions:
  * Provide concise ordered steps.

* Examples:
  * Add examples only when useful.
  * Skip irrelevant examples.

OUTPUT STYLE:
* Clear
* Compact
* Practical
* Easy to scan
"""

chat = client.chats.create(model="gemini-2.5-flash")

def print_separator():
    print("=" * 50)


def generate_roadmap(chat,topic):

    try:
        print("\nGenerating roadmap...")

        response = chat.send_message(f"""
            System Instructions:
            {ROADMAP_PROMPT}

            User Topic:
            {topic}
            """
        )
        

        return response.text

    except Exception as e:
        return f"Error generating roadmap: {e}"



def ask_followup(chat,question):

    try:
        response = chat.send_message(f"""
            System Instructions:
            {FOLLOWUP_PROMPT}

            User Question:
            {question}
            """
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# ==================== MAIN PROGRAM ============================

print_separator()
print(f"{'AI POWERED STUDY ASSISTANT':^50}")
print_separator()

topic = input("\nEnter Topic to Study: ").strip()

if not topic:
    print("Topic cannot be empty!")
    exit()


roadmap = generate_roadmap(chat,topic)

print(f"\n{roadmap}")


print("\nYou can now ask follow-up questions.")
print("Type 'exit' or 'quit' to end.\n")

question_count = 0

while True:

    user_input = input("\nAsk Question(or type 'exit'): ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["exit", "quit"]:
        break

    answer = ask_followup(chat,user_input)

    print(f"\n{answer}")


    question_count += 1

# Session Summary
print_separator()
print(f"{'SESSION SUMMARY':^50}")
print_separator()

print(f"Topic Studied   : {topic}")
print(f"Questions Asked : {question_count}")

print("\nThank you for using AI Study Assistant!")