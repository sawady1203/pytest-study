import sys
sys.path.append("../app")

import pytest
import tempfile
import app.sample
import sqlite3

def test_sample():
    assert app.sample.countdown(2) == 1
    assert app.sample.countdown(0) == None

@pytest.fixture
def my_tmp_path():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.mark.parametrize(
    "before_file_body, expect_return, except_file_body",
    [
        ("4", 3, "4\n3"),
        ("2\n1", 0, "2\n1\n0"),
    ]
)
def test_countdown_file(
    before_file_body, expect_return, except_file_body,
    my_tmp_path
):
    filename = f"{my_tmp_path}/contdown.txt"
    with  open(filename, "w") as fp:
        fp.write(before_file_body)
    assert app.sample.countdown_file(filename) == expect_return
    with open(filename, "r") as fp:
        body = fp.read()
    assert body  == except_file_body

@pytest.fixture
def sqlite_db():
    with sqlite3.connect(":memory:") as db:
        db.execute("create table countdown(key, string, val int, primary key(key))")
        yield db

@pytest.mark.parametrize(
    "before_dbvalue, expect_return, expect_dbvalue",
    [
        (4,3,3),
        (1,0,0)
    ]
)
def test_countdown_sqlite(
    before_dbvalue, expect_return, expect_dbvalue,
    sqlite_db
    ):
    key_name = "unittest"
    SQL_INSERT_VAL = "insert into countdown(key, val) values (?, ?)"
    SQL_SELECT_VAL = "select val from countdown where key=?"
    sqlite_db.execute(SQL_INSERT_VAL, (key_name, before_dbvalue))
    assert app.sample.countdown_sqlite(sqlite_db, key_name) == expect_return
    assert sqlite_db.cursor().execute(SQL_SELECT_VAL, (key_name, )).fetchone()[0] == expect_dbvalue
