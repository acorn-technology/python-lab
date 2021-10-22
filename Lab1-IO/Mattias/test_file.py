import pytest

from file import last_lines_simple, last_lines

CONTENT = """A
AWFEFae
agrgaergr argaer ga arg
ag"""

@pytest.fixture(scope="session")
def txt_file(tmp_path_factory):
    path = tmp_path_factory.mktemp("data") / "test.txt"
    with open(path, "w") as stream:
        stream.write(CONTENT)

    return path

def test_single_line(txt_file):
    assert last_lines_simple(txt_file, 1) == "ag"
    assert last_lines_simple(txt_file, 1) == last_lines(txt_file, 1)

def test_multi_line(txt_file):
    assert last_lines_simple(txt_file, 3).splitlines() == CONTENT.splitlines()[-3:]
    assert last_lines_simple(txt_file, 3) == last_lines(txt_file, 3)

def test_full_file(txt_file):
    assert last_lines_simple(txt_file, 100).splitlines() == CONTENT.splitlines()
    assert last_lines_simple(txt_file, 100) == last_lines(txt_file, 100)

class TestStuff:
    def test_foo(self):
        pass
    def bar():
        pass