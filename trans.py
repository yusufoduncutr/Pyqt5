import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
from googletrans import Translator

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Arayüz öğelerini oluşturun
        self.setWindowTitle('Çeviri Uygulaması')
        self.resize(400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        self.input_label = QLabel('Metin:', self)
        grid_layout.addWidget(self.input_label, 0, 0)

        self.input_text = QLineEdit(self)
        grid_layout.addWidget(self.input_text, 0, 1)

        self.output_label = QLabel('Çeviri:', self)
        grid_layout.addWidget(self.output_label, 1, 0)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        grid_layout.addWidget(self.output_text, 1, 1)

        self.translate_button = QPushButton('Çevir', self)
        self.translate_button.clicked.connect(self.translate_text)
        grid_layout.addWidget(self.translate_button, 2, 1)

        # Çeviri API'si için Translator sınıfını oluşturun
        self.translator = Translator()

    def translate_text(self):
        input_text = self.input_text.text()
        translation = self.translator.translate(input_text, dest='tr')

        self.output_text.setText(translation.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
