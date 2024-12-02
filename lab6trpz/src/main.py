from archive_process_observer import ArchiveProcessObserver
from gui import ArchiverApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = ArchiverApp(root)
    observer = ArchiveProcessObserver()
    app.add_observer_to_archiver(observer)
    root.mainloop()

if __name__ == "__main__":
    main()
