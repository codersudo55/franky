# franky_app.py
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QMessageBox,
    QLabel,QHBoxLayout
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

from core.file_loader import load_file

class FrankyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Franky")
        self.setWindowIcon(QIcon(os.path.join("assets", "franky_logo.png")))
        self.setGeometry(500, 300, 600, 400)

        main_layout = QVBoxLayout()

        # header layout (logo and title)
        header_layout = QHBoxLayout()

        logo_label = QLabel()
        pixMap = QPixmap(os.path.join("assets","franky_logo.png"))
        logo_label.setPixmap(pixMap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        title_label = QLabel("Franky")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        header_layout.addWidget(logo_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()

        # input + button + output
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter file path...")

        self.button = QPushButton("Open")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        # adding everything to main layout
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.input_box)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.output)

        self.setLayout(main_layout)

        # connect button
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