import openai

openai.api_key = "your_api_key_here"  # সঠিক API কী বসান

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "your question here"}  # সঠিক প্রশ্ন দিন
    ]
)

print(response.choices[0].message["content"])