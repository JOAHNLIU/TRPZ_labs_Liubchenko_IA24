from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def display(self, depth):
        pass

    @abstractmethod
    def archive(self, archiver):
        pass
