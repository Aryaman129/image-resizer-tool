"""
Image Resizer Tool
A batch image resizing and conversion tool using Python and Pillow.

Features:
- Resize multiple images at once
- Maintain aspect ratio or force dimensions
- Convert between different image formats
- Preserve or optimize quality
"""

import os
from PIL import Image
import argparse
from pathlib import Path


def get_images_from_folder(folder_path, extensions=None):
    """
    Get all image files from the specified folder.
    
    Args:
        folder_path (str): Path to the folder containing images
        extensions (list): List of image extensions to include (default: common formats)
    
    Returns:
        list: List of image file paths
    """
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
    
    image_files = []
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return image_files
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            if ext.lower() in extensions:
                image_files.append(file_path)
    
    return image_files


def resize_image(input_path, output_path, width=None, height=None, 
                 maintain_aspect=True, quality=95, output_format=None):
    """
    Resize a single image.
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save resized image
        width (int): Target width in pixels
        height (int): Target height in pixels
        maintain_aspect (bool): Whether to maintain aspect ratio
        quality (int): Image quality (1-100) for JPEG
        output_format (str): Output format (e.g., 'JPEG', 'PNG')
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            original_width, original_height = img.size
            
            # Calculate new dimensions
            if width and height:
                if maintain_aspect:
                    # Calculate aspect ratio
                    aspect_ratio = original_width / original_height
                    
                    # Determine which dimension to use
                    if width / height > aspect_ratio:
                        # Height is the limiting factor
                        new_height = height
                        new_width = int(height * aspect_ratio)
                    else:
                        # Width is the limiting factor
                        new_width = width
                        new_height = int(width / aspect_ratio)
                else:
                    new_width = width
                    new_height = height
            elif width:
                # Only width specified
                aspect_ratio = original_height / original_width
                new_width = width
                new_height = int(width * aspect_ratio)
            elif height:
                # Only height specified
                aspect_ratio = original_width / original_height
                new_height = height
                new_width = int(height * aspect_ratio)
            else:
                print(f"Warning: No dimensions specified for {input_path}")
                return False
            
            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Determine output format
            if output_format is None:
                output_format = img.format or 'PNG'
            
            # Save the image
            if output_format.upper() in ['JPEG', 'JPG']:
                # Convert to RGB if necessary (JPEG doesn't support transparency)
                if resized_img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', resized_img.size, (255, 255, 255))
                    if resized_img.mode == 'P':
                        resized_img = resized_img.convert('RGBA')
                    rgb_img.paste(resized_img, mask=resized_img.split()[-1] if resized_img.mode == 'RGBA' else None)
                    resized_img = rgb_img
                resized_img.save(output_path, format=output_format, quality=quality, optimize=True)
            else:
                resized_img.save(output_path, format=output_format)
            
            print(f"✓ Resized: {os.path.basename(input_path)} "
                  f"({original_width}x{original_height} → {new_width}x{new_height})")
            return True
            
    except Exception as e:
        print(f"✗ Error processing {input_path}: {str(e)}")
        return False


def batch_resize_images(input_folder, output_folder, width=None, height=None,
                        maintain_aspect=True, quality=95, output_format=None,
                        prefix="", suffix=""):
    """
    Resize all images in a folder.
    
    Args:
        input_folder (str): Folder containing input images
        output_folder (str): Folder to save resized images
        width (int): Target width in pixels
        height (int): Target height in pixels
        maintain_aspect (bool): Whether to maintain aspect ratio
        quality (int): Image quality (1-100)
        output_format (str): Output format (e.g., 'JPEG', 'PNG')
        prefix (str): Prefix to add to output filenames
        suffix (str): Suffix to add to output filenames
    
    Returns:
        dict: Statistics about the operation
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all images from input folder
    image_files = get_images_from_folder(input_folder)
    
    if not image_files:
        print(f"No images found in '{input_folder}'")
        return {"total": 0, "success": 0, "failed": 0}
    
    print(f"\nFound {len(image_files)} images in '{input_folder}'")
    print(f"Output folder: '{output_folder}'")
    print(f"Target size: {width or 'auto'}x{height or 'auto'}")
    print(f"Maintain aspect ratio: {maintain_aspect}")
    print("-" * 60)
    
    success_count = 0
    failed_count = 0
    
    for image_path in image_files:
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        
        # Determine output extension
        if output_format:
            if output_format.upper() in ['JPEG', 'JPG']:
                output_ext = '.jpg'
            else:
                output_ext = f'.{output_format.lower()}'
        else:
            output_ext = ext
        
        # Create output filename with prefix/suffix
        output_filename = f"{prefix}{name}{suffix}{output_ext}"
        output_path = os.path.join(output_folder, output_filename)
        
        # Resize the image
        if resize_image(image_path, output_path, width, height, 
                       maintain_aspect, quality, output_format):
            success_count += 1
        else:
            failed_count += 1
    
    print("-" * 60)
    print(f"\n✅ Completed: {success_count} images resized successfully")
    if failed_count > 0:
        print(f"❌ Failed: {failed_count} images")
    
    return {
        "total": len(image_files),
        "success": success_count,
        "failed": failed_count
    }


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Batch Image Resizer Tool - Resize and convert images in bulk",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Resize all images to 800px width (maintaining aspect ratio)
  python image_resizer.py -i input_folder -o output_folder -w 800
  
  # Resize to specific dimensions without maintaining aspect ratio
  python image_resizer.py -i images -o resized -w 1920 -h 1080 --no-aspect
  
  # Resize and convert to JPEG with 85% quality
  python image_resizer.py -i photos -o compressed -w 1200 -f JPEG -q 85
  
  # Resize with prefix and suffix
  python image_resizer.py -i input -o output -w 500 --prefix "thumb_" --suffix "_small"
        """
    )
    
    parser.add_argument('-i', '--input', required=True, 
                       help='Input folder containing images')
    parser.add_argument('-o', '--output', required=True,
                       help='Output folder for resized images')
    parser.add_argument('-w', '--width', type=int,
                       help='Target width in pixels')
    parser.add_argument('-ht', '--height', type=int,
                       help='Target height in pixels')
    parser.add_argument('--no-aspect', action='store_true',
                       help='Do not maintain aspect ratio')
    parser.add_argument('-q', '--quality', type=int, default=95,
                       help='Image quality for JPEG (1-100, default: 95)')
    parser.add_argument('-f', '--format', 
                       choices=['JPEG', 'PNG', 'BMP', 'WEBP', 'TIFF'],
                       help='Output image format')
    parser.add_argument('--prefix', default='',
                       help='Prefix for output filenames')
    parser.add_argument('--suffix', default='',
                       help='Suffix for output filenames (before extension)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.width and not args.height:
        parser.error("At least one of --width or --height must be specified")
    
    if args.quality < 1 or args.quality > 100:
        parser.error("Quality must be between 1 and 100")
    
    # Run batch resize
    batch_resize_images(
        input_folder=args.input,
        output_folder=args.output,
        width=args.width,
        height=args.height,
        maintain_aspect=not args.no_aspect,
        quality=args.quality,
        output_format=args.format,
        prefix=args.prefix,
        suffix=args.suffix
    )


if __name__ == "__main__":
    main()
