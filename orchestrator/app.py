from fastapi import FastAPI
from agents import api_agent, lang_agent

app = FastAPI()  # This line must be here

@app.get("/brief")
def brief():
    try:
        market_data = api_agent.get_asia_tech_stocks()
        context = str(market_data)
        response = lang_agent.ask_llm(context, "risk exposure in Asia tech stocks and earnings surprises")
        return {"brief": response}
    except Exception as e:
        return {"error": str(e)}
