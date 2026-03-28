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
```

## 🧠 How It Works

This project follows a hybrid AI architecture:

1. **Data Masking Layer**  
   Sensitive information (emails, account numbers) is masked before processing.

2. **Knowledge Base Lookup**  
   Known issues are matched using a predefined knowledge base for fast and reliable responses.

3. **LLM-based Reasoning**  
   If no match is found, a local LLM (TinyLlama via Ollama) is used to infer root cause and fixes.

---

## 🏗️ System Design

UI Layer (Streamlit)  
↓  
Processing Layer (Agent Logic)  
↓  
Knowledge Base + LLM  

---

## 🔐 Security Considerations

- No external API calls (fully local)
- Sensitive data masking before processing
- Suitable for financial systems (PII safe)

---

## 🚧 Limitations

- Does not access real logs or codebase
- Relies on pattern-based inference
- Knowledge base is static (can be improved)

---

## 🔮 Future Improvements

- Integration with log systems (Splunk, Kibana)
- Dynamic learning from past incidents
- Multi-agent architecture for deeper analysis