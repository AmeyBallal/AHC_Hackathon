import cv2


def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    duration = frame_count / fps if fps > 0 else 0

    print("Video:", video_path)
    print("FPS:", fps)
    print("Frames:", frame_count)
    print("Duration:", round(duration, 2), "seconds")

    cap.release()


if __name__ == "__main__":
    print("Video processor is ready.")