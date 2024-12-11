from archiver import Archiver
from database_manager import DatabaseManager
from composite import Composite
from leaf import Leaf

class ArchiveHandler:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_archive(self, archive_name, files, timestamp):
        root_component = Composite("root")
        for file_path in files:
            leaf = Leaf(file_path.split("/")[-1], file_path)
            root_component.add(leaf)
        archive_id = self.db_manager.add_archive(archive_name, timestamp)
        archiver = Archiver(archive_name.split('.')[-1])
        archiver.create_archive(archive_name)
        root_component.archive(archiver, self.db_manager, archive_id)
        return archive_id

    def extract_archive(self, archive_name, destination_folder):
        archiver = Archiver(archive_name.split('.')[-1])
        archiver.extract_archive(archive_name, destination_folder)
