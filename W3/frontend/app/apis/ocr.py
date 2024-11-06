from utils import plot_bbox
import requests
from PIL import Image
import io
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://0.0.0.0:8000")

def ocr_api(image_path: str):
    url = f"{BACKEND_URL}/ocr"

    image = Image.open(image_path)
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format="PNG")
    image_data = image_byte_array.getvalue()

    image_name = image_path.split("/")[-1]
    files = {
        "file_upload": (image_name, image_data, "image/png")
    }
    headers = {'accept': 'application/json'}
    response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        json_response = response.json()["data"]
        image_with_bbox = plot_bbox(json_response, image)[0]
        return "Success", image_with_bbox
    else:
        return "Error: API request failed", None



