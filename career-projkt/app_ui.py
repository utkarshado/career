import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Career Predictor", page_icon="🚀", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🚀 Career Recommendation System Using Random Forest Classifier</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar info
st.sidebar.header("About")
st.sidebar.write("Web application to predict career path of an individual by analyzing skills.")

# Input section
st.subheader("🧠 Enter Your Skills")

col1, col2 = st.columns(2)

with col1:
    prog = st.slider("💻 Programming", 0, 10, 5)
    math = st.slider("📊 Math", 0, 10, 5)
    comm = st.slider("🗣 Communication", 0, 10, 5)
    creative = st.slider("🎨 Creativity", 0, 10, 5)

with col2:
    logic = st.slider("🧩 Logic", 0, 10, 5)
    tech = st.slider("⚙ Tech Interest", 0, 10, 5)
    business = st.slider("📈 Business", 0, 10, 5)
    cgpa = st.slider("🎓 CGPA", 0.0, 10.0, 7.0)

st.markdown("---")

# Predict button
if st.button("🔮 Predict Career", use_container_width=True):
    with st.spinner("Analyzing your skills..."):

        try:
            response = requests.post(
                "https://career-rd17.onrender.com/predict",
                json={
                    "prog": prog,
                    "math": math,
                    "comm": comm,
                    "creative": creative,
                    "logic": logic,
                    "tech": tech,
                    "business": business,
                    "cgpa": cgpa
                }
            )

            if response.status_code == 200:
                result = response.json()["career"]

                st.success("✅ Prediction Complete!")
                st.markdown(f"""
                ### 🎯 Best career for your set of skills is :
                ## **{result}**
                """)

            else:
                st.error("❌ API Error. Check backend.")

        except Exception as e:
            st.error("🚨 Could not connect to API. Is FastAPI running?")
