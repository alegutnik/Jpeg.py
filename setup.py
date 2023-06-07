# from cx_Freeze import setup, Executable
#
# # Список файлов и папок для включения
# include_files = ["Шаблон RUS.png","Шаблон UKR.png", 'font', "poppler-0.68.0"]
#
# setup(
#     name="YourApp",
#     version="1.0",
#     description="Description of your app",
#     options={'build_exe': {'include_files': include_files}},
#     executables=[Executable("app.py",base="Win32GUI")]
# )


import sys
from cx_Freeze import setup, Executable

include_files = ["Шаблон RUS.png", "Шаблон UKR.png", 'font', "poppler-0.68.0"]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Если ваше приложение имеет графический интерфейс пользователя

setup(
    name="YourApp",
    version="1.0",
    description="Description of your app",
    options={'build_exe': {'include_files': include_files}},
    executables=[Executable("app.py", base=base)]
)
