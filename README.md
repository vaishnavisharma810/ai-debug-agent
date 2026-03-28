# 🤖 AI Debugging Agent

A privacy-first AI agent that analyzes backend logs and suggests root causes and fixes.

## 🚀 Features
- 🔐 Sensitive data masking (PII protection)
- 📚 Knowledge base for known issues
- 🤖 Local LLM (TinyLlama via Ollama)
- 📊 Structured output (RCA, Fix, Component, Confidence)

## 🧠 Architecture
1. Mask sensitive data
2. Check knowledge base
3. AI-based reasoning (fallback)

## 🛠️ Tech Stack
- Python
- Streamlit
- Ollama (Local LLM)
- JSON (Knowledge Base)

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py