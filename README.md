
# Multi-Agent Finance Assistant

This is a voice-enabled financial assistant that responds to queries like:
> "What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?"

## Features
- Voice Input (STT with Whisper)
- Text-to-Speech Output
- Market data from Yahoo Finance
- Document scraping from SEC
- Retrieval-Augmented Generation (FAISS)
- OpenAI LLM integration
- Streamlit front-end
- FastAPI microservice backend

## Run Locally

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run FastAPI Backend
```bash
uvicorn orchestrator.app:app --reload
```

### Step 3: Run Streamlit App
```bash
streamlit run streamlit_app/app.py
```

## Deployment
You can deploy this on [Streamlit Cloud](https://share.streamlit.io) or Render.com.

## Architecture Diagram
See `docs/architecture.png`
