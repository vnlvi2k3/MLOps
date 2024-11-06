from apis.ocr import ocr_api
import gradio

demo = gradio.Interface(
    fn=ocr_api,
    inputs="file",
    outputs=["text", "image"],
    description="This is an OCR model that extracts text from images.",
    title="OCR",
)
demo.launch(
    server_name="0.0.0.0",
    server_port=3000, 
)
            