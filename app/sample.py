def countdown(x):
    """
    与えた数から1減らして返却する
    :param x: 対象の数字
    :return: 1減らした数字
    >>> countdonw(2)
    1
    """
    if x < 1:
        return None
    return x - 1

def countdown_file(filename):
    """
    与えたファイルの、末尾行の数字を読み取り1減らして追記する
    :param filename: ファイル名
    :return: ファイル末尾の数字から1減らした数字
    >>> countdown_file(filename)
    1
    """
    with open(filename, "r") as fp:
        lines = fp.readlines()
    x = int(lines[-1].strip())

    with open(filename, "a") as fp:
        fp.write(f"\n{(x-1)}")

    return x-1

def countdown_sqlite(db, key_name):
    """
    SQLiteのcountdownテーブルのkeyで指定したレコードのvalの値を1減らす
    :param db: SQLiteDBへのConnection
    :param key_name: キー名
    :return: 最新のレコードのvalの値
    """
    db.execute("update countdown set val = val - 1 where key = ?", (key_name,))
    SQL_SELECT_VAL = "select val from countdown where key = ?"
    return db.cursor().execute(SQL_SELECT_VAL, (key_name, )).fetchone()[0]
