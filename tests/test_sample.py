import app.sample
import tempfile

def test_sample():
    assert app.sample.countdown(2) == 1
    assert app.sample.countdown(0) == None

def test_countdown_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = f"{tmpdir}/contdown.txt"
        with  open(filename, "w") as fp:
            fp.write("4")
        assert app.sample.countdown_file(filename) == 3
        with open(filename, "r") as fp:
            body = fp.read()
        assert body  == "4\n3"