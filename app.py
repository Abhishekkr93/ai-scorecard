import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Cricket Scorecard", layout="wide")

st.title("🏏 AI Smart Scorecard")

# Dummy Teams
team1 = "MI"
team2 = "CSK"

st.header(f"{team1} vs {team2}")

# Dynamic Score Simulation
runs = st.slider("Runs", 50, 250, 145)
wickets = st.slider("Wickets", 0, 10, 3)
overs = st.slider("Overs", 1.0, 20.0, 16.2)

st.subheader(f"Score: {runs}/{wickets} ({overs} overs)")

# Batsmen Table
batsmen = pd.DataFrame({
    "Player": ["Rohit Sharma", "Surya"],
    "Runs": [random.randint(20, 80), random.randint(10, 60)],
    "Balls": [random.randint(10, 50), random.randint(10, 40)]
})

st.write("### 🏏 Batsmen")
st.table(batsmen)

# Win Probability Logic
run_rate = runs / overs
required_rate = 8.5

if run_rate > required_rate:
    win_prob = random.randint(60, 85)
else:
    win_prob = random.randint(30, 55)

st.write("## 📊 Win Probability")
st.progress(win_prob)
st.write(f"{win_prob}% chance to win")

# AI Insight (Fake but smart-looking)
st.write("## 🧠 AI Insight")

if st.button("Generate Insight"):
    if win_prob > 60:
        st.success("Batting team is dominating with strong momentum 🔥")
    else:
        st.warning("Match is getting tight, pressure is building ⚡")

# Commentary Generator
event = st.text_input("Enter last ball event")

if st.button("Generate Commentary"):
    comments = [
        "What a शानदार shot! Pure timing!",
        "That’s gone for a massive SIX! 🚀",
        "Brilliant bowling under pressure!",
        "Crowd is loving this contest!"
    ]
    st.write(random.choice(comments))
