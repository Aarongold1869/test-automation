import os
import pathlib
import pytest
import sqlite3

TMP_PATH = pathlib.Path.cwd()


@pytest.fixture(scope="session")
def temp_db():
    db_path = TMP_PATH / "test.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    with sqlite3.connect(db_path) as conn:
        yield conn
