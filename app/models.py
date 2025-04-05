from sqlalchemy import text
from . import db

def create_tables():
    with db.engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS pictures (
                id CHAR(36) PRIMARY KEY,
                path VARCHAR(255) NOT NULL,
                date VARCHAR(19) NOT NULL
            );
        """))

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS tags (
                tag VARCHAR(32),
                picture_id CHAR(36),
                confidence FLOAT,
                date VARCHAR(19) NOT NULL,
                PRIMARY KEY (tag, picture_id),
                FOREIGN KEY (picture_id) REFERENCES pictures(id)
            );
        """))
