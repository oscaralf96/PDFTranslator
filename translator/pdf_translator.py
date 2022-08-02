# my functions
from .conversions import *

# external libraries
import pytesseract

# utils
import os



poppler_path=r'C:\Users\omejia\Downloads\Release-22.04.0-0\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def pdf_translator(pdf_path="pdfs/POO.pdf", storage="./"):
    
    output_language = "es"
    output_folder = storage + "/output/"

    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    output_path = convert_pdf_to_image(pdf_path, output_folder, poppler_path) + "/"
    convert_images_to_text(output_path, translate=True, output_language=output_language)



if __name__ == '__main__':
    pdf_translator()
