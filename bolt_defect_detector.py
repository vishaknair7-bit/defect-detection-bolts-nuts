import base64
import os
import cv2
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv(override=True)

API_KEY = os.getenv("ROBOFLOW_API_KEY")

if not API_KEY:
  raise ValueError("ROBOFLOW_API_KEY is missing from your .env file!")

ENDPOINT = "https://detect.roboflow.com/nut-bolt-detection-z8v1u/3"

# Folders
input_folder = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\defect-detection-bolts-nuts\input_folder"
output_folder = os.path.join(input_folder, "results")
os.makedirs(output_folder, exist_ok=True)

# Loop through images
for filename in os.listdir(input_folder):
  if (
      filename.lower().endswith((".jpg", ".jpeg", ".png"))
      and not filename.startswith("result_")
  ):

    image_path = os.path.join(input_folder, filename)
    print(f"\nProcessing: {filename}")

    img = cv2.imread(image_path)
    if img is None:
      continue

    orig_h, orig_w = img.shape[:2]
    img_resized = cv2.resize(img, (600, 700))

    with open(image_path, "rb") as f:
      encoded = base64.b64encode(f.read()).decode("utf-8")

    response = requests.post(
        ENDPOINT,
        params={"api_key": API_KEY},
        data=encoded,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    result = response.json()

    if "predictions" not in result:
      print(f"  API Output: {result}")
      continue

    predictions = result.get("predictions", [])

    if len(predictions) > 0:
      for pred in predictions:
        x = int(pred["x"] * (600 / orig_w))
        y = int(pred["y"] * (700 / orig_h))
        w = int(pred["width"] * (600 / orig_w) / 2)
        h = int(pred["height"] * (700 / orig_h) / 2)
        label = pred["class"]
        confidence = pred["confidence"]

        if confidence > 0.40:
          cv2.rectangle(
              img_resized, (x - w, y - h), (x + w, y + h), (0, 255, 0), 3
          )
          cv2.putText(
              img_resized,
              f"{label} {confidence:.0%}",
              (x - w, max(y - h - 10, 20)),
              cv2.FONT_HERSHEY_SIMPLEX,
              0.8,
              (0, 255, 0),
              2,
          )
        else:
          cv2.putText(
              img_resized,
              "LOW CONFIDENCE - CHECK MANUALLY",
              (20, 50),
              cv2.FONT_HERSHEY_SIMPLEX,
              0.7,
              (0, 0, 255),
              2,
          )

      print(f"  Found {len(predictions)} objects")
    else:
      cv2.putText(
          img_resized,
          "NO OBJECTS FOUND - CHECK MANUALLY",
          (20, 50),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.7,
          (0, 0, 255),
          2,
      )
      print("  No detections")

    output_path = os.path.join(output_folder, f"result_{filename}")
    cv2.imwrite(output_path, img_resized)
    print(f"  Saved: {output_path}")

print("\nProcessing finished!")