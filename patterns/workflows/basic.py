import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {
            "role": "system", "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)
response = completion.choices[0].message.content
print(response)