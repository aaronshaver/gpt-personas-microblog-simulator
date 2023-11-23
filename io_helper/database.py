import atexit
import sqlite3
from shared import global_config

class Database:
    """
    Usage:

    db = Database()
    cursor = db.get_cursor()
    ...perform operations using cursor
    ...the connection will close automatically when the script exits
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            try:
                print("Connecting to the database...")
                cls._instance.connection = sqlite3.connect(global_config.DB_NAME)
                # close db connection upon normal script exit
                atexit.register(cls._instance.close)
            except Exception as e:
                print(f"Database connection error: {e}")
                raise
        return cls._instance

    def get_cursor(self):
        return self._instance.connection.cursor()

    def get_connection(self):
        return self._instance.connection

    def close(self):
        if self._instance.connection:
            print("Closing database connection...")
            self._instance.connection.close()