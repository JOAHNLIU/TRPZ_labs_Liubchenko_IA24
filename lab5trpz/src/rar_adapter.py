import rarfile

class RarAdapter:
    def __init__(self):
        self.archive = None

    def create_archive(self, file_name):
        raise NotImplementedError("RAR підтримується лише для читання")

    def add_file(self, file_path):
        raise NotImplementedError("RAR підтримується лише для читання")

    def close(self):
        pass
