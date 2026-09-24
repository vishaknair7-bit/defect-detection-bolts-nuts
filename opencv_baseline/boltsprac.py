import cv2
import numpy as np
import os

input_folder = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\resources\bolt data\input_folder"
output_folder = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\resources\bolt data\output_folder"
canny_img = r"C:\Users\Vishak\Documents\GITHUB FILES\computer vision\resources\bolt data\canny_img"
os.makedirs(output_folder, exist_ok=True)
os.makedirs(canny_img, exist_ok=True)

min_area = 500

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    path = os.path.join(input_folder, filename)
    img = cv2.imread(path)
    if img is None:
        print(f"{filename}: could not read")
        continue

    img = cv2.resize(img, (600, 700))

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray, (9, 9), 0)
    imgcanny = cv2.Canny(imgblur, 100, 200)

    kernel = np.ones((3, 3), np.uint8)
    imgdilate = cv2.dilate(imgcanny, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(
        imgdilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    img_contours = img.copy()
    detections_found = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > min_area:
            detections_found += 1
            cv2.drawContours(img_contours, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)

            if area > 15000:
                label, color = "NUT DETECTED", (0, 255, 0)
            elif area > 3000:
                label, color = "THREADS EXPOSED", (0, 0, 255)
            else:
                label, color = "NOISE", (255, 165, 0)

            cv2.putText(img_contours, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            cv2.rectangle(img_contours, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # save instead of imshow
    out_path = os.path.join(output_folder, filename)
    cv2.imwrite(out_path, img_contours)
    cv2.imwrite(os.path.join(canny_img, "edges_" + filename), imgcanny)

    print(f"{filename}: {detections_found} detections found")

