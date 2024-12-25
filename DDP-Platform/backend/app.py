from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes.upload import upload_blueprint
from routes.questions import questions_blueprint
from routes.progress import progress_blueprint

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dpp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(upload_blueprint)
app.register_blueprint(questions_blueprint)
app.register_blueprint(progress_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
