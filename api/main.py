from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent.research_agent import run_research

app = FastAPI(title="AI Research Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Server is running"}


@app.post("/research")
def research(request: ResearchRequest):
    if not request.topic or len(request.topic.strip()) < 3:
        raise HTTPException(status_code=400, detail="Topic too short")
    try:
        result = run_research(request.topic.strip())
        return result
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"ERROR in /research endpoint:\n{error_details}")
        raise HTTPException(status_code=500, detail=str(e))
    
"""What it is: The FastAPI server. It exposes your agent as a URL endpoint so Streamlit (or anything else) can call it over HTTP. This is what makes your project a real backend service.
Why FastAPI: It's the fastest Python web framework, has automatic documentation at /docs, and handles JSON automatically. You define what goes in and what comes out using Python classes."""