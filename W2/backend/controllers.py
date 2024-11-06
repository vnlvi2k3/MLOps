from schemas import OCR_Response, OCR_Output
import numpy as np 
from PIL import Image
import easyocr

def extract_ocr(image_path, languages: list = ["en"]):
    OCR_Reader = easyocr.Reader(languages)
    img = np.asarray(Image.open(image_path).convert("RGB"))
    result = OCR_Reader.readtext(img)
    return_data = []
    for line in result:
        bbox = [[int(x) for x in point] for point in line[0]]
        text = line[1]
        score = line[2]
        return_data.append(
            OCR_Output(bbox=bbox, text=text, score=score)
        )
    return return_data