from flask import Blueprint, request, jsonify
from models.question_generator import generate_mcqs
from db import db, File, Question

questions_blueprint = Blueprint('questions', __name__)

@questions_blueprint.route('/generate', methods=['POST'])
def generate_questions():
    file_id = request.json['file_id']
    file = File.query.get(file_id)
    questions = generate_mcqs(file.content)

    for q in questions:
        new_question = Question(
            question_text=q['question'],
            options=q['options'],
            answer=q['answer'],
            file_id=file_id
        )
        db.session.add(new_question)
    db.session.commit()

    return jsonify({'message': 'Questions generated successfully!'})
