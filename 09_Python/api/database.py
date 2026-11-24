
import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

# Load .env from the same folder as this Python file
ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_FILE)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "solar360_db"),
    "port": int(os.getenv("DB_PORT", "3306"))
}


def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection

    except mysql.connector.Error as error:
        print(f"Database connection error: {error}")
        return None
