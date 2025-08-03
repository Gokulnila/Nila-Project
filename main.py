from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Smallest and fastestpy main.py
# Paths to 4 images (simulate 4 junctions)
image_paths = {
    "North": "junction1.jpg",
    "East": "junction2.jpg",
    "South": "junction3.jpg",
    "West": "junction4.jpg"
}

vehicle_classes = ["car", "motorbike", "bus", "truck"]
vehicle_counts = {}

# Loop through each junction image
for direction, path in image_paths.items():
    img = cv2.imread(path)
    results = model(img, verbose=False)[0]

    count = 0
    for r in results.boxes.data:
        class_id = int(r[5])
        class_name = model.names[class_id]
        if class_name in vehicle_classes:
            count += 1

    vehicle_counts[direction] = count
    print(f"{direction} - Vehicles detected: {count}")

# Decide who gets the green light (max vehicles)
max_direction = max(vehicle_counts, key=vehicle_counts.get)
print("\n🚦 Green signal given to:", max_direction)
