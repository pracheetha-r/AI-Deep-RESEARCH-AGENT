import streamlit as st
import requests

def render_dashboard(api_url, sign_out_callback):
    # --- RENDER SIDEBAR USER PROFILE ---
    user = st.session_state["user"]
    
    st.markdown("""
        <style>
        .profile-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .profile-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: 2px solid #a855f7;
            object-fit: cover;
        }
        
        .profile-info {
            flex: 1;
            min-width: 0;
        }
        
        .profile-name {
            color: #f1f5f9;
            font-weight: 600;
            font-size: 14px;
            margin: 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        .profile-email {
            color: #64748b;
            font-size: 12px;
            margin: 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .profile-badge {
            background: rgba(168, 85, 247, 0.15);
            color: #c084fc;
            font-size: 10px;
            padding: 2px 6px;
            border-radius: 20px;
            border: 1px solid rgba(168, 85, 247, 0.3);
            display: inline-block;
            margin-top: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar profile card
    st.sidebar.markdown(f"""
        <div class="profile-card">
            <img class="profile-avatar" src="{user['picture']}" alt="Avatar">
            <div class="profile-info">
                <p class="profile-name">
                    {user['name']}
                    <span style="color: #10b981; font-size: 14px;">✔</span>
                </p>
                <p class="profile-email">{user['email']}</p>
                <span class="profile-badge">{user['role']}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Sign out button inside sidebar
    if st.sidebar.button("🔒 Sign Out from Session", use_container_width=True, type="secondary"):
        sign_out_callback()
        
    st.sidebar.divider()
    
    # --- YOUR EXACT API INTERACTION FUNCTION ---
    def call_api(topic):
        try:
            response = requests.post(
                f"{api_url}/research",
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

    # --- YOUR EXACT MAIN PAGE LAYOUT ---
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

    # --- YOUR EXACT RESULT RENDERING LOGIC ---
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