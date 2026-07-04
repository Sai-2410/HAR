# 🏃 ActiVision AI
### Real-Time Human Activity Recognition Using Deep Learning

ActiVision AI is a Flask-based Human Activity Recognition (HAR) system that uses **Computer Vision**, **MediaPipe Pose Estimation**, and **Deep Learning** to recognize human activities in real time through a laptop camera.

The system detects human body landmarks from live video, extracts pose features, and feeds them into a trained deep learning model to classify different human activities instantly. The predictions are displayed through an interactive web interface built using Flask.

This project demonstrates an end-to-end AI workflow, including:

- Human Pose Detection
- Feature Extraction
- Deep Learning Model Training
- Real-Time Activity Recognition
- Flask Deployment

---

# 📖 Table of Contents

- Features
- Technology Stack
- System Architecture
- Project Workflow
- Deep Learning Pipeline
- Model Architecture
- Repository Structure
- Installation
- Running the Application
- Project Screenshots
- Skills Demonstrated
- Future Improvements
- Project Note

---

# ✨ Features

- 🎥 Real-time activity recognition using webcam
- 🦴 Human pose detection using MediaPipe
- 📍 Body landmark extraction
- 🧠 Deep learning-based activity classification
- ⚡ Instant predictions from live camera feed
- 🌐 Flask web application
- 📊 Complete AI inference pipeline
- 📂 Modular code structure
- 💾 Trained model integration
- 🖥 User-friendly interface

---

# 🚀 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Backend | Flask |
| Deep Learning | TensorFlow, Keras |
| Computer Vision | OpenCV |
| Pose Detection | MediaPipe |
| Machine Learning | Scikit-Learn |
| Data Processing | NumPy, Pandas |
| Frontend | HTML, CSS, JavaScript |

---

# 🏗 System Architecture

```text
               Live Camera
                    │
                    ▼
      MediaPipe Pose Detection
                    │
                    ▼
      Human Landmark Extraction
                    │
                    ▼
      Feature Preprocessing
                    │
                    ▼
      Trained Deep Learning Model
                    │
                    ▼
      Human Activity Prediction
                    │
                    ▼
      Flask Web Application
                    │
                    ▼
      Activity Display to User
```

---

# 🔄 Project Workflow

## 1️⃣ Data Collection

- Capture live video using webcam
- Detect human body pose
- Extract body landmark coordinates
- Store activity samples

---

## 2️⃣ Feature Engineering

- Clean collected data
- Normalize landmark coordinates
- Prepare training dataset
- Convert movements into numerical features

---

## 3️⃣ Model Training

- Train deep learning model
- Evaluate model performance
- Save trained model

Outputs:

```
model.h5
labels.npy
```

---

## 4️⃣ Inference

- Load trained model
- Capture live camera frames
- Extract pose landmarks
- Predict activity
- Display prediction in browser

---

# 🧠 Deep Learning Pipeline

```text
Camera Frame
      │
      ▼
MediaPipe Pose Detection
      │
      ▼
Pose Landmarks
      │
      ▼
Feature Extraction
      │
      ▼
Deep Learning Model
      │
      ▼
Activity Classification
      │
      ▼
Real-Time Prediction
```

---

# 🧠 Deep Learning Models

The project experiments with different sequence-learning architectures.

| Model | Purpose |
|--------|----------|
| CNN | Learns spatial features |
| RNN | Sequential learning |
| LSTM | Learns temporal dependencies |
| GRU | Lightweight sequence learning |
| CNN-LSTM | Spatial + Temporal feature learning |

---

# 📂 Repository Structure

```text
HUMAN_ACTIVITY_FINAL/
│
├── app.py
├── inference.py
├── data_collection.py
├── data_training.py
│
├── model.h5
├── labels.npy
├── requirements.txt
│
├── templates/
│   ├── home.html
│   └── login.html
│
├── static/
│   ├── bg.jpg
│   └── styles/
│
├── Snapshots/
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/IgrisViOverlord-10/laughing-dollop.git
```

Move into the project directory.

```bash
cd HUMAN_ACTIVITY_FINAL
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Start the Flask server.

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

The application will start detecting and recognizing human activities using your webcam.

---

# 📸 Project Screenshots

| Screenshot | Description |
|------------|-------------|
| ![](Snapshots/Snap-1.png) | Login Page |
| ![](Snapshots/Snap-2.png) | Home Dashboard |
| ![](Snapshots/Snap-3.png) | Real-Time Activity Prediction |

---

# 🧪 Machine Learning Workflow

```text
Collect Dataset
      │
      ▼
Extract Pose Landmarks
      │
      ▼
Preprocess Features
      │
      ▼
Train Deep Learning Model
      │
      ▼
Save Model
      │
      ▼
Deploy with Flask
      │
      ▼
Real-Time Prediction
```

---

# 💡 Skills Demonstrated

- Deep Learning
- Computer Vision
- Human Pose Estimation
- OpenCV
- MediaPipe
- TensorFlow
- Keras
- Flask Development
- Feature Engineering
- Machine Learning Pipeline
- Model Deployment
- Real-Time AI Systems

---

# 🔮 Future Improvements

- Support more activity classes
- Increase dataset diversity
- Improve prediction accuracy
- Integrate Transformer-based models
- Handle occlusion and low-light environments
- Cloud deployment
- Mobile application
- Edge-device optimization
- Activity history dashboard
- Explainable AI integration

---

# 📚 Project Note

This project was developed as a final-year academic project to demonstrate the practical implementation of **Deep Learning**, **Computer Vision**, **MediaPipe Pose Estimation**, and **Real-Time Human Activity Recognition**.

ActiVision AI showcases the complete AI development lifecycle—from collecting pose data and training deep learning models to deploying an interactive Flask application capable of recognizing human activities in real time.

---

# ⭐ If you found this project useful, consider giving it a star!

```
⭐ Star this repository if you like the project!
```
