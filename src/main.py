import cv2
import torch


def main():
    print("AHC Video Anomaly Detection")
    print("OpenCV version:", cv2.__version__)
    print("PyTorch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))


if __name__ == "__main__":
    main()