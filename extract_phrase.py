import os
import logging
import re
logger = logging.getLogger(__name__)

import pytesseract
from PIL import Image
import pdf2image

from docx import Document

def docx2txt(docx_filename, txt_filename):
    doc = Document(docx_filename)
    with open(txt_filename, "w", encoding="utf-8") as textfile:
        for paragraph in doc.paragraphs:
            textfile.write(paragraph.text + '\n')

def pdf2docx():
    pass

def pdf2txt(data_file,cache_file): #tesseract
    logger.info("***** extracting pdf *****")
    logger.info("Convert pdf to images")
    images = pdf2image.convert_from_path(data_file)

    logger.info("Convert images to txt")
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image, lang='eng+chi_sim') #lang='eng+chi_sim'

    with open(cache_file, 'w', encoding='utf-8') as file:
        file.write(text)

def extract_phrases(cache_file):
    with open(cache_file, 'r', encoding='utf-8') as file:
        content = file.read()

    english_phrases = re.findall(r'[A-Za-z0-9.,]+(?: [A-Za-z0-9.,]+)+', content)
    english_phrases.sort(key = lambda x:x[:3])

    return english_phrases

def main():
    data_dir = './人教版初中重点短语汇总'
    term_dir = '七下重点短语pdf'
    data_file = '七下U1重点短语.pdf' #'七上重点短语汇总.pdf'
    data_path = os.path.join(data_dir,term_dir,data_file)
    cache_dir = './cache'
    cache_file = 'grade7_termB.txt'
    cache_path = os.path.join(cache_dir,cache_file)
    tpdf2txt(data_path,cache_path)
    print(extract_phrases(cache_path))

if __name__ == "__main__":
    main()