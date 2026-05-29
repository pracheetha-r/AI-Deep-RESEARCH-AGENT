import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.search_tool import search_web, format_results_for_llm
from agent.prompts import build_prompt
from agent.llm_client import call_llm


def run_research(topic):
    print(f"\n[Agent] Researching: {topic}")

    # Step 1 — search the web
    print("[Agent] Searching the web...")
    sources = search_web(topic)
    print(f"[Agent] Found {len(sources)} sources")

    # Step 2 — format results into context (this is RAG)
    context = format_results_for_llm(sources)

    # Step 3 — fill the prompt template
    prompt = build_prompt(topic=topic, context=context)

    # Step 4 — call the LLM
    print("[Agent] Calling LLM...")
    summary = call_llm(prompt)
    print("[Agent] Done!")

    # Step 5 — return structured result as a plain dict
    return {
        "topic": topic,
        "summary": summary,
        "sources": sources,
        "source_count": len(sources)
    }
    
"""The flow in plain English: User gives a topic → agent Googles it → takes those results and pastes them into the prompt → sends the full prompt to the LLM → LLM writes a summary based only on those results → agent returns everything neatly packaged.
"""