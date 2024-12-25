import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Progress.css"; // Custom CSS for styling

const Progress = ({ userId }) => {
  const [progress, setProgress] = useState({
    total_attempts: 0,
    correct_answers: 0,
    accuracy_percentage: 0,
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch user progress when the component loads
    const fetchProgress = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`/progress/${userId}`);
        setProgress(response.data);
      } catch (err) {
        setError("Failed to fetch progress. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchProgress();
  }, [userId]);

  const resetProgress = async () => {
    // Reset user progress
    try {
      setLoading(true);
      await axios.delete(`/progress/reset/${userId}`);
      setProgress({
        total_attempts: 0,
        correct_answers: 0,
        accuracy_percentage: 0,
      });
    } catch (err) {
      setError("Failed to reset progress. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="progress-container">Loading progress...</div>;
  }

  if (error) {
    return <div className="progress-container error">{error}</div>;
  }

  return (
    <div className="progress-container">
      <h2>Your Progress</h2>
      <div className="progress-stats">
        <div className="stat">
          <strong>Total Attempts:</strong> {progress.total_attempts}
        </div>
        <div className="stat">
          <strong>Correct Answers:</strong> {progress.correct_answers}
        </div>
        <div className="stat">
          <strong>Accuracy:</strong> {progress.accuracy_percentage}%
        </div>
      </div>
      <button className="reset-button" onClick={resetProgress}>
        Reset Progress
      </button>
    </div>
  );
};

export default Progress;
