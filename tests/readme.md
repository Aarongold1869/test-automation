# tests/test_readme.md

import pytest
import sqlite3
from unittest import mock
from add_numbers import add_two_numbers

# 1. Test for add_two_numbers
def test_add_two_numbers():
    assert add_two_numbers(2, 3) == 5

# 2. Example organization (answer, not code)
# tests/
#   conftest.py  # shared fixtures
#   unit/
#   integration/
#   e2e/
#   fixtures/
#   test_module1.py

# 3. SQLite fixture
@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

def test_temp_db(temp_db):
    cur = temp_db.cursor()
    cur.execute("CREATE TABLE test (id INTEGER)")
    cur.execute("INSERT INTO test (id) VALUES (1)")
    cur.execute("SELECT id FROM test")
    assert cur.fetchone()[0] == 1

# 4. Parametrize example
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_two_numbers_param(a, b, result):
    assert add_two_numbers(a, b) == result

# 5. Mock REST API call
@mock.patch("requests.get")
def test_api_call(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}
    import requests
    resp = requests.get("http://example.com")
    assert resp.status_code == 200
    assert resp.json() == {"key": "value"}

# 6. Test code depending on system clock
@mock.patch("time.time", return_value=1234567890)
def test_time_dependent_code(mock_time):
    import time
    assert time.time() == 1234567890

# 7. Mark tests
@pytest.mark.slow
def test_slow():
    import time
    time.sleep(0.1)
    assert True

@pytest.mark.xfail
def test_expected_fail():
    assert False

# 8. Mock file reading
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
def test_read_file(mock_open):
    from read_file import read_file_contents
    assert read_file_contents("dummy.txt") == "data"

# 9. Testing types (answer, not code)
# Unit: test small pieces (functions/classes).
# Integration: test interactions between modules.
# End-to-end: test full workflow.
# Automate unit tests first.

# 10. Flaky test (answer, not code)
# Flaky: sometimes passes, sometimes fails.
# Deal: isolate cause, use retries, fix nondeterminism.