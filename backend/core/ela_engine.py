import os
from PIL import Image, ImageChops, ImageEnhance

def perform_ela(image_path, quality=90):
    """
    Performs Error Level Analysis to find compression inconsistencies.
    """
    temp_path = "temp_ela.jpg"
    
    # 1. Open original and convert to RGB
    original = Image.open(image_path).convert('RGB')
    
    # 2. Save at a specific quality to force a new compression level
    original.save(temp_path, 'JPEG', quality=quality)
    temporary = Image.open(temp_path)
    
    # 3. Find the absolute difference between original and re-compressed
    # Areas with different compression histories will have higher differences
    ela_image = ImageChops.difference(original, temporary)
    
    # 4. Enhance the difference so it's visible to the eye (scaling)
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    
    # Clean up the temporary file
    if os.path.exists(temp_path):
        os.remove(temp_path)
        
    return ela_image