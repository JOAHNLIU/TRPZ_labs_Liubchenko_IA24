import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from archive_facade import ArchiveFacade
from archive_process_observer import ArchiveProcessObserver
from composite import Composite
from leaf import Leaf
import tkinter.simpledialog
from database_manager import DatabaseManager

class ArchiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Архіватор")
        self.root.geometry("600x400")
        self.create_buttons()
        self.facade = None
        self.observers = []
        self.db_manager = DatabaseManager("archiver.db")

        # Ініціалізація компонента дерева
        self.root_component = Composite("root")

    def create_buttons(self):
        self.create_button = ttk.Button(self.root, text="Створити архів", command=self.create_archive)
        self.create_button.pack(pady=10)

        self.extract_button = ttk.Button(self.root, text="Розпакувати архів", command=self.extract_archive)
        self.extract_button.pack(pady=10)

        self.add_button = ttk.Button(self.root, text="Додати файли до архіву", command=self.add_files_to_archive)
        self.add_button.pack(pady=10)
        
        self.show_db_button = ttk.Button(self.root, text="Показати базу даних", command=self.show_database)
        self.show_db_button.pack(pady=10)

    def add_observer_to_archiver(self, observer):
        self.observers.append(observer)
        if self.facade is not None:
            self.facade.archiver.add_observer(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)
        self.db_manager.add_notification(message)

    def create_archive(self):
        archive_type = self.get_archive_type()
        if archive_type:
            archive_name = filedialog.asksaveasfilename(defaultextension=f".{archive_type}",
                                                        filetypes=[(f"{archive_type.upper()} файли", f"*.{archive_type}")])
            if archive_name:
                try:
                    self.facade = ArchiveFacade(archive_type, self.db_manager)
                    self.facade.create_archive(archive_name, self.root_component)
                    messagebox.showinfo("Успіх", f"Архів {archive_name} успішно створений.")
                    self.notify_observers(f"Архів {archive_name} успішно створений.")
                    self.show_database()  # Показати базу даних після створення архіву
                except Exception as e:
                    self.notify_observers(f"Error: {str(e)}")
                    messagebox.showerror("Помилка", str(e))

    def extract_archive(self):
        file_path = filedialog.askopenfilename(filetypes=[("Всі архіви", "*.zip;*.tar.gz;*.rar")])
        if file_path:
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                try:
                    self.facade = ArchiveFacade(file_path.split('.')[-1], self.db_manager)
                    self.facade.extract_archive(file_path, destination_folder)
                    messagebox.showinfo("Успіх", f"Архів успішно розпаковано до {destination_folder}.")
                    self.notify_observers(f"Архів успішно розпаковано до {destination_folder}.")
                    self.show_database()  # Показати базу даних після розпакування архіву
                except Exception as e:
                    self.notify_observers(f"Error: {str(e)}")
                    messagebox.showerror("Помилка", str(e))

    def add_files_to_archive(self):
        files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання")
        if files_to_add:
            try:
                for file_path in files_to_add:
                    leaf = Leaf(file_path.split("/")[-1], file_path)
                    self.root_component.add(leaf)
                self.notify_observers("Файли успішно додано до архіву.")
                messagebox.showinfo("Успіх", "Файли успішно додано до архіву.")
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

    def show_database(self):
        archives = self.db_manager.get_archives()
        db_info = ""
        for archive in archives:
            archive_id, archive_name = archive
            db_info += f"Архів: {archive_name}\n"
            files = self.db_manager.get_files_in_archive(archive_id)
            for file in files:
                db_info += f"  Файл: {file[0]}\n"
        messagebox.showinfo("База даних", db_info)
