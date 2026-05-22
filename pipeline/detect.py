import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")


def process_video(video_path):

    cap = cv2.VideoCapture(video_path)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                if cls == 0:

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

        cv2.imshow("Detection", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()