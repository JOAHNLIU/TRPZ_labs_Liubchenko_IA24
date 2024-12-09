from component import Component

class Leaf(Component):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def add(self, component):
        raise Exception("Cannot add to a leaf")

    def remove(self, component):
        raise Exception("Cannot remove from a leaf")

    def display(self, depth):
        print("-" * depth + self.name)

    def archive(self, archiver, db_manager, archive_id):
        archiver.add_file(self.path)
        db_manager.add_file(archive_id, self.path)
