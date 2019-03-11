from get_directory import get_subdirectories
def test_empty_dir():
    assert get_subdirectories('') == []

def test_nonempty_dir():
    assert get_subdirectories('.') != []