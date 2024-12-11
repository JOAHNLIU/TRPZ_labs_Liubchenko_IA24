import sqlite3

class DatabaseManager:
    def __init__(self, db_name="archiver.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS archives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                archive_id INTEGER,
                path TEXT NOT NULL,
                FOREIGN KEY (archive_id) REFERENCES archives (id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()

    def add_archive(self, name):
        self.cursor.execute("INSERT INTO archives (name) VALUES (?)", (name,))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_file(self, archive_id, file_path):
        self.cursor.execute("INSERT INTO files (archive_id, path) VALUES (?, ?)", (archive_id, file_path))
        self.connection.commit()

    def add_notification(self, message):
        self.cursor.execute("INSERT INTO notifications (message) VALUES (?)", (message,))
        self.connection.commit()

    def get_archives(self):
        self.cursor.execute("SELECT * FROM archives")
        return self.cursor.fetchall()

    def get_files_in_archive(self, archive_id):
        self.cursor.execute("SELECT path FROM files WHERE archive_id = ?", (archive_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
