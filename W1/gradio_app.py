import numpy as np 
import easyocr
import gradio as gr 
from PIL import Image, ImageDraw, ImageFont

def plot_bbox(easy_ocr_result, image):
    boxes = [line[0] for line in easy_ocr_result]
    texts = [line[1] for line in easy_ocr_result]
    scores = [line[2] for line in easy_ocr_result]
    image = Image.fromarray(image)

    draw = ImageDraw.Draw(image)
    rectangle_width = 2
    font_size = 20
    font = ImageFont.truetype("./JetBrainsMono-Medium.ttf", size=font_size)  

    for box, text in zip(boxes, texts):
        top_left     = (int(box[0][0]), int(box[0][1]))
        bottom_right = (int(box[2][0]), int(box[2][1]))

        # Check if x1 < x0
        if top_left[0] > bottom_right[0]:
            top_left, bottom_right = (bottom_right[0], top_left[1]), (top_left[0], bottom_right[1])
        
        # Check if y1 < y0
        if top_left[1] > bottom_right[1]:
            top_left, bottom_right = (top_left[0], bottom_right[1]), (bottom_right[0], top_left[1])
        
        text_pos = (top_left[0], top_left[1]-font_size-rectangle_width)
        draw.rectangle([top_left, bottom_right], outline="green", width=2)
        draw.text(text_pos, text, fill="blue", font=font)

    return image

def creat_reader(languages):
    return easyocr.Reader(languages)

def extract_text(image, languages):
    reader = creat_reader(languages)
    res = reader.readtext(image)
    return plot_bbox(res, image)

lang = ['ch_tra', 'en', 'vi', 'fr', 'es', 'ko', 'ja']

demo = gr.Interface(
    fn = extract_text, 
    inputs = [gr.Image(), gr.CheckboxGroup(lang, label="Languages")],
    outputs= [gr.Image()]
)
demo.launch()
