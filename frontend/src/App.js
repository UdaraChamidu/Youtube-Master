import React, { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    setLoading(true);
    setError("");
    setResponse(null);

    try {
      const res = await fetch(`http://127.0.0.1:8000/summarize/?url=${encodeURIComponent(url)}`);
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError("Something went wrong!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="chatbox">
        <h1>YouTube Summary Chat</h1>
        <div className="input-area">
          <input
            type="text"
            placeholder="Paste YouTube URL..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button onClick={handleSubmit}>{loading ? "Loading..." : "Send"}</button>
        </div>

        {error && <p className="error">{error}</p>}

        {response && (
          <div className="response-area">
            <div className="message bot">
              <strong>🤖 English Summary:</strong>
              <p>{response.summary_en}</p>
            </div>
            <div className="message bot">
              <strong>🗣️ Sinhala Summary:</strong>
              <p>{response.summary_si}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
