import os 
from PIL import Image 

def log_image(image_path, image_name, log_dir: str = "./app/logs/images"):
    image = Image.open(image_path).convert("RGB")
    image_path = os.path.join(log_dir, image_name)
    image.save(image_path)