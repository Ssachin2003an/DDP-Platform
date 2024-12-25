from transformers import pipeline

def generate_mcqs(text):
    generator = pipeline('text2text-generation', model='t5-base')
    prompt = f"Generate multiple-choice questions based on the following text:\n{text}\n"
    response = generator(prompt, max_length=512, num_return_sequences=5)

    questions = []
    for item in response:
        question_data = parse_question(item['generated_text'])
        questions.append(question_data)
    return questions

def parse_question(text):
    # Custom logic to parse generated text into question, options, and answers
    return {
        "question": "What is ...?",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
    }
