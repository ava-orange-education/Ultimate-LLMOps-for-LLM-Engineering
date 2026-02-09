# Make a request to deployed model
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Explain cloud deployment"}]
)
print(response.choices[0].message.content)