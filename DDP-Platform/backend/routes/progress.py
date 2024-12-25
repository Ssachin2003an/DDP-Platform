from flask import Blueprint, request, jsonify
from db import db, Progress, User, Question

progress_blueprint = Blueprint('progress', __name__)

@progress_blueprint.route('/progress', methods=['POST'])
def update_progress():
    """
    Update user progress after answering a question.
    The request body should include:
    - user_id: ID of the user
    - question_id: ID of the question
    - correct: Boolean indicating whether the answer was correct
    """
    data = request.json

    try:
        user_id = data['user_id']
        question_id = data['question_id']
        correct = data['correct']

        # Create a new progress entry
        progress = Progress(user_id=user_id, question_id=question_id, correct=correct)
        db.session.add(progress)
        db.session.commit()

        return jsonify({'message': 'Progress updated successfully!'}), 200

    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@progress_blueprint.route('/progress/<int:user_id>', methods=['GET'])
def get_user_progress(user_id):
    """
    Retrieve the progress of a specific user.
    Returns:
    - Total questions attempted
    - Correct answers
    - Accuracy percentage
    """
    try:
        total_attempts = Progress.query.filter_by(user_id=user_id).count()
        correct_answers = Progress.query.filter_by(user_id=user_id, correct=True).count()

        if total_attempts == 0:
            accuracy = 0
        else:
            accuracy = (correct_answers / total_attempts) * 100

        progress_summary = {
            'total_attempts': total_attempts,
            'correct_answers': correct_answers,
            'accuracy_percentage': round(accuracy, 2)
        }

        return jsonify(progress_summary), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@progress_blueprint.route('/progress/reset/<int:user_id>', methods=['DELETE'])
def reset_user_progress(user_id):
    """
    Reset all progress for a specific user.
    Deletes all progress records for the user from the database.
    """
    try:
        Progress.query.filter_by(user_id=user_id).delete()
        db.session.commit()

        return jsonify({'message': 'User progress reset successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
