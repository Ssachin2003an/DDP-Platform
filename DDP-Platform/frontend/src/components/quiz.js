import React, { useState, useEffect } from "react";
import axios from "axios";

const Quiz = ({ fileId }) => {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    const fetchQuestions = async () => {
      const response = await axios.post("http://localhost:5000/generate", {
        file_id: fileId,
      });
      setQuestions(response.data.questions);
    };

    fetchQuestions();
  }, [fileId]);

  return (
    <div>
      <h1>Quiz</h1>
      {questions.map((q, index) => (
        <div key={index}>
          <p>{q.question_text}</p>
          {q.options.map((option, idx) => (
            <button key={idx}>{option}</button>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Quiz;
