import streamlit as st
import time

def render_login_page(google_client_id, redirect_uri):
    # --- CUSTOM CSS FOR PREMIUM GLASSMORPHISM & ANIMATIONS ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@300;400;500;600&display=swap');
        
        /* Apply modern Inter font globally */
        html, body, [class*="css"], .stApp {
            font-family: 'Inter', sans-serif;
        }
        
        h1, h2, h3, .title-text {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
        }

        /* Custom Dark Gradient Background */
        .stApp {
            background: radial-gradient(circle at 10% 20%, rgba(20, 20, 35, 1) 0%, rgba(10, 10, 15, 1) 100%);
            overflow: hidden;
        }
        
        /* Floating Left Purple Glow Orb */
        .bg-glow-1 {
            position: absolute;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(124, 58, 237, 0.15) 0%, rgba(0,0,0,0) 70%);
            top: -100px;
            left: -100px;
            z-index: 0;
            pointer-events: none;
        }
        
        /* Floating Right Blue Glow Orb */
        .bg-glow-2 {
            position: absolute;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.12) 0%, rgba(0,0,0,0) 70%);
            bottom: -150px;
            right: -100px;
            z-index: 0;
            pointer-events: none;
        }

        /* Frosted Glass Login container */
        .login-container {
            max-width: 480px;
            margin: 80px auto;
            padding: 45px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
            text-align: center;
            position: relative;
            z-index: 10;
            animation: fadeIn 1s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .login-subtitle {
            color: #94a3b8;
            font-size: 15px;
            margin-bottom: 35px;
            line-height: 1.6;
        }

        /* Styled Brand Logo */
        .logo-container {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
            border-radius: 20px;
            margin-bottom: 25px;
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.4);
            font-size: 40px;
        }
        
        /* High Fidelity custom Google button */
        .google-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #ffffff;
            color: #1f2937;
            font-size: 16px;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            padding: 14px 28px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            width: 100%;
            box-sizing: border-box;
            margin-bottom: 20px;
        }
        
        .google-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(99, 102, 241, 0.25);
            border-color: #a855f7;
        }
        
        .google-icon {
            width: 20px;
            height: 20px;
            margin-right: 12px;
        }

        .security-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #64748b;
            font-size: 12px;
            margin-top: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Render floating glow effects on screen
    st.markdown('<div class="bg-glow-1"></div><div class="bg-glow-2"></div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 5vh;"></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="login-container">
            <div class="logo-container">🔬</div>
            <h1 style="color: #ffffff; font-size: 32px; margin-bottom: 8px; letter-spacing: -0.5px;">Deep Research</h1>
            <p style="color: #a855f7; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; font-size: 11px; margin-bottom: 24px;">Autonomous AI Research Assistant</p>
            
            <p class="login-subtitle">
                Access advanced multi-agent intelligence, live web-crawling, and synthesis models.
                Sign in to secure your computational workbench.
            </p>
    """, unsafe_allow_html=True)

    # Authentication button
    if google_client_id:
        # Generate OAuth consent redirection link
        google_oauth_url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?"
            f"client_id={google_client_id}&"
            f"redirect_uri={redirect_uri}&"
            f"response_type=code&"
            f"scope=openid%20email%20profile&"
            f"state=deep_research_state"
        )
        
        st.markdown(f"""
            <a href="{google_oauth_url}" target="_self" class="google-btn">
                <img class="google-icon" src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google logo">
                Sign in with Google
            </a>
        """, unsafe_allow_html=True)
    else:
        # Simulated test authentication flow
        if st.button("✨ Demo OAuth Sign In", use_container_width=True, type="primary"):
            with st.spinner("Simulating Google OAuth redirect and token handshake..."):
                time.sleep(1.5)
                st.session_state["authenticated"] = True
                st.session_state["user"] = {
                    "name": "Dr. Sarah Chen",
                    "email": "sarah.chen@deepresearch.ai",
                    "picture": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=100",
                    "role": "Lead Research Fellow",
                    "id_token": "mocked_jwt_token_google_oauth2_xyz123"
                }
                st.rerun()
                
        st.markdown("""
            <p style="color: #64748b; font-size: 11px; margin-top: 10px;">
                💡 Running in <b>Standalone UI Mode</b>. Clicking above simulates a secure OAuth flow.
            </p>
        """, unsafe_allow_html=True)

    st.markdown("""
            <div class="security-badge">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
                AES-256 Bit Encrypted Authentication Gate
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_verification_loader():
    st.markdown("""
        <style>
        .login-container {
            max-width: 480px;
            margin: 80px auto;
            padding: 45px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            text-align: center;
        }
        .logo-container {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
            border-radius: 20px;
            margin-bottom: 25px;
            font-size: 40px;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="logo-container">🔬</div>', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #f8fafc; margin-bottom:10px;">Security Verification</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8; font-size:15px; margin-bottom: 25px;">Exchanging secure token with Google Auth Services...</p>', unsafe_allow_html=True)