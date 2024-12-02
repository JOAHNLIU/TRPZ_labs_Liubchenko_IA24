import tarfile

class TarGzStrategy:
    def create_archive(self, file_name):
        self.archive = tarfile.open(file_name, 'w:gz')
        print("Creating TAR.GZ archive...")
    
    def add_file(self, file_path):
        if hasattr(self, 'archive') and self.archive:
            self.archive.add(file_path)
        else:
            print("Error: Archive not initialized")

    def close(self):
        if hasattr(self, 'archive') and self.archive:
            self.archive.close()
            print("TAR.GZ archive closed")

    def extract_archive(self, archive_path, destination_folder):
        with tarfile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(destination_folder)
            print("Extracting TAR.GZ archive...")
