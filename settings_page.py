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
pdfmetrics.registerFont(TTFont('Klein-Medium', './font/Klein-Medium.ttf'))

# Установка нового шрифта
pdf.setFont("Klein-Medium", 18 * mm)

# Вставка картинки на страницу
if app.language == "RUS" and app.gender == "Woman":
    image_path = "./template/Шаблон RUS.png"
elif app.language == "UKR" and app.gender == "Woman":
    image_path = "./template/Шаблон UKR.png"
elif app.language == "RUS" and app.gender == "Man":
    image_path = "./template/Шаблон UKR man.png"
elif app.language == "UKR" and app.gender == "Man":
    image_path = "./template/Шаблон UKR man.png"

pdf.drawImage(image_path, x=0, y=0, width=width * mm, height=height * mm)
