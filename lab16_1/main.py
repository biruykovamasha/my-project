import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow  # Импортируем наш сгенерированный интерфейс

# 1. Создание класса и инициализацияя
class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_UI()

# 2. Настройка интерфейса и Сигналы
    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('icon.png'))
        self.ui.input_cur.setPlaceholderText('Из валюты (напр. USD)')
        self.ui.input_sum.setPlaceholderText('Сколько (напр. 100)')
        self.ui.output_cur.setPlaceholderText('В валюту (напр. RUB)')
        self.ui.output_sum.setPlaceholderText('Итог')

        self.ui.pushButton.clicked.connect(self.converter)

# 3. защита от ошибок
    def converter(self):
        try:
            c = CurrencyConverter()

            in_cur = self.ui.input_cur.text().upper().strip()  # .upper() сделает usd -> USD
            out_cur = self.ui.output_cur.text().upper().strip()

            in_sum = float(self.ui.input_sum.text())

            result = c.convert(in_sum, in_cur, out_cur)

            self.ui.output_sum.setText(str(round(result, 2)))

        except ValueError:
            self.ui.output_sum.setText("Ошибка: введите число!")
        except Exception as e:
            self.ui.output_sum.setText("Ошибка проверки!")


# 4. запуск приложения
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = CurrencyConv()
    application.show()
    sys.exit(app.exec_())