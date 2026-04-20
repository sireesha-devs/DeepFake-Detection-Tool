# Forensix AI: Deepfake Detector
### Hybrid Image Forensics & Explainable AI (XAI)

Forensix AI is a full-stack deepfake detection system developed for **ELEXCENTRA 2K26**. It bridges the gap between complex deep learning models and human-readable forensic evidence by providing a "Confidence Score" alongside detailed visual heatmaps.

## 🚀 Key Features

* **Hybrid Analysis:** Combines a lightweight **MobileNetV2** CNN for fast classification with classic forensic algorithms.
* **Error Level Analysis (ELA):** Detects localized compression mismatches by analyzing the difference between original and resaved JPEG data.
* **Frequency Spectrum (FFT):** Uses Fast Fourier Transform to expose GAN-generated grid patterns and frequency-domain anomalies.
* **Real-time Dashboard:** A React-based interface providing instant feedback on uploaded images.

## 🛠️ Tech Stack

* **Frontend:** React (Vite), Axios, Tailwind CSS
* **Backend:** Flask, Flask-CORS
* **AI/Forensics:** PyTorch, Pillow, NumPy, SciPy

## 📦 Installation & Setup

### 1. Backend Setup
```bash
cd backend
pip install flask flask-cors torch torchvision pillow numpy
python app.py
Your README.md and a professional PDF version for your project documentation are ready. This file includes the full-stack setup, the technical logic behind ELA and FFT, and the hybrid detection architecture you implemented.

 Forensix_AI_README 
PDF

README.md
Markdown
# Forensix AI: Deepfake Detector
### Hybrid Image Forensics & Explainable AI (XAI)

Forensix AI is a full-stack deepfake detection system developed for **ELEXCENTRA 2K26**. It bridges the gap between complex deep learning models and human-readable forensic evidence by providing a "Confidence Score" alongside detailed visual heatmaps.

## 🚀 Key Features

* **Hybrid Analysis:** Combines a lightweight **MobileNetV2** CNN for fast classification with classic forensic algorithms.
* **Error Level Analysis (ELA):** Detects localized compression mismatches by analyzing the difference between original and resaved JPEG data.
* **Frequency Spectrum (FFT):** Uses Fast Fourier Transform to expose GAN-generated grid patterns and frequency-domain anomalies.
* **Real-time Dashboard:** A React-based interface providing instant feedback on uploaded images.

## 🛠️ Tech Stack

* **Frontend:** React (Vite), Axios, Tailwind CSS
* **Backend:** Flask, Flask-CORS
* **AI/Forensics:** PyTorch, Pillow, NumPy, SciPy

## 📦 Installation & Setup

### 1. Backend Setup
```bash
cd backend
pip install flask flask-cors torch torchvision pillow numpy
python app.py
2. Frontend Setup
Bash
cd frontend
npm install
npm run dev```


🧠 Technical Logic
The system addresses the "Black Box" problem in AI by providing Explainable AI (XAI):

Spatial Domain: ELA identifies where pixels have been modified or replaced by highlighting inconsistencies in the compression grid.

Frequency Domain: FFT uncovers mathematical periodicities that are invisible to the naked eye but common in synthetic imagery.

📂 Project Structure
Plaintext
/
├── backend/
│   ├── app.py             # API Endpoints & CORS Config
│   ├── core/
│   │   ├── ela_engine.py  # ELA computation logic
│   │   └── fft_engine.py  # FFT processing logic
│   └── uploads/           # Forensic output storage
└── frontend/
    └── src/
        └── App.jsx        # Forensic Dashboard UI
Developed for ELEXCENTRA 2K26 | AU Hackathon
