import rarfile

class RarStrategy:
    def create_archive(self, file_name):
        self.archive = rarfile.RarFile(file_name, 'w')
        print("Creating RAR archive...")
    
    def add_file(self, file_path):
        if hasattr(self, 'archive') and self.archive:
            self.archive.write(file_path)
        else:
            print("Error: Archive not initialized")

    def close(self):
        if hasattr(self, 'archive') and self.archive:
            self.archive.close()
            print("RAR archive closed")

    def extract_archive(self, archive_path, destination_folder):
        with rarfile.RarFile(archive_path, 'r') as rar_ref:
            rar_ref.extractall(destination_folder)
            print("Extracting RAR archive...")
