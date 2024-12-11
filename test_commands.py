import unittest
from commands import execute_command
from fs_emulator import load_file_system

class TestCommands(unittest.TestCase):
    def setUp(self):
        self.fs = load_file_system("filesystem.zip")
        self.current_dir = "/"

    def test_ls(self):
        output = execute_command("ls", self.fs, self.current_dir)
        self.assertIsInstance(output, str)

    def test_cd(self):
        self.current_dir, _ = execute_command("cd folder", self.fs, self.current_dir)
        self.assertEqual(self.current_dir, "/folder")

    def test_tac(self):
        output = execute_command("tac one two three", self.fs, self.current_dir)
        self.assertEqual(output, "three two one")

    def test_uptime(self):
        output = execute_command("uptime", self.fs, self.current_dir)
        self.assertTrue(output.startswith("Uptime:"))

if __name__ == "__main__":
    unittest.main()
