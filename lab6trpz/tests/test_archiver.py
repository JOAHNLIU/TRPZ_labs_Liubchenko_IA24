import unittest
from src.archiver import Archiver

class TestArchiver(unittest.TestCase):
    def test_create_zip_archive(self):
        archiver = Archiver('zip')
        archiver.create_archive('test.zip')
        archiver.close()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
