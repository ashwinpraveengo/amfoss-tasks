import sys
import requests
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from display import MainWindow
import os

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.background_black = False  
        self.set_background_image()

        self.setFixedSize(850, 500)

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 50, 600, 70)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 100, 280, 40)

        search_button = QPushButton("Search", self)
        search_button.setGeometry(50, 300, 160, 43)
        search_button.clicked.connect(self.search_pokemon)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.open_main_window)

        self.pokemon_label = QLabel(self)
        self.pokemon_label.setGeometry(400, 50, 200, 200)

        self.pokemon_details_label = QLabel(self)
        self.pokemon_details_label.setGeometry(400, 270, 400, 200)

        self.captured_pokemon_pixmap = None 
    def set_background_image(self):
        if self.background_black:

            self.setStyleSheet("""
                QMainWindow {
                    background-color: black;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow {
                    background-image: url("/home/ashwin/task-08/assets/landing.jpg"); /* Replace with your background image path */
                    background-repeat: no-repeat;
                    background-position: center;
                }
            """)

    def search_pokemon(self):
        global pokemon_name
        pokemon_name = self.textbox.text().lower()
        if not pokemon_name:
            return

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data['name'].capitalize()
            types = ', '.join([t['type']['name'].capitalize() for t in pokemon_data['types']])
            abilities = ', '.join([a['ability']['name'].capitalize() for a in pokemon_data['abilities']])
            height = pokemon_data['height']/10  
            weight = pokemon_data['weight']/10  

            self.pokemon_details_label.setText(f"Name: {name}\n"
                                               f"Type(s): {types}\n"
                                               f"Abilities: {abilities}\n"
                                               f"Height: {height} m\n"
                                               f"Weight: {weight} kg")
            image_url = pokemon_data['sprites']['front_default']
            if image_url:
                pixmap = self.load_image_from_url(image_url)
                if pixmap:
                    pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio)
                    self.pokemon_label.setPixmap(pixmap)
                    self.captured_pokemon_pixmap = pixmap  
                else:
                    self.pokemon_label.clear()
            else:
                self.pokemon_label.clear()


            self.background_black = True
            self.set_background_image()
        else:
            self.pokemon_label.clear()
            self.pokemon_details_label.setText("Pokémon not found")

    def load_image_from_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_data = response.content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                return pixmap
            else:
                return None
        except Exception as e:
            print(f"Error loading image: {str(e)}")
            return None

    def capture_pokemon(self):
        if self.captured_pokemon_pixmap:
            if not os.path.exists("/home/ashwin/task-08/poke_images"):
                os.makedirs("/home/ashwin/task-08/poke_images")

            self.captured_pokemon_pixmap.save(f"/home/ashwin/task-08/poke_images/{pokemon_name}.png", "PNG")

            msg_box = QMessageBox()
            custom_icon = QIcon("/home/ashwin/task-08/pokeball-logo-DC23868CA1-seeklogo.com.png")
            msg_box.setIconPixmap(custom_icon.pixmap(64, 64))  
            msg_box.setWindowTitle("Capture")
            msg_box.setText(f"You captured {pokemon_name.capitalize()}! It's saved as '{pokemon_name}.png'")

            msg_box.exec()
            
            msg_box


    def open_main_window(self, checked):
        if self.w is None:
            self.w = MainWindow()
        self.w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
