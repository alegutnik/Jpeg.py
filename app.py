#!/usr/bin/env python

import os

from pdf2image import convert_from_path
from reportlab.lib import colors
from reportlab.lib.units import mm

import interface
from client import Client
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

# Вставка заголовка на страницу
pdf.drawCentredString((width_cell + 1.5) * mm, (height - height_cell * 0.6 - 5) * mm, birthday)
pdf.setFont("Klein-Medium", 16 * mm)
pdf.drawCentredString((width_cell + 1.5) * mm, (height - height_cell * 0.3 - 5) * mm, name.upper())

# -------------------------------------

pdf.save()
path = f"result/{name}_{birthday}/{name}_{birthday}"
images = convert_from_path(f"{path}.pdf", 500, poppler_path=r'poppler-0.68.0\bin')
images[0].save(f"{path}.jpeg", "JPEG")

os.startfile(f"{path}.jpeg".replace("/","\\"))
