from zip_adapter import ZipAdapter
from rar_adapter import RarAdapter
from tar_gz_adapter import TarGzAdapter

class ArchiveFactory:
    @staticmethod
    def create_archiver(archive_type):
        if archive_type == 'zip':
            return ZipAdapter()
        elif archive_type == 'tar.gz':
            return TarGzAdapter()
        elif archive_type == 'rar':
            return RarAdapter()
        else:
            raise ValueError(f"Непідтримуваний тип архіву: {archive_type}")
