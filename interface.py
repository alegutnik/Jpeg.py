import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        # Создание окна, задание его размера
        self.width = 300
        self.height = 450
        self.geometry(f"{self.width}x{self.height}")
        self.title("Нумерологические показатели")
        self.resizable(False, False)

        self.general_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.general_frame.place(relx=0.5, rely=0.5, anchor=CTk.CENTER)

        self.birthday_entry = CTk.CTkEntry(master=self.general_frame)
        self.birthday_entry.pack()
        self.birthday_label = CTk.CTkLabel(master=self.general_frame, text="Введите имя")
        self.birthday_label.pack(pady=(0, 20))

        self.name_entry = CTk.CTkEntry(master=self.general_frame)
        self.name_entry.pack()
        self.name_label = CTk.CTkLabel(master=self.general_frame, text="Введите дату рождения")
        self.name_label.pack(pady=(0, 20))

        self.language_entry = CTk.CTkComboBox(master=self.general_frame, values=("UKR", "RUS"))
        self.language_entry.pack()
        self.language_label = CTk.CTkLabel(master=self.general_frame, text="Выберите язык")
        self.language_label.pack(pady=(0, 20))

        self.gender_entry = CTk.CTkComboBox(master=self.general_frame, values=("Woman", "Man"))
        self.gender_entry.pack()
        self.gender_label = CTk.CTkLabel(master=self.general_frame, text="Выберите пол")
        self.gender_label.pack(pady=(0, 20))

        self.btn = CTk.CTkButton(master=self.general_frame, text="Готово", width=100, command=self.get_value)
        self.btn.pack()

        # Атрибуты для хранения значений
        self.name = ""
        self.birthday = ""
        self.language = ""
        self.gender = ""

    def get_value(self):
        self.name = self.birthday_entry.get()
        self.birthday = self.name_entry.get()
        self.language = self.language_entry.get()
        self.gender = self.gender_entry.get()
        # App.destroy()

        # Закрытие окна
        self.destroy()


app = App()
app.mainloop()
