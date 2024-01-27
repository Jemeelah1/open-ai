import ollama

stream = ollama.chat(
    model='mistral',
    messages[{'role': 'user', 'content': 'What is Python Programming'}],
    stream=True,
)

for chunk in strem:
    print(chunk['message']['content'], end='', flush=True)
