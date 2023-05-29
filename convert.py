import fitz
from PIL import Image


class Jpeg:
    """Класс Jpeg для конвертации PDF файла в формат jpeg"""

    def __init__(self, pdf_path, output_folder, name_image):
        """
        Инициализация объекта Jpeg.

        :param pdf_path: Путь к PDF-файлу.
        :param output_folder: Путь к папке, в которую сохранится JPEG-изображение.
        :param name_image: Имя JPEG-изображения.
        """
        self.pdf_path = pdf_path
        self.output_folder = output_folder
        self.name_image = name_image
        self.img_path = f"{output_folder}/{name_image}.jpeg"

    def convert_to_jpeg(self):
        """
        Конвертирует PDF-файл в формат JPEG.

        Использует библиотеки fitz и PIL для открытия PDF-файла,
        извлечения первой страницы, создания пиксельной карты (pixmap)
        и сохранения ее в формате JPEG.
        """
        doc = fitz.open(self.pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(self.img_path, "JPEG", quality=100)
        print(f"Страница сохранена как {self.img_path}")
