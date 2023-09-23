import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.w = None
        self.image_folder = "/home/ashwin/task-08/poke_images"
        self.image_files = []
        self.current_image_index = 0
        self.load_images()
        self.display_current_image()
        
    def initUI(self):
        self.setWindowTitle("Pokédex")
        self.setFixedSize(850, 500)

        self.setStyleSheet("""
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 32px;
                color: white;
            }
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.labelpic = QLabel(self)
        self.labelpic.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelpic)

        self.labelname = QLabel(self)
        self.labelname.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelname)





        next_button = QPushButton("Previous",self)
        next_button.clicked.connect(self.show_next_image)
        next_button.setGeometry(10, 450, 410, 43)

        previous_button = QPushButton("Next",self)
        previous_button.clicked.connect(self.show_previous_image)
        previous_button.setGeometry(430, 450, 410, 43)


        self.show()

    def load_images(self):
        # Load image files from the specified folder
        if os.path.exists(self.image_folder):
            self.image_files = [f for f in os.listdir(self.image_folder) if f.endswith(('.jpg', '.png'))]
            self.image_files.sort()

    def display_current_image(self):
        if self.image_files:
            image_path = os.path.join(self.image_folder, self.image_files[self.current_image_index])
            pixmap = QPixmap(image_path)
            self.labelpic.setPixmap(pixmap)
            image_name = os.path.splitext(self.image_files[self.current_image_index])[0]
            self.labelname.setText(image_name)

    def show_next_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
            self.display_current_image()

    def show_previous_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
            self.display_current_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
