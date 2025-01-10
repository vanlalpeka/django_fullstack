import pytest
from .tests import Note

@pytest.fixture
def note():
    return Note()

def test_note_creation(note):
    assert note.title == ""
    assert note.content == ""

def test_note_set_title(note):
    note.title = "Test Title"
    assert note.title == "Test Title"

def test_note_set_content(note):
    note.content = "Test Content"
    assert note.content == "Test Content"

def test_note_str(note):
    note.title = "Test Title"
    note.content = "Test Content"
    assert str(note) == "Test Title: Test Content"

def test_note_empty_title(note):
    note.title = ""
    assert note.title == ""

def test_note_empty_content(note):
    note.content = ""
    assert note.content == ""