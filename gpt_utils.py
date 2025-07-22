from utils import format_conversation
from config import client

def classify_conversation(history):
    formatted = format_conversation(history)

    prompt = f"""
Below is a conversation between a user and an HR assistant bot. Determine whether the user's issue was resolved or not.

Then, generate a brief title summarizing the main topic of the conversation.

Return the result in this format:
Resolved: Conversation Title
or
Unresolved: Conversation Title

Conversation:
{formatted}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content.strip()
