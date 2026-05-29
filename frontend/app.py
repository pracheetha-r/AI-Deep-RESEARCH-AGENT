import streamlit as st
import requests

st.set_page_config(page_title="AI Research Assistant", page_icon="🔬", layout="wide")

API_URL = "http://localhost:8000"


def call_api(topic):
    try:
        response = requests.post(
            f"{API_URL}/research",
            json={"topic": topic},
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Backend not running. Start it with: uvicorn api.main:app --reload")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None


st.title("🔬 AI Research Assistant")
st.caption("Enter a topic → AI searches the web → returns a structured summary")
st.divider()

col1, col2 = st.columns([4, 1])
with col1:
    topic = st.text_input("Topic", placeholder="e.g. quantum computing breakthroughs 2025", label_visibility="collapsed")
with col2:
    go = st.button("Research ↗", type="primary", use_container_width=True)

st.caption("Try: `AI chip wars 2025`  |  `CRISPR gene therapy`  |  `India startup funding 2025`")
st.divider()

if go and topic:
    with st.spinner("Searching and generating summary..."):
        result = call_api(topic)
    if result:
        st.session_state["result"] = result

if "result" in st.session_state:
    r = st.session_state["result"]
    st.subheader(f"Topic: {r['topic']}")
    st.metric("Sources used", r["source_count"])
    st.markdown(r["summary"])

    st.sidebar.header("Sources")
    for i, s in enumerate(r["sources"], 1):
        with st.sidebar.expander(f"Source {i}"):
            st.write(f"**{s['title']}**")
            st.write(s["url"])
            st.write(s["snippet"][:200] + "...")

    with st.expander("Raw JSON"):
        st.json(r)
else:
    st.info("Enter a topic above to get started.")