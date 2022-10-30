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