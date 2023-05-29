import fitz
from PIL import Image


class Pdf:
    def __init__(self, pdf_path, output_folder, name_image):
        self.pdf_path = pdf_path
        self.output_folder = output_folder
        self.name_image = name_image
        self.img_path = f"{output_folder}/{name_image}.jpeg"

    def pdf_to_jpeg(self):
        doc = fitz.open(self.pdf_path)
        page = doc.load_page(0)  # Обращаемся к первой странице (индекс 0)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(self.img_path, "JPEG", quality=100)  # Установите параметр quality на желаемое значение
        print(f"Page saved as {self.img_path}")
