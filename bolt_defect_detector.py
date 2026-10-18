import requests
import base64
import cv2

image_path = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\test_bolt.jpg"

with open(image_path, "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")

response = requests.post(
    "https://detect.roboflow.com/nut-bolt-detection-z8v1u/3",
    params={"api_key": "pNP4brlwFpopG6wR2n2Y"},
    data=encoded,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

result = response.json()

if 'predictions' in result:
    img = cv2.imread(image_path)

    for pred in result['predictions']:
        x = int(pred['x'])
        y = int(pred['y'])
        w = int(pred['width'] / 2)
        h = int(pred['height'] / 2)
        confidence = pred['confidence']
        label = pred['class']

        cv2.rectangle(img, (x - w, y - h), (x + w, y + h), (0, 255, 0), 8)
        cv2.putText(img, f"{label} {confidence:.0%}",
                    (x - w, y - h - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

    # Save result instead of showing
    output_path = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\result.jpg"
    cv2.imwrite(output_path, img)
    print(f"Result saved to: {output_path}")
    print(f"Detected: {len(result['predictions'])} objects")
    for pred in result['predictions']:
        print(f"  {pred['class']} — {pred['confidence']:.0%} confidence")
else:
    print("No detections found")
    print(result)
