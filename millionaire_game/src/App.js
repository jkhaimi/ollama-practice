import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [aiMessage, setAiMessage] = useState('');

  useEffect(() => {
    fetch('/result').then(
      res => res.json()
    ).then(
      aiMessage => {
        setAiMessage(aiMessage);
        console.log(aiMessage);
      }
    )
  }, []);

  return (
    <div className="app">
      <h1>Tekoälyn vastaus:</h1>
      <div className="message-box">
        <p>{aiMessage?.message}</p>
      </div>
    </div>
  );
}

export default App; 