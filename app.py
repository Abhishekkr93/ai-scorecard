import streamlit as st
import pandas as pd
import random
import google.generativeai as genai

# 🔑 Gemini API (put your key here)
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎨 IPL Theme UI
st.set_page_config(page_title="IPL AI Scorecard", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0b1c2c;
        color: white;
    }
    .stButton>button {
        background-color: #ff4b2b;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏏 IPL AI Vibe Scorecard 🔥")

# 🧩 Tabs (Premium UI)
tab1, tab2, tab3 = st.tabs(["📊 Scorecard", "🧠 AI Vibes", "🎙️ Commentary"])

# ------------------ TAB 1 ------------------
with tab1:
    st.header("Match Dashboard")

    team1 = "MI"
    team2 = "CSK"

    runs = st.slider("Runs", 50, 250, 145)
    wickets = st.slider("Wickets", 0, 10, 3)
    overs = st.slider("Overs", 1.0, 20.0, 16.2)

    st.subheader(f"{team1} vs {team2}")
    st.metric("Score", f"{runs}/{wickets}")
    st.metric("Overs", overs)

    # Win Probability
    run_rate = runs / overs
    required_rate = 8.5

    if run_rate > required_rate:
        win_prob = random.randint(60, 85)
    else:
        win_prob = random.randint(30, 55)

    st.write("## 📊 Win Probability")
    st.progress(win_prob)
    st.write(f"{win_prob}% chance to win")

    # Fake Live Update
    if st.button("Simulate Live Update"):
        runs += random.randint(1, 6)
        st.success(f"Updated Score: {runs}/{wickets}")

# ------------------ TAB 2 ------------------
with tab2:
    st.header("🧠 AI Match Insights")

    if st.button("Analyze Match Vibe"):
        prompt = f"""
        You are an IPL expert commentator.

        Score: {runs}/{wickets}
        Overs: {overs}

        Give:
        1. 1-line headline
        2. Match insight
        3. Who is winning and why
        """

        response = model.generate_content(prompt)

        st.success("AI Insight Generated 🔥")
        st.write(response.text)
        st.balloons()

    # Vibe Meter
    vibe = st.slider("🔥 Match Vibe Meter", 0, 100, 65)

    if vibe > 70:
        st.success("🔥 High energy match!")
    elif vibe > 40:
        st.info("😐 Balanced game")
    else:
        st.warning("😬 Pressure situation!")

# ------------------ TAB 3 ------------------
with tab3:
    st.header("🎙️ AI Commentary Generator")

    event = st.text_input("Enter last ball event")

    if st.button("Generate Commentary"):
        prompt = f"""
        Create exciting IPL commentary in Hinglish for:
        {event}
        """

        response = model.generate_content(prompt)

        st.write(response.text)
