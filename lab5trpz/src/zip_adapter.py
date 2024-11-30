import zipfile

class ZipAdapter:
    def __init__(self):
        self.archive = None

    def create_archive(self, file_name):
        self.archive = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)

    def add_file(self, file_path):
        self.archive.write(file_path, arcname=file_path.split('/')[-1])

    def close(self):
        self.archive.close()
