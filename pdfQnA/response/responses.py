import os
from huggingface_hub import InferenceClient

client = InferenceClient()

def ask_llm(prompt):
    completion = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = [
            { 
                "role":"user",
                "content": prompt
            }
        ],
    )
    return completion.choices[0].message.content
def main():

    prompt = """
    You are a question answering system.

    Instructions:
    1. Answer ONLY using the provided context.
    2. If the answer is not in the context, say "I don't know".
    3. Do NOT make up information.
    4. Keep the answer concise.

    Context:
    Text formatting options to ensure proper rendering in PDF readers.

    Text Formatting Examples:
    1. Bold text is used for emphasis.
    2. Italic text can be used for titles or subtle emphasis.
    3. Strikethrough is used to show deleted text.

    Lists:
    Here's an example of an unordered list:
    Item 1
    Item 2

    This document demonstrates various formatting options that should translate well to PDF format.

    Query:
    What formatting options are available?
    """
    ans = ask_llm(prompt)
    print(ans)
if __name__ == "__main__":
    main()