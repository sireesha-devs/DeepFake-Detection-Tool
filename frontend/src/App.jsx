import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:5000/analyze', formData);
      setResults(response.data);
    } catch (err) {
      console.error("Analysis failed", err);
    } setLoading(false);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif', backgroundColor: '#0f172a', color: 'white', minHeight: '100vh' }}>
      <h1>🔍 Forensix AI: Deepfake Detector</h1>
      
      {/*<input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={loading} style={{ marginLeft: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        {loading ? 'Analyzing...' : 'Run Forensic Scan'}
      </button>*/}
      <div style={{ marginBottom: '20px' }}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button 
          onClick={handleUpload} 
          disabled={loading} 
          style={{ marginLeft: '10px', padding: '10px 20px', cursor: 'pointer', borderRadius: '4px', border: 'none', backgroundColor: '#3b82f6', color: 'white' }}
        >
          {loading ? 'Analyzing...' : 'Run Forensic Scan'}
        </button>
      </div>

      {results && (
        <div style={{ marginTop: '30px' }}>
            {console.log("Results received:", results)}
          <h2>Confidence Score: <span style={{ color: results.score > 50 ? '#e5dbdbff' : '#dee2dfff' }}>{results.score}% Artificial</span></h2>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginTop: '20px' }}>
            <div>
              <h3>Original</h3>
              <img src={URL.createObjectURL(file)} alt="Original" style={{ width: '100%', borderRadius: '8px' }} />
            </div>
            <div>
              <h3>Error Level Analysis (ELA)</h3>
              <img src={results.ela_url} alt="ELA" style={{ width: '100%', borderRadius: '8px', border: '1px solid #334155' }} />
            </div>
            <div>
              <h3>Frequency Spectrum (FFT)</h3>
              <img src={results.fft_url} alt="FFT" style={{ width: '100%', borderRadius: '8px', border: '1px solid #334155' }} />
            </div>
            <div style={{ border: '1px solid #334155', padding: '10px', borderRadius: '8px' }}>
              <h3>Forensic Heatmap</h3>
              <img src={results.heatmap_url} alt="Heatmap" style={{ width: '100%', borderRadius: '4px' }} />
              <p style={{ fontSize: '12px', color: '#94a3b8' }}>Visualizes high-probability tampered regions</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;