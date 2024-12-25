Step-by-Step Guide to Run the DPP-Platform
1. Clone the Repository
First, clone the project repository to your local machine (or server) if you haven't already.

bash
Copy code
git clone <your-repo-url>
cd DPP-Platform
2. Set Up the Backend
2.1. Install Backend Dependencies
Navigate to the backend directory and install the required Python dependencies listed in requirements.txt.

bash
Copy code
cd backend
pip install -r requirements.txt
2.2. Configure Environment Variables
Create a .env file in the backend directory to configure environment variables. This file should contain information like your database URL and other necessary credentials.

bash
Copy code
touch .env
Populate it with the following settings (modify accordingly based on your setup):

plaintext
Copy code
DATABASE_URL=postgres://username:password@localhost:5432/dpp_db
SECRET_KEY=your-secret-key
DEBUG=True
2.3. Set Up Database
If you are using PostgreSQL, MySQL, or another database, you need to set up the database. The example below assumes PostgreSQL, but adjust as needed for other databases.

Create the Database:
bash
Copy code
psql -U postgres
CREATE DATABASE dpp_db;
Migrate the Database (if using SQLAlchemy or another ORM):
Inside the backend directory, run the migration command (e.g., Flask-Migrate).

bash
Copy code
flask db upgrade
2.4. Run the Backend Server
Now that the environment is configured, you can start the backend server using Flask:

bash
Copy code
flask run
This will run the backend locally on http://127.0.0.1:5000 by default.

Alternatively, for production use, you can run the Flask app with Gunicorn:

bash
Copy code
gunicorn -w 4 app:app
This runs the Flask app with 4 worker processes for better performance in a production environment.

3. Set Up the Frontend
3.1. Install Frontend Dependencies
Navigate to the frontend directory and install the required dependencies using npm:

bash
Copy code
cd frontend
npm install
3.2. Configure Environment Variables
Create a .env file in the frontend directory to define the API URL of the backend.

bash
Copy code
touch .env
Add the following line to the .env file, adjusting for your backend URL:

plaintext
Copy code
REACT_APP_API_BASE_URL=http://localhost:5000
3.3. Start the Frontend Development Server
Once dependencies are installed and environment variables are set, start the React development server:

bash
Copy code
npm start
This will start the frontend locally on http://localhost:3000.

4. Connect Backend and Frontend
Once both the backend and frontend servers are running, ensure they are properly connected. The frontend will make API calls to the backend using the API URL defined in the .env file.

Backend API will run at http://localhost:5000.
Frontend will run at http://localhost:3000.
Ensure that the frontend components, such as the Dashboard, Progress, and Practice, are interacting correctly with the backend API.

Important Notes for API Requests:
Make sure that the frontend requests are directed to the correct endpoint, as configured in api.js and .env.
The backend must allow cross-origin requests (CORS). If it's not already set, you can configure CORS in Flask:
python
Copy code
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
5. Testing the Application
Now that both frontend and backend are running:

Visit the Frontend: Open your browser and go to http://localhost:3000 (or the URL defined for your frontend).
Log In: If authentication is set up, log in using a test user.
Test Upload: Upload a PDF and check if the MCQs are generated correctly.
Track Progress: Navigate to the progress page to view practice statistics.
Practice MCQs: Start practicing MCQs to see how the app generates them dynamically.
6. Deployment (Optional)
6.1. Backend Deployment
To deploy the backend, you can use platforms like Heroku, AWS EC2, or DigitalOcean.

Example deployment on Heroku:

Install Heroku CLI and log in.

Create a Procfile in the backend directory:

plaintext
Copy code
web: gunicorn -w 4 app:app
Deploy the App:

bash
Copy code
git push heroku main
After deployment, your backend will be accessible via the Heroku URL (e.g., https://your-app-name.herokuapp.com).

6.2. Frontend Deployment
For deploying the React frontend, platforms like Netlify, Vercel, or Firebase Hosting are ideal.

To deploy on Netlify:

Build the React App:

bash
Copy code
npm run build
Deploy: Follow Netlify's deployment steps (you can push your build folder to a GitHub repository and connect it to Netlify for easy deployment).

Once deployed, the frontend will be available on your Netlify domain.

7. Final Notes
Security: Make sure to secure sensitive data, such as the SECRET_KEY, and use proper authentication and authorization mechanisms (like JWT).
API Testing: Consider using tools like Postman or Insomnia for testing API endpoints during development.
Performance: If necessary, optimize both frontend and backend for better performance using tools like React Profiler or Flask caching.
This should get your DPP-Platform up and running on both the local environment and for deployment.
