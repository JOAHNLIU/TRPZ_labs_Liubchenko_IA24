from archive_process_observer import ArchiveProcessObserver
from gui import ArchiverApp
import tkinter as tk

def main():
    try:
        root = tk.Tk()
        app = ArchiverApp(root)
        observer = ArchiveProcessObserver()
        app.add_observer_to_archiver(observer)
        root.mainloop()
    except KeyboardInterrupt:
        print("Program interrupted. Exiting gracefully.")

if __name__ == "__main__":
    main()
