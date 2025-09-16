# Image Color Histogram

A Python application for analyzing and visualizing color distributions in images by creating histograms for Red, Green, and Blue channels. This project demonstrates fundamental computer vision concepts and image processing techniques.

## Requirements

### Python Dependencies

The following Python packages are required to run this application:

```
numpy>=1.21.0
opencv-python>=4.5.0
matplotlib>=3.5.0
```

### System Requirements

- Python 3.7 or higher
- Operating System: Windows, macOS, or Linux
- Minimum 4GB RAM (recommended for large images)

## Installation

### Method 1: Using pip (Recommended)

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd Image-color-histogram
   ```

2. Install the required dependencies:
   ```bash
   pip install numpy opencv-python matplotlib
   ```

### Method 2: Using requirements.txt

1. Create a requirements.txt file with the following content:
   ```
   numpy>=1.21.0
   opencv-python>=4.5.0
   matplotlib>=3.5.0
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Method 3: Using conda

```bash
conda install numpy opencv matplotlib
```

## Usage

### Basic Usage

1. Run the script:
   ```bash
   python CV-1-07.py
   ```

2. Enter the path to your image when prompted:
   ```
   Enter image path: path/to/your/image.jpg
   ```

3. The application will display three histograms showing the color distribution for Red, Green, and Blue channels.

### Supported Image Formats

The application supports all image formats that OpenCV can read, including:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)

## Implementation Details

### Core Functions

- `load_img_color(img_path)`: Loads color images with error handling
- `plot_color_histograms(img)`: Creates and displays RGB channel histograms
- `main()`: Handles user input and orchestrates the workflow

## Examples

### Sample Output
<img width="300" alt="icon" src="https://github.com/user-attachments/assets/58e1c54e-9081-4c03-8399-f55b8d1745e2" />
<img width="600" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/ef15c59a-99d8-4b71-ae17-b008719f39cc" />

## Educational Context

**Novosibirsk State University (NSU)**  
**Bachelor's Program**: 15.03.06 - Mechatronics and Robotics (AI Profile)

*Project Activity Course - Task 1*  
*Computer Vision Algorithms in Python*

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is part of an educational curriculum at Novosibirsk State University.

