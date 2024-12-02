from strategies import ZipStrategy, RarStrategy, TarGzStrategy

class ArchiveFactory:
    @staticmethod
    def create_archiver(archive_type):
        if archive_type == 'zip':
            return ZipStrategy()
        elif archive_type == 'rar':
            return RarStrategy()
        elif archive_type == 'tar.gz':
            return TarGzStrategy()
        else:
            return None
