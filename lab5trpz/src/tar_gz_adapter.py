import tarfile

class TarGzAdapter:
    def __init__(self):
        self.archive = None

    def create_archive(self, file_name):
        self.archive = tarfile.open(file_name, 'w:gz')

    def add_file(self, file_path):
        self.archive.add(file_path)

    def close(self):
        self.archive.close()
