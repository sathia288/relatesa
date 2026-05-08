import streamlit as st
import numpy as np
from datetime import datetime

st.set_page_config(page_title="RelateSA", page_icon="🌱", layout="centered")

st.title("🌱 RelateSA")
st.subheader("Matches on behavior • Skills • Compatibility")
st.caption("Johannesburg Pilot | Privacy-first | Relationship Science Driven")

page = st.sidebar.selectbox(
    "Menu", 
    ["Onboarding", "Discover Matches", "Messages", "Skill Builder", "Safety Hub"]
)

def create_psych_vector(answers):
    return {
        "Openness": answers[0]/5,
        "Conscientiousness": answers[1]/5,
        "Extraversion": answers[2]/5,
        "Agreeableness": answers[3]/5,
        "Emotional_Stability": 1 - (answers[4]/5),
        "Attachment_Secure": answers[5]/5
    }

if page == "Onboarding":
    st.header("Create Your Behavioral Profile")
    with st.form("onboarding_form"):
        name = st.text_input("Full Name *")
        age = st.number_input("Age", 18, 65, 28)
        email = st.text_input("Email *")
        
        st.subheader("Quick Relationship Personality Assessment")
        q1 = st.slider("I have a rich vocabulary and enjoy deep topics.", 1, 5, 4)
        q2 = st.slider("I get things done and follow through on commitments.", 1, 5, 4)
        q3 = st.slider("I am outgoing and energetic in social settings.", 1, 5, 3)
        q4 = st.slider("I sympathize with others and try to help.", 1, 5, 4)
        q5 = st.slider("I get stressed or worried easily.", 1, 5, 2)
        q6 = st.slider("I feel comfortable being close and depending on a partner.", 1, 5, 4)
        
        goals = st.multiselect("What are you looking for?", 
                              ["Long-term partner", "Marriage-minded", "Growth-focused relationship"])
        
        if st.form_submit_button("Create Profile & Get Matches"):
            if name and email:
                vector = create_psych_vector([q1, q2, q3, q4, q5, q6])
                st.session_state.profile = {
                    "name": name, "age": age, "email": email,
                    "psych_vector": vector, "goals": goals
                }
                st.success(f"✅ Profile created, {name}!")
                st.balloons()
            else:
                st.error("Name and Email required")

elif page == "Discover Matches":
    st.header("🔍 Your Compatibility Matches")
    if "profile" not in st.session_state:
        st.warning("Complete Onboarding first")
    else:
        st.write(f"Matches for **{st.session_state.profile['name']}**")
        mock = [
            {"name": "Thandiwe M.", "age": 29, "score": 89},
            {"name": "Sipho K.", "age": 33, "score": 84},
            {"name": "Lerato N.", "age": 26, "score": 91}
        ]
        for m in mock:
            with st.expander(f"{m['name']} — {m['score']}% Compatible"):
                st.progress(m['score']/100)
                st.button("💬 Message", key=m['name'])

elif page == "Messages":
    st.header("💬 Guided Messaging")
    st.info("**Tip**: Use 'I feel...' statements")
    st.text_area("Your message", "I really appreciated how you...")
    st.button("Send with Empathy Scaffold")

elif page == "Skill Builder":
    st.header("🛠 Build Relationship Skills")
    for lesson in ["Active Listening", "Healthy Conflict Repair", "Expressing Needs"]:
        if st.button(lesson):
            st.success(f"✅ Completed {lesson} • +50 XP")

elif page == "Safety Hub":
    st.header("🛡️ Safety First")
    st.success("All pilot profiles reviewed")
    st.button("Send Safety Check-in")

st.sidebar.success("RelateSA Pilot v0.1 • Johannesburg")
