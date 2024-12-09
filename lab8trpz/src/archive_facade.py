from archiver import Archiver
from database_manager import DatabaseManager

class ArchiveFacade:
    def __init__(self, archive_type, db_manager):
        self.archiver = Archiver(archive_type)
        self.db_manager = db_manager
    
    def create_archive(self, file_name, component):
        archive_id = self.db_manager.add_archive(file_name)
        self.archiver.create_archive(file_name)
        self.archiver.archive_component(component, self.db_manager, archive_id)
    
    def extract_archive(self, archive_path, destination_folder):
        self.archiver.extract_archive(archive_path, destination_folder)
