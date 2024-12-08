from archive_factory import ArchiveFactory
from observable import Observable
import os

class Archiver(Observable):
    def __init__(self, archive_type):
        super().__init__()
        self.adapter = ArchiveFactory.create_archiver(archive_type)
        self.files_added = set()
        self.archive_initialized = False

    def create_archive(self, file_name):
        if self.adapter:
            self.adapter.create_archive(file_name)
            self.archive_initialized = True
            self.notify_observers(f"Archive {file_name} created")
        else:
            self.notify_observers("Error: Adapter not initialized")

    def add_file(self, file_path):
        if not self.archive_initialized:
            self.notify_observers("Error: Archive not initialized")
            return

        if os.path.exists(file_path):
            if file_path not in self.files_added:
                self.adapter.add_file(file_path)
                self.files_added.add(file_path)
                self.notify_observers(f"File {file_path} added to archive")
            else:
                self.notify_observers(f"File {file_path} already added to archive")
        else:
            self.notify_observers(f"Error: File {file_path} not found")

    def close(self):
        if not self.archive_initialized:
            self.notify_observers("Error: Archive not initialized")
            return

        if hasattr(self.adapter, 'close'):
            self.adapter.close()
            self.archive_initialized = False
            self.notify_observers("Archive process completed")

    def extract_archive(self, archive_path, destination_folder):
        if self.adapter:
            self.adapter.extract_archive(archive_path, destination_folder)
            self.notify_observers(f"Archive {archive_path} successfully extracted to {destination_folder}")
        else:
            self.notify_observers("Error: Adapter not initialized")
