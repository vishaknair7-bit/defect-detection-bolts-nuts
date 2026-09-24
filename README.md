# Bolt & Nut Defect Detection

A computer vision project for detecting defects in bolts and nuts using **deep-learning-based object detection**, with **OpenCV** used for initial classical computer vision experiments.

## 📌 Project Overview

The project started with traditional image-processing techniques to identify bolt and nut defects. After evaluating the limitations of rule-based methods, the approach was extended to a deep-learning object detection model trained and deployed using **Roboflow** and **Python**.

The project demonstrates the transition from classical computer vision to machine-learning-based inspection for industrial components.

## 🛠️ Technologies Used

* Python
* OpenCV
* Roboflow
* Object Detection
* Convolutional Neural Networks
* Canny Edge Detection
* HSV Color Masking
* Contour Detection

## 📊 Dataset & Model

* **Dataset:** 70 annotated high-resolution images
* **Application:** Bolt and nut defect detection
* **Annotation & Training:** Roboflow
* **Inference:** Python using the Roboflow Inference SDK

🔗 **Roboflow Dataset & Model:**
https://app.roboflow.com/vishak-nair/nut-bolt-detection-z8v1u/3

> The dataset contains different bolt and nut configurations and defect conditions to provide variation during model training and testing.

## 🔬 Development Approach

### Phase 1 — Classical Computer Vision

The initial approach used traditional OpenCV techniques:

* Canny edge detection
* HSV color masking
* Contour detection
* Contour filtering based on geometric properties

These methods were useful for understanding the structure and appearance of the components.

However, the rule-based approach had limitations when dealing with:

* Changes in lighting
* Surface reflections
* Different bolt geometries
* Background variations
* Complex defect patterns

Because the detection logic depended heavily on manually selected image-processing parameters, it was difficult to generalize across different samples.

### Phase 2 — Deep Learning Object Detection

To improve generalization, the project was moved to a deep-learning-based object detection approach.

The workflow included:

1. Collecting bolt and nut images
2. Annotating objects and defect conditions
3. Preparing the dataset using Roboflow
4. Training an object detection model
5. Testing the trained model on new images
6. Running inference through Python
7. Visualizing detections using bounding boxes

This approach provides a more flexible method for detecting defects across different component configurations and imaging conditions.

## 📁 Project Structure

```text
defect-detection-bolts-nuts/
│
├── opencv_baseline/
│   └── boltsprac.py
│       # Classical computer vision experiments
│       # Canny, HSV masking and contour detection
│
├── script8.py
│   # Main deep-learning inference script
│
├── test_bolt.jpg
│   # Sample input image
│
├── result.jpg
│   # Detection output
│
├── .gitignore
│
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd defect-detection-bolts-nuts
```

### 2. Install dependencies

```bash
pip install inference-sdk opencv-python
```

### 3. Configure the model

Update the required Roboflow model/API configuration in `script8.py`.

### 4. Run the detection script

```bash
python script8.py
```

The script processes the input image and generates the detection result with bounding boxes.

## 🖼️ Example

### Input

`test_bolt.jpg`

### Detection Output

`result.jpg`

The output image displays the detected bolt/nut regions and the corresponding predicted defect classes.

## 🚀 Future Improvements

* Increase the dataset size and diversity
* Add more defect categories
* Capture images under controlled industrial lighting conditions
* Test the model on real-time camera/video input
* Improve detection performance for small surface defects
* Integrate the model with an automated inspection system
* Explore deployment on an edge device for real-time inspection

## 🎯 Learning Outcomes

Through this project, I explored:

* Classical computer vision techniques using OpenCV
* Image preprocessing and contour-based detection
* Dataset annotation and augmentation
* Deep-learning-based object detection
* Model inference using Python
* The practical challenges of applying computer vision to industrial inspection

## 👨‍💻 Author

**Vishak Nair**

Mechanical Engineer | Computer Vision & Physical AI
