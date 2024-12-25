import React from "react";
import { Link } from "react-router-dom";
import "./Dashboard.css";

const Dashboard = ({ userName }) => {
  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Welcome, {userName}!</h1>
        <p>Your personal study and practice platform</p>
      </header>

      <div className="dashboard-content">
        <div className="dashboard-section">
          <h2>Daily Practice Problems</h2>
          <p>Sharpen your skills with AI-generated questions based on your materials.</p>
          <Link to="/practice" className="dashboard-link">
            Start Practicing
          </Link>
        </div>

        <div className="dashboard-section">
          <h2>Upload Study Materials</h2>
          <p>Upload PDFs or textbooks to generate custom MCQs and quizzes.</p>
          <Link to="/upload" className="dashboard-link">
            Upload Materials
          </Link>
        </div>

        <div className="dashboard-section">
          <h2>Track Your Progress</h2>
          <p>View your performance and improve your learning journey.</p>
          <Link to="/progress" className="dashboard-link">
            View Progress
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
