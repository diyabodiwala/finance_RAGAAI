import openai
import os

# Use the environment variable set in Render dashboard
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(context, question):
    prompt = f"Context: {context}\nQuestion: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
