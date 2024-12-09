import zipfile

class ZipStrategy:
    def create_archive(self, file_name):
        self.archive = zipfile.ZipFile(file_name, 'w')
        print("Creating ZIP archive...")
    
    def add_file(self, file_path):
        if hasattr(self, 'archive') and self.archive:
            self.archive.write(file_path)
        else:
            print("Error: Archive not initialized")

    def close(self):
        if hasattr(self, 'archive') and self.archive:
            self.archive.close()
            print("ZIP archive closed")

    def extract_archive(self, archive_path, destination_folder):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
            print("Extracting ZIP archive...")
