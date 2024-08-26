import argparse
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

def main(image_path):

    model = YOLO(r"D:\project\yolov8-osteo-arthritis.pt")


    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB


    results = model(img)


    boxes = results[0].boxes.xyxy.cpu().numpy()  
    scores = results[0].boxes.conf.cpu().numpy()  
    classes = results[0].boxes.cls.cpu().numpy()  


    plt.imshow(img)
    ax = plt.gca()

    for box, score, cls in zip(boxes, scores, classes):
        x1, y1, x2, y2 = box
        width, height = x2 - x1, y2 - y1
        rect = plt.Rectangle((x1, y1), width, height, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.text(x1, y1, f'{model.names[int(cls)]} {score:.2f}', color='yellow', fontsize=12, bbox=dict(facecolor='black', alpha=0.5))

    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 Object Detection")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()
    main(args.image_path)

