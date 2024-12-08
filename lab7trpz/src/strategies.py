import zipfile
import rarfile
import tarfile

class ZipStrategy:
    def create_archive(self, file_name):
        self.archive = zipfile.ZipFile(file_name, 'w')
        print("Creating ZIP archive...")
    
    def add_file(self, file_path):
        if hasattr(self, 'archive') and self.archive:
            self.archive.write(file_path)
            print(f"Adding {file_path} to ZIP archive")
        else:
            print("Error: Archive not initialized")

    def close(self):
        if hasattr(self, 'archive') and self.archive:
            self.archive.close()
            print("ZIP archive closed")

    def extract_archive(self, archive, destination_folder):
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
            print("Extracting ZIP archive...")

class RarStrategy:
    def create_archive(self, file_name):
        self.archive = rarfile.RarFile(file_name, 'w')
        print("Creating RAR archive...")
    
    def add_file(self, file_path):
        if hasattr(self, 'archive') and self.archive:
            self.archive.write(file_path)
            print(f"Adding {file_path} to RAR archive")
        else:
            print("Error: Archive not initialized")

    def close(self):
        if hasattr(self, 'archive') and self.archive:
            self.archive.close()
            print("RAR archive closed")

    def extract_archive(self, archive, destination_folder):
        with rarfile.RarFile(archive, 'r') as rar_ref:
            rar_ref.extractall(destination_folder)
            print("Extracting RAR archive...")

class TarGzStrategy:
    def create_archive(self, file_name):
        self.archive = tarfile.open(file_name, 'w:gz')
        print("Creating TAR.GZ archive...")
    
    def add_file(self, file_path):
        if hasattr(self, 'archive') and self.archive:
            self.archive.add(file_path)
            print(f"Adding {file_path} to TAR.GZ archive")
        else:
            print("Error: Archive not initialized")

    def close(self):
        if hasattr(self, 'archive') and self.archive:
            self.archive.close()
            print("TAR.GZ archive closed")

    def extract_archive(self, archive, destination_folder):
        with tarfile.open(archive, 'r:gz') as tar_ref:
            tar_ref.extractall(destination_folder)
            print("Extracting TAR.GZ archive...")
