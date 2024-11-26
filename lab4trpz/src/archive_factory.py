from archiver import Archiver



class ArchiveFactory:
    @staticmethod
    def create_archiver(archive_type):
        if archive_type in ['zip', 'tar.gz', 'rar']:
            return Archiver(archive_type)
        else:
            raise ValueError(f"Непідтримуваний тип архіву: {archive_type}")
