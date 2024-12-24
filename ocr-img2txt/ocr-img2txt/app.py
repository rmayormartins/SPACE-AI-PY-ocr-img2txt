import gradio as gr
import pytesseract
from PIL import Image
import easyocr

##
easyocr_reader = easyocr.Reader(['en', 'pt', 'es'], gpu=False)  # 

#Tesseract
def tesseract_ocr(image):
    return pytesseract.image_to_string(image)

#EasyOCR 
def easyocr_ocr(image):
    return ' '.join(easyocr_reader.readtext(image, detail=0))

#
def extract_text_from_image(ocr_engine, image):
    if ocr_engine == "Tesseract":
        return tesseract_ocr(image)
    elif ocr_engine == "EasyOCR":
        return easyocr_ocr(image)
    else:
        return "Invalid OCR selection."


#Gradio
iface = gr.Interface(
    fn=extract_text_from_image,
    inputs=[gr.Dropdown(["Tesseract", "EasyOCR"], label="Select the OCR Engine"), "image"],
    outputs="text",
    title="OCR Img2txt",
    description="This application uses Optical Character Recognition (OCR) technology to extract text from images. Choose between Tesseract OCR and EasyOCR engine to process images containing printed text, converting it into editable and searchable text."
)

iface.launch(debug=True)




