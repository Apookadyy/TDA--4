import os
import tempfile
from file_organizer import categorize_file, is_duplicate

def test_file_categorization():
    assert categorize_file("report.pdf") == "Documents"
    assert categorize_file("image.jpg") == "Images"
    assert categorize_file("video.mp4") == "Videos"
    assert categorize_file("random.xyz") == "Others"

def test_duplicate_detection():
    with tempfile.NamedTemporaryFile(delete=False) as f1, \
         tempfile.NamedTemporaryFile(delete=False) as f2:
        f1.write(b"duplicate content")
        f2.write(b"duplicate content")

    assert is_duplicate(f1.name, f2.name) is True

    os.remove(f1.name)
    os.remove(f2.name)
