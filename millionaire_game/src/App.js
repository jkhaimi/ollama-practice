import React, { useState } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const res = await fetch('http://127.0.0.1:5000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question }),
    });

    console.log(question)
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="app">
      <h1>Who want to be a millionaire?</h1>
      <div className="answer-box">
        <h2>AI:s answer:</h2>
        <p>{response}</p>
      </div>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={question} 
          onChange={(e) => setQuestion(e.target.value)} 
          placeholder="Ask a question..." 
          required 
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
