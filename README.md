# 🏃 ActiVision AI – Real-Time Human Activity Recognition Using Deep Learning

A Flask-based Human Activity Recognition system that uses computer vision and deep learning to identify human activities in real time through a laptop camera.

ActiVision AI uses MediaPipe for extracting human body landmarks from live video input and a trained deep learning model to classify different human activities. The system captures movement patterns, processes the extracted features, and displays the predicted activity through an interactive web-based interface.

The project demonstrates an end-to-end AI workflow including human pose detection, feature extraction, deep learning model integration, and real-time activity prediction.

---

# 🚀 Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white)](https://keras.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?logo=google&logoColor=white)](https://developers.google.com/mediapipe)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

# 🏗 Workflow & Activity Recognition Pipeline

```
🎥 Laptop Camera / Video Input
              ↓
🦴 MediaPipe Pose Detection
              ↓
📍 Human Body Landmark Extraction
              ↓
🧹 Feature Processing & Data Preparation
              ↓
🧠 Deep Learning Classification Model
              ↓
📊 Human Activity Prediction
              ↓
🌐 Flask Web Application
              ↓
✅ Activity Displayed To User
```

---

# ✨ Core Features

- Real-time human activity recognition using laptop camera input  
- Human pose detection using MediaPipe framework  
- Body landmark extraction for movement analysis  
- Deep learning based activity classification  
- Flask-based interactive web application  
- Real-time prediction from live video feed  
- Modular pipeline for data collection, training, and inference  
- Trained model integration for instant activity recognition  
- User-friendly interface for interacting with the AI system  

ActiVision AI provides a complete computer vision pipeline where human movements are captured, analyzed, and classified into different activity categories using deep learning techniques.

---

# 🧪 Deep Learning Models & Implementation

ActiVision AI uses deep learning techniques to recognize human activities by learning patterns from extracted body movement features.

The project follows a complete machine learning workflow:

| Stage | Description |
|--------|-------------|
| Data Collection | Captures human pose landmarks using MediaPipe and camera input |
| Feature Extraction | Converts body movements into numerical landmark features |
| Data Processing | Prepares and formats activity data for model training |
| Model Training | Trains deep learning classification models |
| Model Integration | Loads trained model for real-time prediction |
| Inference | Classifies live human activities from camera input |

---

# 🧠 Model Architecture

The system experiments with deep learning architectures for activity recognition:

| Model | Purpose |
|--------|---------|
| CNN | Extracts spatial patterns from movement features |
| LSTM | Learns temporal relationships in activity sequences |
| GRU | Provides efficient sequence learning with lower complexity |
| RNN | Basic sequential learning approach |
| CNN-LSTM | Combines spatial and temporal feature learning |

---

# ✅ Final Prediction Pipeline


Live Camera Frame
        ↓
MediaPipe Pose Landmark Detection
        ↓
Feature Extraction
        ↓
Trained Deep Learning Model
        ↓
Activity Classification
        ↓
Real-Time Result Display

---

# ⚙️ Development Workflow

## 📌 Data Collection Module

- Captures real-time video input through laptop camera
- Uses MediaPipe to detect human body landmarks
- Extracts body joint coordinates from detected poses
- Converts human movement into structured numerical data
- Stores collected activity samples for training

---

## 📌 Data Processing & Feature Extraction

- Processes collected pose landmark data
- Cleans and prepares activity samples
- Converts movement patterns into model-ready features
- Organizes data based on activity classes

---

## 📌 Model Training Module

- Uses processed activity data for deep learning training
- Builds and trains activity classification models
- Evaluates model performance
- Saves trained model as `model.h5`
- Stores activity labels using `labels.npy`

---

## 📌 Inference Module

- Loads the trained deep learning model
- Receives live camera input
- Extracts real-time pose features using MediaPipe
- Performs activity classification
- Displays predicted activity instantly

---

## 📌 Web Application Integration

- Flask connects the trained AI model with the frontend
- Handles user requests and prediction flow
- Provides browser-based interaction
- Displays real-time activity recognition results

---

# 📂 Repository Structure

HUMAN_ACTIVITY_FINAL/

│
├── app.py
│   └── Main Flask application
│       Handles routes, user interaction, and activity prediction
│
├── data_collection.py
│   └── Collects human pose data using MediaPipe
│       Extracts body landmark coordinates from camera input
│
├── data_training.py
│   └── Processes collected data
│       Trains the deep learning activity classification model
│
├── inference.py
│   └── Loads trained model
│       Performs real-time activity prediction
│
├── model.h5
│   └── Saved trained deep learning model
│
├── labels.npy
│   └── Stores activity class labels
│
├── requirements.txt
│   └── Contains all required Python dependencies
│
├── templates/
│
│   ├── home.html
│   │   └── Main application interface
│   │
│   └── login.html
│       └── User authentication page
│
├── static/
│
│   ├── bg.jpg
│   │   └── Background assets
│   │
│   └── styles/
│       └── CSS files and frontend styling
│
├── Snapshots/
│   └── Project screenshots
│
└── README.md

---

# ▶️ Running The Application

## 1. Clone Repository

git clone https://github.com/IgrisViOverlord-10/laughing-dollop.git

Move into the project folder:

cd HUMAN_ACTIVITY_FINAL

2. Create Virtual Environment

Create a Python virtual environment:

python -m venv venv

3. Activate Virtual Environment
Windows:
venv\Scripts\activate

After successful activation:

(venv) C:\Users\User\HUMAN_ACTIVITY_FINAL>

4. Install Dependencies

Install all required libraries:

pip install -r requirements.txt
5. Run Flask Application

Start the application:

python app.py
6. Open Website

After starting the Flask server, open:

http://127.0.0.1:5000/

The ActiVision AI web application will open in the browser and allow real-time human activity recognition using the laptop camera.

---

# 📸 Project Snapshots

| Screenshot | Description |
|------------|-------------|
| ![Login Page](Snapshots/Snap-1.png) | User login interface |
| ![Home Page](Snapshots/Snap-2.png) | ActiVision AI main dashboard |
| ![Activity Prediction](Snapshots/Snap-3.png) | Real-time human activity recognition output |


---

# 🧠 Skills Demonstrated

- Deep Learning model implementation  
- Computer Vision application development  
- Human Pose Estimation using MediaPipe  
- Real-time video processing using OpenCV  
- Data collection and feature extraction  
- Neural network training and model integration  
- Machine Learning workflow development  
- Flask-based web application development  
- Backend and frontend integration  
- Real-time AI inference systems  
- Model deployment and optimization  


---

# 🔮 Future Improvements

- Support recognition of a larger number of human activities  
- Improve model accuracy using larger and more diverse datasets  
- Implement advanced deep learning architectures such as Transformers  
- Improve detection under low lighting and complex backgrounds  
- Handle partial body visibility and occlusion scenarios  
- Deploy the application on cloud platforms  
- Develop a mobile application version  
- Optimize the model for edge devices and real-time deployment  
- Add activity history tracking and analytics dashboard  
- Integrate explainable AI techniques for better prediction understanding  

---

# 🏁 Project Note

> This project was developed as a final year academic project to demonstrate the practical implementation of deep learning, computer vision, human pose estimation, and real-time activity recognition using a Flask-based web application.

ActiVision AI showcases the complete AI development lifecycle — from collecting human movement data and training deep learning models to deploying a real-time recognition system that works through a laptop camera.
