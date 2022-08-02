"""
Requirements:

    1.  Install poppler
    2.  Install tesseract

"""

# utils
import os, fitz
from PIL import Image

# external libraries
from pdf2image import convert_from_path
import pytesseract
from googletrans import Translator

# poppler_path=r'C:\Users\omejia\Downloads\Release-22.04.0-0\poppler-22.04.0\Library\bin'
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def convert_pdf_to_image(file_path, output_folder, poppler_path):

    output_path = f"{output_folder}" + file_path.split("/")[-1][:-4]
    
    if not os.path.isdir(f"{output_path}/images/"):
        os.mkdir(f"{output_path}/")
        os.mkdir(f"{output_path}/images/")
    
    print("Generating images ...")
    images = convert_from_path(file_path,poppler_path=poppler_path)

    print(f"Saving images into ./{output_path}/images/")
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'{output_path}/images/page' + str(i+1) + '.jpg', 'JPEG')

    return output_path
    

def convert_images_to_text(output_path, translate=False, output_language='es'):

    if translate:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        translator = Translator()
        print("transtaltion is ON")
    if not os.path.isdir(f"{output_path}/text/"):
            os.mkdir(f"{output_path}/text/")

    print(f"Saving text files into {output_path}text/")
    for file in os.listdir(f"{output_path}/images"):
        text = pytesseract.image_to_string(Image.open(f"{output_path}/images/{file}"), lang="eng")
        # print(file)
        with open(f"{output_path}/text/{file[:-4]}.txt", 'w') as f:
            f.write(text)
        if translate:
            with open(f"{output_path}/text/{file[:-4]}-{output_language}.txt", 'w') as f:
                try:
                    f.write(translator.translate(text=text, dest=output_language).text)
                except UnicodeEncodeError:
                    print("Invalid character in file")
    print("END")
        

def run():
    pass


if __name__ == '__main__':
    run()
