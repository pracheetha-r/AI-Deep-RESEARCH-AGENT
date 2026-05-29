from ddgs import DDGS
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import MAX_SEARCH_RESULTS


def search_web(query):
    results = []
    with DDGS() as ddgs:
        for result in ddgs.text(query, max_results=MAX_SEARCH_RESULTS):
            results.append({
                "title":   result.get("title", ""),
                "url":     result.get("href", ""),
                "snippet": result.get("body", "")
            })
    return results


def format_results_for_llm(results):
    if not results:
        return "No search results found."

    formatted = []
    for i, r in enumerate(results, 1):
        snippet = r['snippet'][:300]
        formatted.append(
            f"[Source {i}]\n"
            f"Title: {r['title'][:100]}\n"
            f"URL: {r['url']}\n"
            f"Content: {snippet}\n"
        )
    return "\n---\n".join(formatted)


'''What it is: The search tool — gives your agent the ability to look things up on the web. It takes a query, hits DuckDuckGo, and returns a list of results.
Why this way: DuckDuckGo needs no API key, which means you can search for free. The results come back as a list of dicts — each one has a title, URL, and snippet of text.
What RAG means here: RAG = Retrieval Augmented Generation. You retrieve real web content, then augment your LLM prompt with it. The LLM doesn't search the web itself — your code does, then hands it the results. That's the core trick of this whole project.'''