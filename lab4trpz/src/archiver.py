import zipfile
import tarfile
import rarfile


class Archiver:
    def __init__(self, archive_type):
        self.archive_type = archive_type
        self.archive = None

    def create_archive(self, file_name):
        if self.archive_type == 'zip':
            self.archive = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
        elif self.archive_type == 'tar.gz':
            self.archive = tarfile.open(file_name, 'w:gz')
        elif self.archive_type == 'rar':
            raise NotImplementedError("RAR підтримується лише для читання")
        else:
            raise ValueError(f"Непідтримуваний тип архіву: {self.archive_type}")

    def add_file(self, file_path):
        if not self.archive:
            raise RuntimeError("Архів ще не створено!")

        if self.archive_type == 'zip':
            self.archive.write(file_path, arcname=file_path.split('/')[-1])
        elif self.archive_type == 'tar.gz':
            self.archive.add(file_path)

    def close(self):
        if self.archive:
            self.archive.close()
