import streamlit as st
import time
# 1. We import the render functions from the modules we created
from login import render_login_page, render_verification_loader
from dashboard import render_dashboard

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Research Assistant", page_icon="🔬", layout="wide")

API_URL = "http://localhost:8000"

# --- SESSION STATE INITIALIZATION ---
# Keeps track of whether a user has successfully signed in
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user" not in st.session_state:
    st.session_state["user"] = None

# --- OAUTH CONFIGURATION ---
# Check for client configuration settings
GOOGLE_CLIENT_ID = st.secrets.get("GOOGLE_CLIENT_ID", None)
REDIRECT_URI = "http://localhost:8501/" # Redirect target back to Streamlit app

# --- STEP 1: INTERCEPT AUTH REDIRECT (QUERY PARAMETERS) ---
# When Google redirects back to your app, it will append '?code=xxx'
query_params = st.query_params
if "code" in query_params:
    auth_code = query_params["code"]
    
    # 2. Render intermediate security handshake screen
    render_verification_loader()
    
    with st.spinner("Establishing secure session..."):
        time.sleep(1.8) # Simulate token exchange delay
        
        # When your backend OAuth route is ready, exchange the auth code here:
        # response = requests.post(f"{API_URL}/auth/google", json={"code": auth_code})
        
        # Standalone mode: securely mock the validated user details
        st.session_state["authenticated"] = True
        st.session_state["user"] = {
            "name": "Dr. Sarah Chen",
            "email": "sarah.chen@deepresearch.ai",
            "picture": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=100",
            "role": "Lead Research Fellow",
            "id_token": "mocked_jwt_token_google_oauth2_xyz123"
        }
        
    # Clear parameters to clean up browser address bar URL
    st.query_params.clear()
    st.rerun()

# --- SIGN OUT FUNCTION ---
# Wipes user session states and reruns to trigger login card view
def sign_out():
    st.session_state["authenticated"] = False
    st.session_state["user"] = None
    # Wipe past search records on logout
    if "result" in st.session_state:
        del st.session_state["result"]
    st.rerun()

# --- STEP 2: ORCHESTRATE VIEWS ---
if not st.session_state["authenticated"]:
    # Render Login portal
    render_login_page(GOOGLE_CLIENT_ID, REDIRECT_URI)
else:
    # Render Research Dashboard
    render_dashboard(API_URL, sign_out)