import cv2
import numpy as np

def perform_fft(image_path):
    """
    Performs Fast Fourier Transform to detect periodic noise patterns.
    """
    # 1. Load image in grayscale
    img = cv2.imread(image_path, 0)
    
    # 2. Perform FFT
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    
    # Calculate magnitude spectrum on log scale
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)
    
    # Normalize for display
    magnitude_spectrum = np.uint8(cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX))
    
    return magnitude_spectrum