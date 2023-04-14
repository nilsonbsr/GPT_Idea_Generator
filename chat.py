import os
import openai

# get the key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# send a request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hi ChatGPT, say hi back!"}
    ]
)
# get the answer provided by chatgpt
answer = response.choices[0].message.content
print(answer)
