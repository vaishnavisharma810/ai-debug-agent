import ollama

response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            "role": "user",
            "content": "You are a senior backend engineer. Analyze this error: NullPointerException in FacilityService"
        }
    ]
)

print(response['message']['content'])