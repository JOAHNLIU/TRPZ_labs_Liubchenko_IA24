import sqlite3

class DatabaseManager:
    def __init__(self, db_name="archiver.db"):
        self.db_name = db_name
        self.create_tables()
        self.migrate_data()

    def create_connection(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        return connection, cursor

    def create_tables(self):
        connection, cursor = self.create_connection()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS archives_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                archive_id INTEGER,
                path TEXT NOT NULL,
                FOREIGN KEY (archive_id) REFERENCES archives_new (id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        connection.close()

    def migrate_data(self):
        connection, cursor = self.create_connection()
        cursor.execute("""
            INSERT INTO archives_new (id, name, timestamp)
            SELECT id, name, 'N/A' FROM archives
        """)
        cursor.execute("DROP TABLE archives")
        cursor.execute("ALTER TABLE archives_new RENAME TO archives")
        connection.commit()
        connection.close()

    def add_archive(self, name, timestamp):
        connection, cursor = self.create_connection()
        cursor.execute("INSERT INTO archives (name, timestamp) VALUES (?, ?)", (name, timestamp))
        connection.commit()
        archive_id = cursor.lastrowid
        connection.close()
        return archive_id

    def add_file(self, archive_id, file_path):
        connection, cursor = self.create_connection()
        cursor.execute("INSERT INTO files (archive_id, path) VALUES (?, ?)", (archive_id, file_path))
        connection.commit()
        connection.close()

    def add_notification(self, message):
        connection, cursor = self.create_connection()
        cursor.execute("INSERT INTO notifications (message) VALUES (?)", (message,))
        connection.commit()
        connection.close()

    def get_archives(self):
        connection, cursor = self.create_connection()
        cursor.execute("SELECT id, name, timestamp FROM archives")
        archives = cursor.fetchall()
        connection.close()
        return archives

    def get_files_in_archive(self, archive_id):
        connection, cursor = self.create_connection()
        cursor.execute("SELECT path FROM files WHERE archive_id = ?", (archive_id,))
        files = cursor.fetchall()
        connection.close()
        return files

    def clear_database(self):
        connection, cursor = self.create_connection()
        cursor.execute("DELETE FROM archives")
        cursor.execute("DELETE FROM files")
        cursor.execute("DELETE FROM notifications")
        connection.commit()
        connection.close()
