import streamlit as st
from agent import analyze_logs

st.set_page_config(page_title="AI Debug Agent", layout="centered")

st.title("🤖 AI Debugging Agent")
st.write("Analyze backend logs with AI + Knowledge Base")

uploaded_file = st.file_uploader("📁 Upload log file")

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8")
else:
    logs = st.text_area("📥 Paste your logs here", height=200)

# Button
if st.button("Analyze"):

    if logs:
        # Step-by-step agent feel
        st.write("🔐 Step 1: Masking sensitive data...")
        st.write("📚 Step 2: Checking historical incidents...")
        st.write("🧠 Step 3: Performing AI analysis...")

        # Get result
        result = analyze_logs(logs)

        st.write("✅ Analysis Complete")
        st.markdown("---")

        # Output
        st.subheader("📊 Result")
        st.write(result)

        # Follow-up question (agent feel)
        st.markdown("---")
        st.subheader("🤔 Follow-up")
        st.write("Was this issue observed after a recent deployment?")

    else:
        st.warning("⚠️ Please enter logs to analyze")