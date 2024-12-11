from observer import Observer

class ArchiveProcessObserver(Observer):
    def update(self, message):
        print(f"Notification received: {message}")
