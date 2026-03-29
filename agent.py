import ollama
import json
from utils import mask_sensitive_data

# Step 1: Search Knowledge Base
def search_kb(logs):
    with open("mock_kb.json") as f:
        kb = json.load(f)

    for item in kb:
        if any(word in logs.lower() for word in item["error"].lower().split()):
            return item
    return None


# Main function (this was your existing one)
def analyze_logs(logs):

    # Step 1: Mask data
    masked_logs = mask_sensitive_data(logs)

    # Step 2: Check knowledge base
    kb_result = search_kb(masked_logs)

    if kb_result:
        return f"""
Known Issue Detected

Root Cause:
{kb_result['cause']}

Fix:
{kb_result['fix']}

Impacted Component:
{kb_result['component']}

Confidence:
95%
"""

    # Step 3: AI fallback
    prompt = f"""
You are a senior backend engineer.

Analyze the log strictly.

Log:
{masked_logs}

Respond ONLY in this format:

Root Cause:
<one clear reason>

Fix:
<one clear fix>

Impacted Component:
<component>

Confidence:
<percentage>
"""

    try:
        response = ollama.chat(
            model='tinyllama',
            messages=[{"role": "user", "content": prompt}]
        )

        return response['message']['content']

    except Exception as e:
        return """
            ⚠️ AI Model not available in deployed environment.

            Showing Knowledge Base result only.

            👉 For full AI-powered analysis, please run this application locally using Ollama.
            """