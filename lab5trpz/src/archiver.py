from archive_factory import ArchiveFactory

class Archiver:
    def __init__(self, archive_type):
        self.adapter = ArchiveFactory.create_archiver(archive_type)

    def create_archive(self, file_name):
        self.adapter.create_archive(file_name)

    def add_file(self, file_path):
        self.adapter.add_file(file_path)

    def close(self):
        self.adapter.close()
