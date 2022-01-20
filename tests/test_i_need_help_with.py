import os
import sqlite3
import pytest


@pytest.fixture(scope='session', autouse=True)
def create_and_fill_test_db(tmpdir_factory):

    db_dir = tmpdir_factory.mktemp("data")
    db_fn = db_dir.join("test_db.db")
    db_filepath = os.path.join(db_fn.dirname, db_fn.basename)
    con = sqlite3.connect(db_filepath)
    cur = con.cursor()

    cur.execute("""CREATE TABLE Table_1 (name TEXT PRIMARY KEY, age INT)""")
    cur.execute("""CREATE TABLE Table_2 (name TEXT PRIMARY KEY, age INT)""")

    with con:
        cur.execute("INSERT INTO Table_1 VALUES (?, ?)", ("Nikita", 15))
        cur.execute("INSERT INTO Table_1 VALUES (?, ?)", ("Alex", 20))
        cur.execute("INSERT INTO Table_1 VALUES (?, ?)", ("Maria", 25))
        cur.execute("INSERT INTO Table_1 VALUES (?, ?)", ("Boris", 34))
        cur.execute("INSERT INTO Table_1 VALUES (?, ?)", ("Liza", 35))
        cur.execute("INSERT INTO Table_2 VALUES (?, ?)", ("Nikita", 15))
        cur.execute("INSERT INTO Table_2 VALUES (?, ?)", ("Alex", 21))
        cur.execute("INSERT INTO Table_2 VALUES (?, ?)", ("Maria", 23))
        cur.execute("INSERT INTO Table_2 VALUES (?, ?)", ("Boris", 34))
        cur.execute("INSERT INTO Table_2 VALUES (?, ?)", ("Liza", 33))

    cur.close()
    con.close()

    yield db_filepath


def test_get_from_db(create_and_fill_test_db):
    con = sqlite3.connect(create_and_fill_test_db)
    cur = con.cursor()
    rows_from_table_1 = cur.execute("SELECT * from Table_1").fetchall()
    rows_from_table_2 = cur.execute("SELECT * from Table_2").fetchall()

    pairs = []

    for row_t1 in rows_from_table_1:
        for row_t2 in rows_from_table_2:
            if row_t1[0] == row_t2[0]:
                pairs.append((row_t1, row_t2))

    for pair in pairs:
        print(pair)



"""
Прошу помочь написать тесты, которые бы сравнивали попарно значения в списке pairs
Ниже пример как +- она бы выглядела с параметризацией
"""


@pytest.mark.parametrize('pair', [
    (('Nikita', 15), ('Nikita', 15)),
    (('Alex', 20), ('Alex', 21)),
    (('Maria', 25), ('Maria', 23)),
    (('Boris', 34), ('Boris', 34)),
    (('Liza', 35), ('Liza', 33))])
def test_simple_equals_in_pair(pair):
    assert pair[0] == pair[1]
