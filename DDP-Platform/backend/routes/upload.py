from flask import Blueprint, request, jsonify
from models.pdf_parser import parse_pdf
from db import db, File

upload_blueprint = Blueprint('upload', __name__)

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = parse_pdf(file)
    
    new_file = File(filename=file.filename, content=content)
    db.session.add(new_file)
    db.session.commit()
    
    return jsonify({'message': 'File uploaded and parsed successfully!', 'file_id': new_file.id})
