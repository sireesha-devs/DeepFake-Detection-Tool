import cv2
import numpy as np
from PIL import Image

def generate_heatmap(image_path, ela_path):
    """
    Generates a forensic heatmap by highlighting high-energy areas.
    Fulfills the 'Display forensic indicators such as heatmaps' requirement.
    """
    # 1. Load the ELA result (which contains the manipulation energy)
    ela_img = cv2.imread(ela_path)
    gray_ela = cv2.cvtColor(ela_img, cv2.COLOR_BGR2GRAY)

    # 2. Apply a Gaussian blur to smooth out the noise
    blurred = cv2.GaussianBlur(gray_ela, (15, 15), 0)

    # 3. Apply a color map (JET) to create the 'thermal' heatmap look
    heatmap = cv2.applyColorMap(blurred, cv2.COLORMAP_JET)

    # 4. Superimpose the heatmap onto the original image
    original = cv2.imread(image_path)
    original = cv2.resize(original, (heatmap.shape[1], heatmap.shape[0]))
    
    # Blend: 60% original image, 40% heatmap
    overlay = cv2.addWeighted(original, 0.6, heatmap, 0.4, 0)
    
    return overlay