"""
Simple example script demonstrating how to use the image resizer functions directly.
"""

from image_resizer import batch_resize_images

# Example 1: Resize images to 800px width (maintaining aspect ratio)
print("Example 1: Resize to 800px width")
batch_resize_images(
    input_folder="sample_images",
    output_folder="output/resized_800",
    width=800,
    maintain_aspect=True
)

# Example 2: Resize to specific dimensions (1920x1080) without maintaining aspect ratio
print("\n" + "="*60)
print("Example 2: Resize to 1920x1080 (forced dimensions)")
batch_resize_images(
    input_folder="sample_images",
    output_folder="output/resized_1920x1080",
    width=1920,
    height=1080,
    maintain_aspect=False
)

# Example 3: Create thumbnails (300px) and convert to JPEG
print("\n" + "="*60)
print("Example 3: Create thumbnails")
batch_resize_images(
    input_folder="sample_images",
    output_folder="output/thumbnails",
    width=300,
    output_format="JPEG",
    quality=85,
    prefix="thumb_"
)

# Example 4: Resize and convert to WebP format
print("\n" + "="*60)
print("Example 4: Convert to WebP")
batch_resize_images(
    input_folder="sample_images",
    output_folder="output/webp",
    width=1200,
    output_format="WEBP"
)

print("\n" + "="*60)
print("All examples completed!")
