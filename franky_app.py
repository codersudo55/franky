# franky_app.py
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QMessageBox,
    QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem
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

        self.table = QTableWidget()

        # adding everything to main layout
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.input_box)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

        # connect button
        self.button.clicked.connect(self.load_file)

    def load_file(self):
        path = self.input_box.text()
        try:
            df = load_file(path)
            self.display_dataframe(df.head())
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def display_dataframe(self,df):
        self.table.clear()

        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])

        self.table.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                value = str(df.iat[row,col])
                self.table.setItem(row, col, QTableWidgetItem(value))
        
        self.table.resizeColumnsToContents() # auto-adjust column widths (small UX upgrade)

app = QApplication(sys.argv)
window = FrankyApp()
window.show()
sys.exit(app.exec())