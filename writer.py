# writer.py
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def write_text(ideas):
    prompt = f"Explain the topic: {ideas}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
    )
    return response.choices[0].text.strip()

# Example usage
ideas = "Some ideas generated by the Researcher..."
text = write_text(ideas)
print(text)
