import os

from dotenv import load_dotenv
import google.generativeai as genai

from drafting.prompts import MEMO_TEMPLATE
from feedback.feedback_retriever import load_feedback

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_memo(evidence):

    evidence_text = ""

    for item in evidence:

        evidence_text += f"""

Source: {item['source']}
Page: {item['page']}

Content:
{item['text']}

"""

    feedback_examples = load_feedback()

    feedback_text = ""

    for item in feedback_examples:

        feedback_text += f"""

Generated:
{item['generated']}

Edited:
{item['edited']}


"""

    prompt = MEMO_TEMPLATE.format(
        evidence=evidence_text
    )

    if feedback_text:

        prompt += f"""

Previous Operator Edits:

{feedback_text}

When appropriate, follow similar writing style and phrasing patterns.
"""

    response = model.generate_content(
        prompt
    )

    return response.text