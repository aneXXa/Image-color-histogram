import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os


def load_img_color(img_path: str) -> np.ndarray:
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    if img is None:
        return None
    return img


def plot_color_histograms(img: np.ndarray) -> None:
    # creates plot environment with 3 axes for three colours
    fig, axes = plt.subplots(1, 3, figsize=(12, 6), constrained_layout=True)
    
    channels = [
        (2, "r", "Red"),
        (1, "g", "Green"),
        (0, "b", "Blue"),
    ]
    # plots histograms for each channel
    for ax, (channel_idx, color, title) in zip(axes, channels):
        hist = cv.calcHist([img], [channel_idx], None, [256], [0, 256])

        ax.hist(range(256), bins=32, weights=hist.flatten(), color=color, alpha=0.7, density=True)
        ax.set_title(f"{title} channel")
        ax.set_xlabel("Pixel value")
        ax.set_ylabel("Frequency")
    
    plt.show()


def main() -> None:
    src = input("Enter image path: ")
    #input validation
    if not src:
        raise ValueError("Image path cannot be empty.")
    if not os.path.isfile(src):
        raise ValueError(f"File '{src}' does not exist.")

    img = load_img_color(src)

    if img is None:
        raise ValueError(f"Could not open image: {src}")
    
    plot_color_histograms(img)

if __name__ == "__main__":
    main()