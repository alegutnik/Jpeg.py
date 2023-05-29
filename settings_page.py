import os

from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from interface import app


def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_path}' already exists.")


# Создаем новый PDF-файл
width, height = 559, 512
custom_page_size = (width * mm, height * mm)
height_text = 15.8 * mm  # Смотри в canva
name = app.name
birthday = app.birthday

# Пример использования
folder_path = f"./result/{name}_{birthday}"
create_folder(folder_path)

pdf = canvas.Canvas(f"{folder_path}/{name}_{birthday}.pdf", pagesize=custom_page_size)

# Загрузка нового шрифта
pdfmetrics.registerFont(TTFont('Montserrat', './font/Montserrat-VariableFont_wght.ttf'))

# Установка нового шрифта
pdf.setFont("Montserrat", 14 * mm)

# Вставка картинки на страницу
if app.language == "RUS":
    image_path = "./Шаблон RUS.png"
elif app.language == "UKR":
    image_path = "./Шаблон UKR.png"
pdf.drawImage(image_path, x=0, y=0, width=width * mm, height=height * mm)
