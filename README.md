Markdown# 🔩 Bolt & Nut Defect Detection Pipeline

An industrial-grade computer vision and physical AI inspection pipeline for detecting defects in bolts and nuts. This project transitions from **classical rule-based OpenCV experiments** to a **deep-learning model hosted on Roboflow**, finalized with a **Google Gemini LLM Output Alignment Layer** for automated quality control (QC) reporting.

---

## 📌 Project Overview

Traditional computer vision techniques struggle with real-world manufacturing variables like glare, rust, background noise, and varying camera angles. This project demonstrates a multi-stage approach to overcome those limitations:

1. **Phase 1 — Classical OpenCV Baseline:** Uses Canny Edge Detection, Gaussian Blurring, and contour extraction to analyze physical bolt geometry.
2. **Phase 2 — Deep Learning Object Detection:** Employs a trained object detection model hosted on Roboflow for dynamic bounding box and confidence score predictions.
3. **Phase 3 — Google Gemini Output Alignment:** Passes raw computer vision data into Google Gemini using strict System Instructions and JSON Schema to output machine-readable `PASSED`, `REJECTED`, or `MANUAL_INSPECTION_REQUIRED` verdicts.

---

## 🛠️ Tech Stack & Tools

- **Programming Language:** Python 3.10+
- **Computer Vision:** OpenCV (`cv2`)
- **Cloud Model Hosting:** Roboflow API
- **Generative AI Alignment:** Google Gemini API (`gemini-2.5-flash`)
- **Environment Management:** `python-dotenv`
- **Networking & API:** `requests`, `base64`

---

## 📁 Repository Structure

```text
defect-detection-bolts-nuts/
│
├── opencv_baseline/
│   └── opencv_baseline_detector.py # Classical CV (Gaussian Blur, Canny Edges)[cite: 1, 3, 4]
│
├── input_folder/                   # Directory containing test images for batch processing
│   ├── test_bolt.jpg
│   └── result_test_bolt.jpg        # Output with green boxes / confidence labels
│
├── .env.example                    # Template for required API keys
├── .gitignore                      # Excludes secrets (.env) & temporary result images
├── main.py                         # Complete pipeline (Roboflow + Gemini Alignment)
├── requirements.txt                # Project dependencies[cite: 1]
└── README.md                       # Project documentation[cite: 1]

⚙️ Installation & Setup1. Clone the RepositoryBashgit clone [https://github.com/vishaknair7-bit/defect-detection-bolts-nuts.git](https://github.com/vishaknair7-bit/defect-detection-bolts-nuts.git)
cd defect-detection-bolts-nuts
2. Install DependenciesBashpip install -r requirements.txt
3. Configure API CredentialsCopy the example environment file and add your private API keys:Bashcp .env.example .env
Edit .env and fill in your keys:Code snippetROBOFLOW_API_KEY=your_actual_roboflow_key
GEMINI_API_KEY=your_actual_gemini_key

⚠️ Security Note: Never commit your .env file to version control. It is automatically ignored via .gitignore[cite: 1].🚀 How to RunBatch Folder InspectionPlace your target bolt images into the input_folder/ directory and run:Bashpython main.py
What happens during execution:Directory Scanning: Scans input_folder/ for valid image formats (.jpg, .png)[cite: 1].Dynamic Coordinate Calculation: Scales bounding boxes based on screen geometry regardless of input image resolution.   Roboflow Inference: Sends Base64 image payload to Roboflow API to detect nuts/bolts and defects.   Gemini Alignment Report: Formats prediction arrays into a strict, structured JSON quality report:JSON{
  "defect_verdict": "REJECTED",
  "overall_confidence": 0.88,
  "detected_defects": [
    {
      "defect_type": "CORROSION",
      "severity": "CRITICAL"
    }
  ],
  "action_item": "Route to reject bin B"
}
Annotation & Saving: Draws bright green boxes for high-confidence predictions (>40%) and red warning banners for low-confidence detections, saving results back to input_folder/ as result_<filename>[cite: 1].🔬 Classical CV vs. Deep Learning Model ComparisonFeaturePhase 1: OpenCV Baseline   PNG+ 1Phase 2 & 3: Deep Learning + Gemini[cite: 1, 3]MethodCanny Edges & Contour Extraction[cite: 1, 3, 4]YOLO/Roboflow + LLM Alignment[cite: 1, 3]Lighting ChangesSensitive to surface reflection/glare   Highly robust   Defect ClassificationRule-based (manually tuned thresholds)   Data-driven multi-class recognition   Output TypeLocal pixel contours[cite: 1, 3]Machine-readable JSON QC Reports[cite: 1, 3]🎯 Future EnhancementsTrain on a larger dataset containing real-world defect categories (cracks, thread damage, notches).   Integrate live webcam/video stream processing using cv2.VideoCapture()[cite: 3].Deploy to an edge computing device (e.g., NVIDIA Jetson / Raspberry Pi) for assembly-line integration[cite: 3].👨‍💻 AuthorVishak NairMechanical Engineer | Computer Vision & Physical AI
