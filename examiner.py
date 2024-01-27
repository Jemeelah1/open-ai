# examiner.py
import openai

api_key = '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'
openai.api_key = api_key

def generate_questions(text):
    prompt = f"Create 2-3 test questions based on the following text:\n{text}\n\n1."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=3,
    )
    return [choice.text.strip() for choice in response.choices]

# Example usage
text = "Some text written by the Writer..."
questions = generate_questions(text)
print(questions)
