import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hava Durumu Uygulaması")
        self.setGeometry(100, 100, 800, 600)

        # Menü çubuğu oluşturma
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Dosya")
        edit_menu = menubar.addMenu("Düzenle")
        view_menu = menubar.addMenu("Görünüm")
        help_menu = menubar.addMenu("Yardım")

        # Arama bileşenlerinin oluşturulması
        search_label = QLabel("Şehir:")
        self.search_box = QLineEdit()
        search_button = QPushButton("Ara")
        search_button.clicked.connect(self.search)

        search_hbox = QHBoxLayout()
        search_hbox.addWidget(search_label)
        search_hbox.addWidget(self.search_box)
        search_hbox.addWidget(search_button)

        # Sonuçları göstermek için tablo oluşturma
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Şehir', 'Sıcaklık (°C)', 'Nem (%)', 'Rüzgar Hızı (km/s)', 'Hava Durumu'])

        # Ana pencere düzenini oluşturma
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addLayout(search_hbox)
        main_layout.addWidget(self.table)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def search(self):
        city = self.search_box.text()

        # API isteği gönderme
        api_key = "51018b60257b50207fc63de7c53af5e1"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        if response["cod"] != "404":
            city_name = response['name']
            temp = response['main']['temp']
            humidity = response['main']['humidity']
            wind_speed = response['wind']['speed']
            weather_desc = response['weather'][0]['description']

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(city_name))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(temp)))
            self.table.setItem(row_position, 2, QTableWidgetItem(str(humidity)))
            self.table.setItem(row_position, 3, QTableWidgetItem(str(wind_speed)))
            self.table.setItem(row_position, 4, QTableWidgetItem(weather_desc))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

