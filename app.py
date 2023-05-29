import os

from reportlab.lib import colors
from reportlab.lib.units import mm

import interface
import settings_page
from client import Client
from convert import Jpeg
from settings_page import pdf, height


def coordinates(rows, columns):
    x = width_cell / 2 + (width_cell + 3) * (rows - 1)
    if rows > 3:
        x += 25
    y = height - (100 + 3) * (columns - 1) - 40 - 25
    return (x * mm, y * mm)


# INPUT
name = interface.app.name
birthday = interface.app.birthday
width_cell, height_cell = 125, 100
count = 1

# Создаем клиента
client = Client(name, birthday)

# Задаем цвет в формате HEX
text_color_blue = colors.HexColor("#091A4C")  # Синий
text_color_white = colors.HexColor("#FFFFFF")  # Синий

# -------------------------------------

# Устанавливаем цвет текста
pdf.setFillColor(text_color_blue)

# Координаты основных чисел
coordinats_general_numbers = {"Характер": coordinates(1, 2),
                              "Енергия": coordinates(1, 3),
                              "Интерес": coordinates(1, 4),
                              "Здоровье": coordinates(2, 2),
                              "Логика": coordinates(2, 3),
                              "Труд": coordinates(2, 4),
                              "Удача": coordinates(3, 2),
                              "Долг": coordinates(3, 3),
                              "Память": coordinates(3, 4)}

# Вставка основных показателей
for key, value in coordinats_general_numbers.items():
    pdf.drawCentredString(*coordinats_general_numbers.get(key),
                          str(count) * client.general_numbers.get(key) if client.general_numbers.get(key) != 0 else "-")
    count += 1

# -------------------------------------

# Устанавливаем цвет текста
pdf.setFillColor(text_color_white)

# Вставка заголовка на страницу
pdf.drawCentredString((width_cell + 1.5) * mm, (height - height_cell * 0.3) * mm, name)
pdf.drawCentredString((width_cell + 1.5) * mm, (height - height_cell * 0.6) * mm, birthday)

# -------------------------------------

# Координаты дополнительных показательей
coordinats_second_numbers = {"Быт": coordinates(2, 5),
                             "Темперамент": coordinates(4, 1),
                             "Цель": coordinates(4, 2),
                             "Семья": coordinates(4, 3),
                             "Привычки": coordinates(4, 4)}

# Вставка дополнительных показателей
for key, value in coordinats_second_numbers.items():
    pdf.drawCentredString(*coordinats_second_numbers.get(key),
                          str(client.second_general_numbers.get(key)) if
                          client.second_general_numbers.get(key) != 0 else "-")

pdf.drawCentredString(*coordinates(3, 1), str(client.additional_number_2()))

pdf.save()
path_jpeg = settings_page.folder_path
name_jpeg = f"{name}_{birthday}"
pdf = Jpeg(f"{settings_page.folder_path}/{name}_{birthday}.pdf", path_jpeg, name_jpeg)
pdf.pdf_to_jpeg()
# pdf_to_jpeg(f"{settings_page.folder_path}/{name}_{birthday}.pdf", path_jpeg, name_jpeg)
# os.startfile(f"{settings_page.folder_path}/{name}_{birthday}.jpeg")
print(pdf.img_path)
os.startfile(pdf.img_path.replace("/", "\\"))

# try:
#     file_path = f"./{name}_{birthday}.pdf"
#     with open(file_path, "r", encoding="utf-8") as file:
#         # Чтение содержимого файла
#         content = file.read()
#         # Дальнейшая обработка содержимого файла
#         print(content)  # Пример: вывод содержимого файла
# except FileNotFoundError:
#     print("Файл не найден")
# except IOError:
#     print("Ошибка ввода-вывода при открытии файла")
