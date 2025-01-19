// frontend/src/components/HomePage.js
import React from 'react';
import './SpotifyLogin.css';

const SpotifyLogin = () => {
  return (
    <div className="container">
      <h1>Mood Music</h1>
      <p className="description">
        Experience the power of AI-driven music curation. <br /> Our app analyzes your
        mood through facial recognition and creates the perfect Spotify playlist
        to match your emotions.
      </p>
      <div className="features">
        <div className="feature">
          <div className="feature-icon">🎵</div>
          <p>AI-Powered</p>
        </div>
        <div className="feature">
          <div className="feature-icon">😊</div>
          <p>Emotion Detection</p>
        </div>
        <div className="feature">
          <div className="feature-icon">🎯</div>
          <p>Personalized</p>
        </div>
      </div>
      <a href="/login" className="login-button pulse">
        Login with Spotify
      </a>
    </div>
  );
};

export default SpotifyLogin;
