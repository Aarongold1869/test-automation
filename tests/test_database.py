
def test_db(temp_db):
    cur = temp_db.cursor()
    cur.execute("CREATE TABLE test (id INTEGER)")
    cur.execute("INSERT INTO test (id) VALUES (1)")
    cur.execute("SELECT id FROM test")
    assert cur.fetchone()[0] == 1