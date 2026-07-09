# 🏃 ActiVision AI — Real-Time Human Activity Recognition Using Deep Learning

ActiVision AI is a Flask-based Human Activity Recognition (HAR) system that combines MediaPipe pose estimation and deep learning to recognize human activities in real time using a laptop webcam. The project demonstrates an end-to-end AI pipeline from pose detection and feature extraction to model training, inference, and deployment through an interactive web application.

---

# ✨ Project Highlights

- 🏃 Real-Time Human Activity Recognition
- 📹 Webcam-Based Activity Detection
- 🦴 MediaPipe Pose Estimation
- 🧠 Deep Learning-Based Classification
- ⚡ Live Prediction Pipeline
- 🌐 Flask Web Application
- 📊 Benchmark Evaluation on UCI HAR & UCF101

---

# 🚀 Tech Stack

<p align="left">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

</p>

---

# 📌 Key Features

- 🎥 Real-time human activity recognition using a laptop camera
- 🦴 Human pose estimation using MediaPipe
- 📍 Body landmark extraction for movement analysis
- 🧠 Deep learning-based activity classification
- ⚡ Live prediction from webcam feed
- 🌐 Flask-powered interactive web application
- 📊 Modular pipeline for data collection, training, and inference
- 💾 Trained model integration for instant predictions
- 🎯 User-friendly browser interface

---

# 🏃 Supported Activities

ActiVision AI is capable of recognizing the following human activities in real time:

- 🚶 Walking
- 🏃 Running
- 🧍 Standing
- 🤸 Jumping
- 👋 Waving
- 🏋️ Squatting

---

# 🧠 Deep Learning Workflow

ActiVision AI follows a complete machine learning pipeline for recognizing human activities.

| Stage | Description |
|--------|-------------|
| 📹 Data Collection | Captures pose landmarks using MediaPipe |
| 📍 Feature Extraction | Converts body landmarks into numerical features |
| 🧹 Data Processing | Cleans and prepares training data |
| 🧠 Model Training | Trains deep learning activity classification models |
| 💾 Model Integration | Loads trained model for inference |
| ⚡ Inference | Predicts activities from live camera input |

---

# 🦴 Why MediaPipe?

MediaPipe was selected for pose estimation because it provides fast and lightweight real-time human pose tracking with 33 body landmarks. Its efficiency enables accurate webcam-based activity recognition without requiring specialized hardware, making it well suited for real-time inference on standard laptops.

---

# 🧠 Model Architectures

The project experiments with several deep learning architectures.

| Model | Purpose |
|--------|---------|
| CNN | Learns spatial movement features |
| LSTM | Learns temporal relationships between frames |
| GRU | Efficient sequential learning with fewer parameters |
| RNN | Basic sequential activity modeling |
| CNN-LSTM | Combines spatial and temporal learning |

---

# 📚 Datasets

The deep learning models were trained and evaluated using widely recognized human activity recognition benchmark datasets.

| Dataset | Description |
|----------|-------------|
| **UCI HAR** | Smartphone sensor-based dataset containing accelerometer and gyroscope readings collected from 30 participants performing 6 daily activities. |
| **UCF101** | Large-scale real-world video dataset containing 13,000+ videos across 101 human action categories, commonly used for action recognition research. |

---

# 🧪 Model Performance

Multiple deep learning architectures were trained and evaluated on both the **UCI HAR** and **UCF101** benchmark datasets to determine the most suitable model for real-time human activity recognition.

| Model | UCI HAR Training | UCI HAR Test | UCF101 Training | UCF101 Test |
|--------|-----------------:|-------------:|----------------:|------------:|
| Single Layer LSTM | 95.76% | 90.46% | 80.03% | 80.39% |
| Two Layer LSTM | 96.18% | 91.21% | 80.03% | 78.43% |
| Single Layer RNN | 71.10% | 66.07% | 84.30% | 90.20% |
| Two Layer RNN | 53.29% | 51.88% | 85.67% | 82.35% |
| Single Layer GRU | 95.97% | 92.77% | 81.74% | 90.20% |
| Two Layer GRU | 95.80% | 91.14% | 92.49% | 83.33% |
| Single Layer CNN | **98.61%** | 90.91% | **98.63%** | **94.12%** |
| Two Layer CNN | 95.69% | 91.92% | 97.27% | 89.22% |
| Hybrid CNN-LSTM | 95.51% | 91.41% | 80.89% | 76.47% |

The following benchmark results summarize the performance of different deep learning architectures evaluated during the research and development of ActiVision AI.

### ✅ Final Model Selection

- **Single Layer GRU** achieved the highest test accuracy (**92.77%**) on the **UCI HAR** dataset, making it well suited for sensor-based activity recognition.
- **Single Layer CNN** achieved the highest test accuracy (**94.12%**) on the **UCF101** dataset, making it the preferred model for video-based human activity recognition.
- The **CNN-LSTM** architecture demonstrated promising performance in combining spatial and temporal information but introduced additional computational complexity compared to standalone CNN and GRU models.

---

# ⚙️ Prediction Pipeline

```text
🎥 Live Camera Feed
        │
        ▼
🦴 MediaPipe Pose Estimation
        │
        ▼
📍 Body Landmark Extraction
        │
        ▼
🧹 Feature Vector Generation
        │
        ▼
🧠 Trained CNN Model
        │
        ▼
🏃 Activity Classification
        │
        ▼
📺 Real-Time Prediction
```

---

# ⚙️ Development Workflow

## 📌 Data Collection

