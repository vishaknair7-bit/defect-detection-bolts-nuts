import base64
import os
import cv2
import requests

# Your Roboflow details
API_KEY = "3ZY45jlmoiL3abBeY5JU"
ENDPOINT = "https://detect.roboflow.com/nut-bolt-detection-z8v1u/3"

# Folder containing your test images
folder = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\defect-detection-bolts-nuts\input_folder"

# Loop through every image in folder
for filename in os.listdir(folder):
  if filename.lower().endswith((".jpg", ".jpeg", ".png")):

    image_path = os.path.join(folder, filename)
    print(f"Processing: {filename}")

    # Load image
    img = cv2.imread(image_path)
    if img is None:
      continue

    orig_h, orig_w = img.shape[:2]
    img_resized = cv2.resize(img, (600, 700))

    # Send to Roboflow
    with open(image_path, "rb") as f:
      encoded = base64.b64encode(f.read()).decode("utf-8")

    response = requests.post(
        ENDPOINT,
        params={"api_key": API_KEY},
        data=encoded,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    result = response.json()

    # Draw detections
    if "predictions" in result and len(result["predictions"]) > 0:
      for pred in result["predictions"]:
        x = int(pred["x"] * (600 / orig_w))
        y = int(pred["y"] * (700 / orig_h))
        w = int(pred["width"] * (600 / orig_w) / 2)
        h = int(pred["height"] * (700 / orig_h) / 2)
        label = pred["class"]
        confidence = pred["confidence"]

        # CHECK CONFIDENCE HERE
        if confidence > 0.40:
          # High confidence -> Draw Green Box
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
          # Low confidence -> Draw Red Warning Text
          cv2.putText(
              img_resized,
              "LOW CONFIDENCE - CHECK MANUALLY",
              (20, 50),
              cv2.FONT_HERSHEY_SIMPLEX,
              0.7,
              (0, 0, 255),
              2,
          )

      print(f"  Found {len(result['predictions'])} objects")
    else:
      # Zero objects detected at all
      cv2.putText(
          img_resized,
          "NO OBJECTS FOUND - CHECK MANUALLY",
          (20, 50),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.7,
          (0, 0, 255),
          2,
      )
      print(f"  No detections")

    # Save result image
    output_path = os.path.join(folder, f"result_{filename}")
    cv2.imwrite(output_path, img_resized)
    print(f"  Saved: result_{filename}")

print("\nAll images processed!")