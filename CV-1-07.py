import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def load_img_color(img_path):
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    if img is None:
        print(f"Could not open of find the image: {img_path}")
        exit(0)
    return img


def plot_color_histograms(img: np.ndarray) -> None:
    # splits image to the seperate channels BGR
    b, g, r = cv.split(img)

    # creates plot environment with 3 axes for three colours
    fig, axes = plt.subplots(1, 3, figsize=(10, 6), constrained_layout=True)
    channels = [
        (b, "b", "Blue"),
        (g, "g", "Green"),
        (r, "r", "Red"),
    ]

    for ax, (channel, color, title) in zip(axes, channels):
        ax.hist(channel.ravel(), bins=32, color=color, alpha=0.7, density=True)
        ax.set_title(f"{title} channel")

    plt.show()


def main() -> None:
    src = input()
    img = load_img_color(src)
    plot_color_histograms(img)


if __name__ == "__main__":
    main()