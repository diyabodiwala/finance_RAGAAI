from fastapi import FastAPI
from agents import api_agent, lang_agent

app = FastAPI()  # This line must be here

@app.get("/brief")
def brief():
    return {"brief": "✅ Service is running. Whisper and LLM are disabled for memory testing."}
