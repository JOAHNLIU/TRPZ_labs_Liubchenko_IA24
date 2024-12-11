import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import requests
import tkinter.simpledialog
from composite import Composite
from leaf import Leaf

class ArchiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Архіватор")
        self.root.geometry("600x400")
        self.create_buttons()
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

    def create_archive(self):
        archive_name = filedialog.asksaveasfilename(defaultextension=".zip",
                                                    filetypes=[("ZIP файли", "*.zip")])
        if archive_name:
            files = filedialog.askopenfilenames(title="Виберіть файли для додавання")
            if files:
                response = requests.post("http://localhost:5000/create_archive", json={"archive_name": archive_name, "files": files})
                if response.status_code == 200:
                    messagebox.showinfo("Успіх", f"Архів {archive_name} успішно створений.")
                else:
                    messagebox.showerror("Помилка", response.json().get("error", "Unknown error"))

    def extract_archive(self):
        archive_path = filedialog.askopenfilename(filetypes=[("ZIP файли", "*.zip")])
        if archive_path:
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                response = requests.post("http://localhost:5000/extract_archive", json={"archive_name": archive_path, "destination_folder": destination_folder})
                if response.status_code == 200:
                    messagebox.showinfo("Успіх", f"Архів успішно розпаковано до {destination_folder}.")
                else:
                    messagebox.showerror("Помилка", response.json().get("error", "Unknown error"))

    def add_files_to_archive(self):
        files_to_add = filedialog.askopenfilenames(title="Виберіть файли для додавання")
        if files_to_add:
            try:
                for file_path in files_to_add:
                    leaf = Leaf(file_path.split("/")[-1], file_path)
                    self.root_component.add(leaf)
                messagebox.showinfo("Успіх", "Файли успішно додано до архіву.")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))

    def get_archive_type(self):
        archive_type = tkinter.simpledialog.askstring("Тип архіву", "Введіть тип архіву (zip, rar, tar.gz):")
        if archive_type in ['zip', 'rar', 'tar.gz']:
            return archive_type
        else:
            messagebox.showerror("Помилка", "Невірний тип архіву.")
            return None

    def show_database(self):
        response = requests.get("http://localhost:5000/show_database")
        if response.status_code == 200:
            db_info = response.json().get("database_info", "Дані не знайдені")
            messagebox.showinfo("База даних", db_info)
        else:
            messagebox.showerror("Помилка", response.json().get("error", "Unknown error"))

# Ініціалізація GUI
def main():
    root = tk.Tk()
    app = ArchiverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
