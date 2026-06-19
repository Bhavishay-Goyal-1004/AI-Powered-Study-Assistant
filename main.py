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
* Max 250 words total.

OUTPUT FORMAT:

BEGINNER
Topics:
• Topic — Description

INTERMEDIATE
Topics:
• Topic — Description

ADVANCED
Topics:
• Topic — Description

EXPERT
Topics:
• Topic — Description

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

Provide concise, accurate, and structured answers for any topic.

STRICT RULES:

Maximum 150 words.
Use short and clear sentences.
Keep answers practical and relevant.
Maximum 3–5 bullet points.
Avoid unnecessary details.
Do not write long paragraphs.
Do not repeat information.
Focus only on the user's question.
Use simple language whenever possible. 

OUTPUT FORMAT:

Overview:
<short explanation>

Important Points:
• Point 1
• Point 2
• Point 3

Example / Use Case:



Quick Tip:
<1 useful insight or shortcut>

SPECIAL INSTRUCTIONS:

For coding questions: include syntax/examples briefly.
For comparison questions: highlight key differences only.
For theoretical topics: explain core concepts only(formula if any).
For step-based questions: provide concise steps.
If an example is not relevant, skip it.
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