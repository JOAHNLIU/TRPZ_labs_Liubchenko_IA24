from component import Component

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, depth):
        print("-" * depth + self.name)
        for child in self.children:
            child.display(depth + 2)

    def archive(self, archiver, db_manager, archive_id):
        for child in self.children:
            child.archive(archiver, db_manager, archive_id)
