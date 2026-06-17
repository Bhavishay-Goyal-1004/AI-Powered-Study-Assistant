from google import genai
from dotenv import load_dotenv
import os
import time


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

Keep the roadmap compact and practical.
Use ONLY the exact format provided.
Keep every line short and crisp.
Limit each section to 3–6 topics maximum.
Purpose must be 1 short sentence only.
Do not write paragraphs.
Do not give long explanations.
Do not add extra sections.
Do not repeat topics.
Do not use motivational text.
Do not exceed 250 words total.

OUTPUT FORMAT:

BEGINNER
Purpose :
Topics :
• Topic 1
• Topic 2
• Topic 3

ELEMENTARY
Purpose :
Topics :
• Topic 1
• Topic 2
• Topic 3

INTERMEDIATE
Purpose :
Topics :
• Topic 1
• Topic 2
• Topic 3

ADVANCED
Purpose :
Topics :
• Topic 1
• Topic 2
• Topic 3

EXPERT
Purpose :
Topics :
• Topic 1
• Topic 2
• Topic 3

COMMON MISTAKES
• Mistake 1
• Mistake 2
• Mistake 3

================================
Mastery Flow : Beginner → Expert
================================
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

def print_separator():
    print("=" * 50)


def generate_roadmap(topic):

    try:
        print("\nGenerating roadmap...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            System Instructions:
            {ROADMAP_PROMPT}

            User Topic:
            {topic}
            """
        )

        return response.text

    except Exception as e:
        return f"Error generating roadmap: {e}"



def ask_followup(chat_history, question):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            System Instructions:
            {FOLLOWUP_PROMPT}

            Previous Conversation:
            {chat_history}

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

# Chat History
chat_history = []

roadmap = generate_roadmap(topic)

print(f"\n{roadmap}")

chat_history.append(f"User selected topic: {topic}")
chat_history.append(f"Roadmap Generated:\n{roadmap}")

print("\nYou can now ask follow-up questions.")
print("Type 'exit' or 'quit' to end.\n")

question_count = 0

while True:

    user_input = input("\nAsk Question(or type 'exit'): ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["exit", "quit"]:
        break

    answer = ask_followup(chat_history, user_input)

    print(f"\n{answer}")

    chat_history.append(f"User: {user_input}")
    chat_history.append(f"Assistant: {answer}")

    question_count += 1

# Session Summary
print_separator()
print(f"{'SESSION SUMMARY':^50}")
print_separator()

print(f"Topic Studied   : {topic}")
print(f"Questions Asked : {question_count}")

print("\nThank you for using AI Study Assistant!")