# 🏗️ AI-Based Quantity Surveyor Assistant

An AI-powered construction estimation system that analyzes building floor plans and automatically estimates area, material requirements, and construction costs using Computer Vision and Machine Learning techniques.

## 📌 Overview

Quantity surveying is a critical part of construction planning, but manual estimation can be time-consuming and prone to errors. This project automates the estimation process by extracting structural information from floor plan images and generating material and cost estimates.

The system uses image processing techniques to detect walls and building regions, converts pixel measurements into real-world dimensions, estimates construction materials, predicts costs, and generates downloadable PDF reports.

---

## 🚀 Features

✅ Upload building floor plan images

✅ Computer Vision-based structural analysis

✅ Edge detection using Canny Edge Detection

✅ Contour detection for area estimation

✅ Real-world area calculation using scaling factors

✅ Material estimation:

* Cement
* Bricks
* Steel

✅ Construction cost estimation

✅ Machine Learning-based cost prediction

✅ Automated PDF report generation

✅ Interactive Streamlit dashboard

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Computer Vision

* OpenCV
* NumPy

### Machine Learning

* Scikit-Learn
* Linear Regression

### Data Processing

* Pandas

### Visualization & Interface

* Streamlit
* Matplotlib

### Reporting

* ReportLab

---

## 🏗️ System Workflow

1. Upload Floor Plan Image
2. Preprocess Image
3. Detect Edges and Contours
4. Calculate Pixel Area
5. Convert Pixel Measurements to Real-World Dimensions
6. Estimate Materials
7. Estimate Construction Cost
8. Predict Cost using Machine Learning
9. Generate PDF Report

---

## 📂 Project Structure

```text
AI-Quantity-Surveyor-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── cost_data.csv
│   ├── floor-plan1.png
│   └── floor-plan2.jpg
│
└── utils/
    ├── image_processing.py
    ├── estimation.py
    ├── ml_model.py
    └── report.py
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/DEEPIKA-SHANMUGAM22/AI-Quantity-Surveyor-Assistant.git
cd AI-Quantity-Surveyor-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎥 Demo Video

Watch the complete project demonstration:

[▶️ Demo Video] https://drive.google.com/file/d/1Do2LWf1bSkjNdbO6BWctHLrp9T9ZYUc8/view?usp=sharing

---

## 📊 Sample Output

### Material Estimation

| Material | Estimated Quantity |
| -------- | ------------------ |
| Cement   | XX Bags            |
| Bricks   | XXXX               |
| Steel    | XXX Kg             |

### Cost Estimation

| Category       | Cost   |
| -------------- | ------ |
| Material Cost  | ₹XXXXX |
| Labour Cost    | ₹XXXXX |
| Finishing Cost | ₹XXXXX |
| Total Cost     | ₹XXXXX |

---

## 🔮 Future Enhancements

* Multi-floor building estimation
* Automatic scale detection
* BIM integration
* Deep Learning-based floor plan recognition
* Cloud deployment
* Mobile application support
* Advanced quantity takeoff system

---

## 👩‍💻 Author

**Deepika S**

BE CSE (AI & ML)

KPR Institute of Engineering and Technology

GitHub: https://github.com/DEEPIKA-SHANMUGAM22

LinkedIn: https://linkedin.com/in/deepikashanmugasundaram

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
