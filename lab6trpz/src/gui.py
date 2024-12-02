import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from archiver import Archiver
import tkinter.simpledialog

class ArchiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Архіватор")
        self.root.geometry("600x400")
        self.create_buttons()
        self.archiver = None
        self.observers = []

    def create_buttons(self):
        self.create_button = ttk.Button(self.root, text="Створити архів", command=self.create_archive)
        self.create_button.pack(pady=10)

        self.extract_button = ttk.Button(self.root, text="Розпакувати архів", command=self.extract_archive)
        self.extract_button.pack(pady=10)

        self.add_button = ttk.Button(self.root, text="Додати файли до архіву", command=self.add_files_to_archive)
        self.add_button.pack(pady=10)

    def add_observer_to_archiver(self, observer):
        self.observers.append(observer)
        if self.archiver is not None:
            self.archiver.add_observer(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def create_archive(self):
        archive_type = self.get_archive_type()
        if archive_type:
            archive_name = filedialog.asksaveasfilename(defaultextension=f".{archive_type}",
                                                        filetypes=[(f"{archive_type.upper()} файли", f"*.{archive_type}")])
            if archive_name:
                try:
                    self.archiver = Archiver(archive_type)
                    for observer in self.observers:
                        self.archiver.add_observer(observer)
                    self.archiver.create_archive(archive_name)
                    files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання в архів")
                    if files_to_add:
                        for file_path in files_to_add:
                            self.archiver.add_file(file_path)
                    self.archiver.close()
                    messagebox.showinfo("Успіх", f"Архів {archive_name} успішно створений.")
                except Exception as e:
                    self.notify_observers(f"Error: {str(e)}")
                    messagebox.showerror("Помилка", str(e))

    def extract_archive(self):
        file_path = filedialog.askopenfilename(filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if file_path:
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                try:
                    self.archiver = Archiver(file_path.split('.')[-1])
                    for observer in self.observers:
                        self.archiver.add_observer(observer)
                    self.notify_observers(f"Extracting archive {file_path}")
                    self.archiver.extract_archive(file_path, destination_folder)
                    self.notify_observers(f"Archive {file_path} extraction completed successfully")
                    messagebox.showinfo("Успіх", f"Архів успішно розпаковано до {destination_folder}.")
                except Exception as e:
                    self.notify_observers(f"Error: {str(e)}")
                    messagebox.showerror("Помилка", str(e))

    def add_files_to_archive(self):
        archive_path = filedialog.askopenfilename(title="Виберіть архів", filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if archive_path:
            files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання")
            if files_to_add:
                try:
                    self.archiver = Archiver(archive_path.split('.')[-1])
                    for observer in self.observers:
                        self.archiver.add_observer(observer)
                    self.notify_observers(f"Adding files to archive {archive_path}")
                    for file_path in files_to_add:
                        self.archiver.add_file(file_path)
                    self.archiver.close()
                    self.notify_observers("Files added to archive successfully")
                    messagebox.showinfo("Успіх", f"Файли успішно додано до архіву {archive_path}.")
                except Exception as e:
                    self.notify_observers(f"Error: {str(e)}")
                    messagebox.showerror("Помилка", str(e))

    def get_archive_type(self):
        archive_type = tkinter.simpledialog.askstring("Тип архіву", "Введіть тип архіву (zip, rar, tar.gz):")
        if archive_type in ['zip', 'rar', 'tar.gz']:
            return archive_type
        else:
            messagebox.showerror("Помилка", "Невірний тип архіву.")
            return None
