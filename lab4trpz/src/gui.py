import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import zipfile
import os
import rarfile
import tarfile
import zipfile36
from archive_factory import ArchiveFactory
import tkinter.simpledialog  # Додано імпорт для simpledialog

class ArchiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Архіватор")  # Назва вікна програми
        self.root.geometry("600x400")  # Розміри вікна

        # Створення кнопок для операцій з архівами
        self.create_buttons()

    def create_buttons(self):
        # Кнопка для створення архіву
        self.create_button = ttk.Button(self.root, text="Створити архів", command=self.create_archive)
        self.create_button.pack(pady=10)

        # Кнопка для розпакування архіву
        self.extract_button = ttk.Button(self.root, text="Розпакувати архів", command=self.extract_archive)
        self.extract_button.pack(pady=10)

        # Кнопка для додавання файлів до архіву
        self.add_button = ttk.Button(self.root, text="Додати файли до архіву", command=self.add_files_to_archive)
        self.add_button.pack(pady=10)

    def create_archive(self):
        # Отримуємо тип архіву від користувача
        archive_type = self.get_archive_type()
        if archive_type:
            # Запитуємо у користувача файли для додавання в архів
            files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання в архів")
            if files_to_add:
                # Запитуємо, куди зберегти архів
                archive_name = filedialog.asksaveasfilename(defaultextension=f".{archive_type}",
                                                           filetypes=[(f"{archive_type.upper()} файли", f"*.{archive_type}")])
                if archive_name:
                    try:
                        # Створюємо архів через фабричний метод
                        factory = ArchiveFactory()
                        archive = factory.create_archive(archive_type)
                        archive.create(archive_name, files_to_add)  # Створення архіву
                        messagebox.showinfo("Успіх", f"Архів {archive_name} успішно створений.")  # Повідомлення про успіх
                    except Exception as e:
                        messagebox.showerror("Помилка", str(e))  # Повідомлення про помилку

    def extract_archive(self):
        # Запитуємо у користувача архів для розпакування
        file_path = filedialog.askopenfilename(filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if file_path:
            # Запитуємо, куди розпакувати архів
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                try:
                    # Створюємо об'єкт архіватора через фабричний метод
                    factory = ArchiveFactory()
                    archive = factory.create_archive(file_path.split('.')[-1])
                    archive.extract(file_path, destination_folder)  # Розпаковка архіву
                    messagebox.showinfo("Успіх", f"Архів успішно розпаковано до {destination_folder}.")  # Повідомлення про успіх
                except Exception as e:
                    messagebox.showerror("Помилка", str(e))  # Повідомлення про помилку

    def add_files_to_archive(self):
        # Крок 1: Вибір архіву для додавання файлів
        archive_path = filedialog.askopenfilename(title="Виберіть архів", filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if archive_path:
            # Крок 2: Вибір файлів для додавання
            files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання")
            if files_to_add:
                try:
                    # Створення архіватора через фабричний метод
                    factory = ArchiveFactory()
                    archive_type = archive_path.split('.')[-1]
                    archive = factory.create_archive(archive_type)
                    archive.add_files(archive_path, files_to_add)  # Додавання файлів до архіву
                    messagebox.showinfo("Успіх", f"Файли успішно додано до архіву {archive_path}.")  # Повідомлення про успіх
                except Exception as e:
                    messagebox.showerror("Помилка", str(e))  # Повідомлення про помилку

    def get_archive_type(self):
        # Використовуємо simpledialog для отримання типу архіву
        archive_type = tkinter.simpledialog.askstring("Тип архіву", "Введіть тип архіву (zip, rar, tar.gz):")
        if archive_type in ['zip', 'rar', 'tar.gz']:  # Перевірка введеного типу архіву
            return archive_type
        else:
            messagebox.showerror("Помилка", "Невірний тип архіву.")  # Якщо введено некоректний тип
            return None
