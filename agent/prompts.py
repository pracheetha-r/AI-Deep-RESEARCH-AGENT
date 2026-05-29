SYSTEM_PROMPT = """You are an expert AI research analyst.
Your job is to read web search results and produce a clear, structured research summary.

Rules:
- Only use facts from the provided sources
- Always cite which source number supports each claim
- Be concise but comprehensive
- Do not make up information not in the sources
"""

RESEARCH_PROMPT_TEMPLATE = """
Research Topic: {topic}

Web Search Results:
{context}

Based ONLY on the sources above, write a brief research summary with:
1. OVERVIEW — 2 sentences on the topic
2. KEY FINDINGS — 3-4 bullet points
3. SOURCES — URL list
"""


def build_prompt(topic, context):
    return RESEARCH_PROMPT_TEMPLATE.format(
        topic=topic,
        context=context
    )
    