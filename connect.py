import psycopg2
from config import DB_CONFIG


def connect():
    missing = [key for key, value in DB_CONFIG.items() if not value]
    if missing:
        raise RuntimeError(f"Missing database settings: {', '.join(missing)}")

    return psycopg2.connect(**DB_CONFIG)
