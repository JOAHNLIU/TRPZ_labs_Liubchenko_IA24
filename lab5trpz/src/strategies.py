class ZipStrategy:
    def create_archive(self, files):
        print("Creating ZIP archive...")
    
    def extract_archive(self, archive):
        print("Extracting ZIP archive...")

class RarStrategy:
    def create_archive(self, files):
        print("Creating RAR archive...")
    
    def extract_archive(self, archive):
        print("Extracting RAR archive...")

class TarGzStrategy:
    def create_archive(self, files):
        print("Creating TAR.GZ archive...")
    
    def extract_archive(self, archive):
        print("Extracting TAR.GZ archive...")
