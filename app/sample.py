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
    return 0