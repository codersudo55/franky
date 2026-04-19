# main.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from core.file_loader import load_file

class FrankyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Franky")
        self.setGeometry(500, 300, 600, 400)

        layout = QVBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter file path...")

        self.button = QPushButton("Open")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        self.setLayout(layout)

        self.button.clicked.connect(self.load_file)

    def load_file(self):
        path = self.input_box.text()
        try:
            df = load_file(path)
            self.output.setText(df.head().to_string())
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

app = QApplication(sys.argv)
window = FrankyApp()
window.show()
sys.exit(app.exec())