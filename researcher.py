# researcher.py
import openai

api_key = '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'
openai.api_key = api_key

def generate_ideas(topic):
    prompt = f"Generate ideas for teaching someone new about {topic}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
    )
    return response.choices[0].text.strip()

# Example usage
ideas = generate_ideas("Python programming")
print(ideas)
