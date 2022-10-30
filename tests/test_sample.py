import sys
sys.path.append("../app")

import pytest
import sample

def test_sample():
    assert app.sample.countdown(2) == 1
    assert app.sample.countdown(0) == None

@pytest.mark.parametrize(
    "before_file_body, expect_return, except_file_body",
    [
        ("4", 3, "4\n3"),
        ("2\n1", 0, "2\n1\n0"),
    ]
)
def test_countdown_file(
    before_file_body, expect_return, except_file_body,
    tmp_path
):
    filename = f"{tmp_path}/contdown.txt"
    with  open(filename, "w") as fp:
        fp.write(before_file_body)
    assert app.sample.countdown_file(filename) == expect_return
    with open(filename, "r") as fp:
        body = fp.read()
    assert body  == except_file_body