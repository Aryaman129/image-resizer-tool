# Image Resizer Tool 🖼️

A powerful and easy-to-use batch image resizing and conversion tool built with Python and Pillow.

## 📋 Features

- **Batch Processing**: Resize multiple images at once
- **Aspect Ratio Control**: Maintain original proportions or force specific dimensions
- **Format Conversion**: Convert between JPEG, PNG, BMP, WebP, TIFF, and more
- **Quality Control**: Adjust compression quality for optimized file sizes
- **Flexible Output**: Add prefixes/suffixes to output filenames
- **Multiple Use Cases**: Perfect for thumbnails, web optimization, or standard resizing

## 🛠️ Technologies Used

- **Python 3.x**
- **Pillow (PIL)** - Python Imaging Library for image processing
- **os module** - File and directory operations
- **argparse** - Command-line interface

## 📁 Project Structure

```
image-resizer-tool/
├── image_resizer.py       # Main script with CLI interface
├── example_usage.py       # Example usage scripts
├── requirements.txt       # Python dependencies
├── sample_images/         # Input images folder
│   └── README.md
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites

Install Python 3.x and the required package:

```bash
pip install -r requirements.txt
```

Or install Pillow directly:

```bash
pip install Pillow
```

### Basic Usage

1. **Place images in a folder** (e.g., `sample_images/`)

2. **Resize to specific width** (maintaining aspect ratio):
   ```bash
   python image_resizer.py -i sample_images -o output -w 800
   ```

3. **Resize to specific dimensions**:
   ```bash
   python image_resizer.py -i sample_images -o output -w 1920 -ht 1080
   ```

4. **Create thumbnails**:
   ```bash
   python image_resizer.py -i sample_images -o thumbnails -w 300 --prefix "thumb_"
   ```

## 📖 Command-Line Options

```
Options:
  -i, --input         Input folder containing images (required)
  -o, --output        Output folder for resized images (required)
  -w, --width         Target width in pixels
  -ht, --height       Target height in pixels
  --no-aspect         Do not maintain aspect ratio
  -q, --quality       Image quality for JPEG (1-100, default: 95)
  -f, --format        Output format (JPEG, PNG, BMP, WEBP, TIFF)
  --prefix            Prefix for output filenames
  --suffix            Suffix for output filenames (before extension)
```

## 💡 Usage Examples

### Example 1: Resize to 800px Width
```bash
python image_resizer.py -i photos -o resized -w 800
```
Resizes all images to 800px width while maintaining aspect ratio.

### Example 2: Fixed Dimensions
```bash
python image_resizer.py -i images -o output -w 1920 -ht 1080 --no-aspect
```
Forces all images to exactly 1920x1080 pixels (may distort images).

### Example 3: Convert to JPEG with Compression
```bash
python image_resizer.py -i input -o compressed -w 1200 -f JPEG -q 85
```
Resizes to 1200px width and converts to JPEG with 85% quality.

### Example 4: Create Thumbnails
```bash
python image_resizer.py -i photos -o thumbs -w 200 --prefix "thumb_" --suffix "_sm"
```
Creates 200px thumbnails with names like `thumb_photo1_sm.jpg`.

### Example 5: Convert to WebP
```bash
python image_resizer.py -i images -o webp -w 1000 -f WEBP
```
Resizes and converts all images to modern WebP format.

## 🐍 Using as a Python Module

You can also import and use the functions in your own scripts:

```python
from image_resizer import batch_resize_images

# Resize images programmatically
batch_resize_images(
    input_folder="my_photos",
    output_folder="resized_photos",
    width=800,
    maintain_aspect=True,
    quality=90
)
```

See `example_usage.py` for more examples.

## 📊 Supported Image Formats

**Input formats:**
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)
- WebP (.webp)

**Output formats:**
- JPEG - Best for photos, with quality control
- PNG - Best for graphics with transparency
- BMP - Uncompressed bitmap
- WebP - Modern format with excellent compression
- TIFF - High-quality archival format

## 🔧 Key Functions

### `get_images_from_folder(folder_path, extensions=None)`
Retrieves all image files from a specified folder.

### `resize_image(input_path, output_path, width, height, maintain_aspect, quality, output_format)`
Resizes a single image with specified parameters.

### `batch_resize_images(input_folder, output_folder, ...)`
Processes all images in a folder with batch resizing.

## 📝 Features Explained

### Aspect Ratio Maintenance
- **Enabled (default)**: Images are resized proportionally, preventing distortion
- **Disabled**: Images are stretched/compressed to exact dimensions

### Quality Control
- Applies to JPEG format
- Range: 1-100 (higher = better quality, larger file size)
- Default: 95 (high quality)
- Recommended: 85-90 for web use

### Format Conversion
- Automatically converts between formats
- Handles transparency appropriately (PNG to JPEG adds white background)
- Optimizes output for best quality/size ratio

## 🎯 Use Cases

- **Web Development**: Optimize images for faster page loading
- **Thumbnails**: Generate preview images for galleries
- **Social Media**: Prepare images for different platform requirements
- **E-commerce**: Standardize product photos
- **Photography**: Create multiple sizes for different uses
- **Storage**: Reduce file sizes while maintaining quality

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Image Resizer Tool - Batch Image Processing Project

## 🆘 Troubleshooting

**Issue**: "No images found in folder"
- Ensure images are in supported formats
- Check that the folder path is correct

**Issue**: "Error processing image"
- Image file may be corrupted
- Check if you have read/write permissions
- Ensure output folder is writable

**Issue**: JPEG quality doesn't change file size
- Quality only affects lossy compression in JPEG
- PNG is lossless and won't be affected by quality setting

---

**Note**: This tool uses high-quality resampling (LANCZOS) for the best image quality during resizing.
