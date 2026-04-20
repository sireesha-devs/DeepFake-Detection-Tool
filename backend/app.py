from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import cv2
import numpy as np
from core.ela_engine import perform_ela
from core.fft_engine import perform_fft
from core.classifier import get_prediction
from core.heatmap_engine import generate_heatmap # Import the CNN module
from flask import send_from_directory
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # 1. Forensic Visualizations (Visual evidence for judges)
    # Fulfills 'Display forensic indicators such as heatmaps, ELA maps'
    ela_img = perform_ela(file_path)
    fft_img = perform_fft(file_path)

    ela_path = os.path.join(UPLOAD_FOLDER, f"ela_{file.filename}")
    fft_path = os.path.join(UPLOAD_FOLDER, f"fft_{file.filename}")
    ela_img.save(ela_path)
    cv2.imwrite(fft_path, fft_img)

    # 2. Hybrid Classification Score
    # Combines CNN logic with FFT noise analysis for robustness
    cnn_score = get_prediction(file_path)
    fft_var = np.var(fft_img)
    
    # If the mathematical frequency is smooth, lower the artificial score
    if fft_var < 150:
        confidence_score = min(cnn_score, 12.0) 
    else:
        confidence_score = cnn_score

    # Fulfills 'Output: Image classification (Authentic or Manipulated)'
    classification = "Manipulated" if confidence_score > 50 else "Authentic"
    heatmap_res = generate_heatmap(file_path, ela_path)
    heatmap_path = os.path.join(UPLOAD_FOLDER, f"heatmap_{file.filename}")
    cv2.imwrite(heatmap_path, heatmap_res)

    return jsonify({
        "status": classification,
        "score": confidence_score,
        "ela_url": f"http://localhost:5000/uploads/ela_{file.filename}",
        "fft_url": f"http://localhost:5000/uploads/fft_{file.filename}",
        "heatmap_url": f"http://localhost:5000/uploads/heatmap_{file.filename}"
    })

@app.route('/uploads/<filename>')
def serve_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)