- Captures live webcam frames
- Detects human pose using MediaPipe
- Extracts body landmark coordinates
- Converts movements into structured numerical data
- Stores activity samples for model training

---

## 📌 Data Processing & Feature Extraction

- Cleans collected landmark data
- Prepares activity datasets
- Converts landmarks into model-ready feature vectors
- Organizes samples by activity class

---

## 📌 Model Training

- Loads processed datasets
- Builds deep learning models
- Trains activity classification networks
- Evaluates model performance
- Saves trained model as:

```text
model.h5
```

Stores activity labels as:

```text
labels.npy
```

---

## 📌 Inference

- Loads the trained model
- Captures live webcam frames
- Extracts body landmarks
- Performs activity classification
- Displays prediction in real time

---

## 📌 Flask Web Application

The Flask backend connects the trained deep learning model with the frontend.

Responsibilities include:

- Handling routes
- Managing prediction requests
- Connecting webcam inference
- Displaying activity predictions
- Rendering the user interface

---

# 📂 Repository Structure

```text
HUMAN_ACTIVITY_FINAL/
│
├── app.py
│   └── Flask application entry point that manages routes,
│       user requests, and real-time activity prediction.
│
├── data_collection.py
│   └── Captures pose landmarks using MediaPipe and
│       generates datasets for model training.
│
├── data_training.py
│   └── Performs data preprocessing, feature preparation,
│       model training, and saves the trained model.
│
├── inference.py
│   └── Loads the trained model and performs
│       real-time human activity recognition.
│
├── model.h5
│   └── Pre-trained deep learning model used for activity recognition.
│
├── labels.npy
│   └── Stores activity labels used during inference.
│
├── requirements.txt
│   └── Python dependencies required to run the project.
│
├── templates/
│   ├── home.html      # Activity recognition dashboard
│   └── login.html     # User login interface
│
├── static/
│   ├── bg.jpg
│   └── styles/
│       └── Static assets including CSS, images, and frontend resources.
│
├── Snapshots/
│   ├── Snap-11.png
│   ├── Snap-22.png
│   └── Snap-33.jpg
│
└── README.md
    └── Project documentation.
```

---

# ▶️ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sai-2410/HAR.git
```

Move into the project directory:

```bash
cd HUMAN_ACTIVITY_FINAL
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

After activation:

```text
(venv) C:\Users\User\HUMAN_ACTIVITY_FINAL>
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run the Flask Application

```bash
python app.py
```

---

## 6️⃣ Open the Application

Visit:

```text
http://127.0.0.1:5000/
```

The browser will open the ActiVision AI application and begin real-time activity recognition using your laptop camera.

---

# 📸 Project Snapshots

| Screenshot | Description |
|------------|-------------|
| ![](Snapshots/Snap-11.png) | Login Page |
| ![](Snapshots/Snap-22.png) | Home Dashboard |
| ![](Snapshots/Snap-33.jpg) | Real-Time Activity Prediction |

---

# 🎥 Project Demo

> 🎬 A demonstration video showcasing real-time activity recognition will be added soon.

---

# 💡 Skills Demonstrated

### 🤖 AI & Machine Learning
- Deep Learning
- Computer Vision
- Human Pose Estimation
- Feature Engineering
- Dataset Preparation

### 📚 Frameworks & Libraries
- TensorFlow
- Keras
- OpenCV
- MediaPipe
- Flask

### 💻 Software Development
- Backend & Frontend Integration
- Real-Time Video Processing
- AI Model Deployment

### 🛠️ Tools & Deployment
- Git & GitHub
- Python Virtual Environments
- Package Management (`pip`)
- Model Serialization (`.h5`)
- Flask Development Server

---

# 🚀 Future Improvements

- Support additional activity classes
- Improve accuracy with larger datasets
- Explore Vision Transformers (ViT) & Transformer-based architectures for improved activity recognition
- Enhance low-light detection
- Handle partial body occlusion
- Deploy on cloud platforms
- Develop a mobile application
- Optimize for edge devices
- Add activity history and analytics
- Integrate Explainable AI (XAI)

---

# ⚠️ Current Limitations

- Supports single-person activity recognition only
- Requires clear visibility of the human body
- Performance may decrease under poor lighting conditions
- Similar activities may occasionally be misclassified
- Accuracy depends on webcam quality and camera positioning

---

# 🏅 Recognition

- **KSCST State-Level Poster Presentation:** The project was presented at the Karnataka State Council for Science and Technology (KSCST) State-Level Poster Presentation.
- **Research Publication:** A research paper based on the proposed Human Activity Recognition system was prepared and submitted, highlighting the use of deep learning and computer vision for real-time activity recognition.

---

# 👥 Contributors

This project was developed collaboratively by:

| Contributor | Responsibilities |
|-------------|-----------------------|
| **Sai Ravi Chandran** | Designed and developed the frontend, built the Flask backend, integrated the trained deep learning model, implemented real-time inference, contributed to feature engineering, tested the complete application, and deployed the end-to-end system. |
| **Sirisha V Ramana** | Performed data collection, exploratory data analysis (EDA), data preprocessing, contributed to feature engineering, trained and evaluated multiple deep learning models, optimized model performance, and selected the final activity recognition model. |

---

# 📝 Project Note

> **ActiVision AI** was developed collaboratively as a **final-year engineering project** to demonstrate the practical application of **Deep Learning**, **Computer Vision**, **Human Pose Estimation**, and **Real-Time Human Activity Recognition**.

The project showcases an end-to-end AI pipeline, from pose estimation and model training to real-time activity recognition through a Flask-based web application.

---
