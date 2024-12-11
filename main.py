pip install PyQt5 toml zipfile lxml установить это в bash

import sys
import toml
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout, QWidget
from commands import execute_command
from fs_emulator import load_file_system

class ShellEmulator(QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.init_ui()
        self.fs = load_file_system(config["fs_path"])
        self.current_dir = "/"

    def init_ui(self):
        self.setWindowTitle("Shell Emulator")
        
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        
        self.input = QLineEdit(self)
        self.input.returnPressed.connect(self.run_command)
        
        layout = QVBoxLayout()
        layout.addWidget(self.output)
        layout.addWidget(self.input)
        
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def run_command(self):
        command = self.input.text()
        self.input.clear()
        user_prompt = f"{self.config['username']}@emulator:{self.current_dir}$ "
        try:
            result = execute_command(command, self.fs, self.current_dir)
            self.output.append(user_prompt + command)
            if isinstance(result, tuple):
                self.current_dir, output = result
                if output:
                    self.output.append(output)
            else:
                self.output.append(result)
        except Exception as e:
            self.output.append(f"Error: {e}")

if __name__ == "__main__":
    config = toml.load("config.toml")
    app = QApplication(sys.argv)
    emulator = ShellEmulator(config)
    emulator.show()
    sys.exit(app.exec_())
