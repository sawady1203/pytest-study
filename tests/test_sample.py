import app.sample


def test_sample():
    assert app.sample.countdown(2) == 1
    assert app.sample.countdown(0) == None