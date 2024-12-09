from gui import ArchiverApp
import tkinter as tk

def main():
    # Ініціалізація GUI
    root = tk.Tk()
    app = ArchiverApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()
