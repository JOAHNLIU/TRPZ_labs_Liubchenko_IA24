from archiver import Archiver

class ArchiveFacade:
    def __init__(self, archive_type):
        self.archiver = Archiver(archive_type)
        print(f"Initializing ArchiveFacade with {archive_type} strategy")
    
    def create_archive(self, file_name, files_to_add):
        print("Facade: Creating archive...")
        self.archiver.create_archive(file_name)
        for file_path in files_to_add:
            print(f"Facade: Adding {file_path} to archive...")
            self.archiver.add_file(file_path)
        self.archiver.close()
        print("Facade: Archive creation completed.")
    
    def extract_archive(self, archive_path, destination_folder):
        print("Facade: Extracting archive...")
        self.archiver.extract_archive(archive_path, destination_folder)
        print("Facade: Archive extraction completed.")
    
    def add_files_to_archive(self, archive_path, files_to_add):
        print("Facade: Adding files to existing archive...")
        self.archiver = Archiver(archive_path.split('.')[-1])
        for file_path in files_to_add:
            print(f"Facade: Adding {file_path} to archive...")
            self.archiver.add_file(file_path)
        self.archiver.close()
        print("Facade: Files added to archive.")
