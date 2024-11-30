import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import zipfile
import os
import rarfile
import tarfile
import zipfile36
from archive_factory import ArchiveFactory
import tkinter.simpledialog

class ArchiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Архіватор")
        self.root.geometry("600x400")
        self.create_buttons()

    def create_buttons(self):
        self.create_button = ttk.Button(self.root, text="Створити архів", command=self.create_archive)
        self.create_button.pack(pady=10)

        self.extract_button = ttk.Button(self.root, text="Розпакувати архів", command=self.extract_archive)
        self.extract_button.pack(pady=10)

        self.add_button = ttk.Button(self.root, text="Додати файли до архіву", command=self.add_files_to_archive)
        self.add_button.pack(pady=10)

    def create_archive(self):
        archive_type = self.get_archive_type()
        if archive_type:
            files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання в архів")
            if files_to_add:
                archive_name = filedialog.asksaveasfilename(defaultextension=f".{archive_type}",
                                                           filetypes=[(f"{archive_type.upper()} файли", f"*.{archive_type}")])
                if archive_name:
                    try:
                        factory = ArchiveFactory()
                        archive = factory.create_archiver(archive_type)
                        archive.create_archive(archive_name)
                        for file_path in files_to_add:
                            archive.add_file(file_path)
                        archive.close()
                        messagebox.showinfo("Успіх", f"Архів {archive_name} успішно створений.")
                    except Exception as e:
                        messagebox.showerror("Помилка", str(e))

    def extract_archive(self):
        file_path = filedialog.askopenfilename(filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if file_path:
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                try:
                    factory = ArchiveFactory()
                    archive = factory.create_archiver(file_path.split('.')[-1])
                    archive.extract_archive(file_path, destination_folder)
                    messagebox.showinfo("Успіх", f"Архів успішно розпаковано до {destination_folder}.")
                except Exception as e:
                    messagebox.showerror("Помилка", str(e))

    def add_files_to_archive(self):
        archive_path = filedialog.askopenfilename(title="Виберіть архів", filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if archive_path:
            files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання")
            if files_to_add:
                try:
                    factory = ArchiveFactory()
                    archive_type = archive_path.split('.')[-1]
                    archive = factory.create_archiver(archive_type)
                    for file_path in files_to_add:
                        archive.add_file(file_path)
                    archive.close()
                    messagebox.showinfo("Успіх", f"Файли успішно додано до архіву {archive_path}.")
                except Exception as e:
                    messagebox.showerror("Помилка", str(e))

    def get_archive_type(self):
        archive_type = tkinter.simpledialog.askstring("Тип архіву", "Введіть тип архіву (zip, rar, tar.gz):")
        if archive_type in ['zip', 'rar', 'tar.gz']:
            return archive_type
        else:
            messagebox.showerror("Помилка", "Невірний тип архіву.")
            return None
