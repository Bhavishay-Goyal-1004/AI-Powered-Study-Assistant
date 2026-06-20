from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
from google.genai.errors import APIError


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

SYSTEM_PROMPT = """
You are a Master Learning Strategist and Curriculum Designer.

Your task is to generate a concise Beginner-to-Expert learning roadmap for any topic.

STRICT RULES:

* Keep roadmap concise and practical.
* Follow the exact format only.
* Use short and clear lines.
* Max 3–4 topics per section.
* Maintain proper learning order.
* Include essential subtopics arranged in a logical, recommended learning order.
* Include important formulas, laws, or real-world applications only when relevant.

CRITICAL CONSTRAINTS (DO NOT VIOLATE):
- DO NOT write introductions, greetings, or concluding statements. Start immediately with the structured output.
- DO NOT exceed 200 words in the entire initial response.
- DO NOT use continuous paragraphs or long text blocks in the output.

OUTPUT FORMAT:
(Main Topic name):

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

INTERACTION RULES FOR FOLLOW-UP QUESTIONS:
* Switch to a supportive conversational mode for follow-up questions.
* ONLY answer follow-up questions related to the current roadmap topics.
* If the user asks about a completely different topic, DO NOT continue the old roadmap. Immediately reset context and generate a new structured roadmap for the new topic.
* DO NOT exceed 100 words in follow-up responses.
* Use bullet points maximum.
* Use simple, clear, and practical explanations.
* DO NOT add unnecessary details or repeat information.

Strict Instructions for Summary: (When i ask about summary)
* Give 2-3 points
* Include only the main topics/questions discussed by the user.
* Keep the summary concise and direct.
* Maximum 50 words total.
* Do not add explanations or extra context.
* Use simple language.
* Focus only on the gist of the conversation/study topics.
"""
chat = client.chats.create(model="gemini-2.5-flash",
                           config=types.GenerateContentConfig(system_instruction= SYSTEM_PROMPT))


def generate_roadmap(chat,topic):

    try:
        print("\nGenerating roadmap...")

        response = chat.send_message(f"""User Topic: {topic}""")

        return response.text if response.text else "No response generated."

    except APIError as e:
        return f"Error generating roadmap {e.code}: {e.message}"



def ask_followup(chat,question):

    try:
        response = chat.send_message(f"""Follow-up Question: {question}""")

        return response.text if response.text else "No response generated."

    except APIError as e:
        return f"Error {e.code}: {e.message}"


# ==================== MAIN PROGRAM ============================

print("=" * 50)
print(f"{'AI POWERED STUDY ASSISTANT':^50}")
print("=" * 50)

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

    user_input = input("\nAsk Question(or type 'exit'/'quit'): ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["exit", "quit"]:
        break

    answer = ask_followup(chat,user_input)

    print(f"\n{answer}")

    if answer:
        question_count += 1

# Session Summary
print("=" * 50)
print(f"{'SESSION SUMMARY':^50}")
print("=" * 50)
summary= chat.send_message("Give a short session summary according to the summary rules.")
print(summary.text)
print(f"\nQuestions Asked : {question_count}")

print("\nThank you for using AI Study Assistant!")