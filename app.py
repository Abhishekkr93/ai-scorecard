import streamlit as st
import pandas as pd
import random
import time
from google import genai

# 🔑 Replace with your API key
client = genai.Client(api_key="API")

# 🎨 UI Config
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

# 🧩 Tabs
tab1, tab2, tab3 = st.tabs(["📊 Scorecard", "🧠 AI Vibes", "🎙️ Commentary"])

# ------------------ TAB 1 ------------------
with tab1:
    st.header("Match Dashboard")

    team1 = "Mumbai Indians"
    team2 = "Chennai Super Kings"

    # Logos
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/en/2/2c/Mumbai_Indians_Logo.svg", width=100)
        st.write(team1)
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/en/2/2e/Chennai_Super_Kings_Logo.svg", width=100)
        st.write(team2)

    # Inputs
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

    # 📊 Graph
    st.write("### 📈 Runs Per Over")
    overs_list = list(range(1, 11))
    runs_data = [random.randint(5, 15) for _ in overs_list]

    df = pd.DataFrame({
        "Over": overs_list,
        "Runs": runs_data
    })

    st.line_chart(df.set_index("Over"))

    # 🔴 Live Simulation
    st.write("### 🔴 Live Match Simulation")

    if st.button("Start Live Match"):
        placeholder = st.empty()
        live_runs = runs
        live_wickets = wickets

        for i in range(6):
            live_runs += random.randint(1, 6)

            if random.random() < 0.2:
                live_wickets += 1

            placeholder.metric("Live Score", f"{live_runs}/{live_wickets}")
            time.sleep(1.5)

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

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        st.success("AI Insight Generated 🔥")
        st.write(response.text)
        st.balloons()

    # 🔥 Vibe Meter
    vibe = st.slider("🔥 Match Vibe Meter", 0, 100, 65)

    if vibe > 70:
        st.success("🔥 High energy match!")
    elif vibe > 40:
        st.info("😐 Balanced game")
    else:
        st.warning("😬 Pressure situation!")

    # 🔥 Moment of Match
    if st.button("Highlight Moment"):
        prompt = f"""
        Based on score {runs}/{wickets} in {overs} overs,
        tell the turning point of the match in 1 line.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        st.warning("🔥 Moment of the Match")
        st.write(response.text)

# ------------------ TAB 3 ------------------
with tab3:
    st.header("🎙️ AI Commentary Generator")

    event = st.text_input("Enter last ball event")

    if st.button("Generate Commentary"):
        prompt = f"""
        Create exciting IPL commentary in Hinglish for:
        {event}
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        st.write(response.text)
