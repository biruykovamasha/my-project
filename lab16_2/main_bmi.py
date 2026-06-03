import sys
from PyQt5 import QtWidgets
from ui_bmi import Ui_MainWindow

class BMICalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(BMICalculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Калькулятор ИМТ')

        # Защита: если кнопка не найдена, мы узнаем об этом сразу, без вылета
        try:
            self.ui.btn_calc.clicked.connect(self.calculate_bmi)
        except AttributeError:
            print("ОШИБКА: Не найдена кнопка 'btn_calc'! Проверь objectName в Qt Designer.")

    def calculate_bmi(self):
        try:
            # 1. Получаем текст и заменяем запятую на точку (на случай русской раскладки)
            weight_text = self.ui.input_weight.text().replace(',', '.')
            height_text = self.ui.input_height.text().replace(',', '.')

            # 2. Превращаем в числа
            weight = float(weight_text)
            height = float(height_text)

            # 3. УМНАЯ ПРОВЕРКА: если рост больше 3, значит ввели в сантиметрах (например, 175)
            # Автоматически переводим в метры
            if height > 3:
                height = height / 100.0

            # 4. Проверка на адекватность данных
            if height <= 0 or weight <= 0:
                self.ui.output_result.setText("Введите числа\nбольше нуля!")
                return

            # 5. Расчет ИМТ
            bmi = weight / (height ** 2)

            # 6. Оценка по стандартам ВОЗ
            if bmi < 18.5:
                status = "Недостаточный вес"
            elif 18.5 <= bmi < 25:
                status = "Нормальный вес"
            elif 25 <= bmi < 30:
                status = "Избыточный вес"
            else:
                status = "Ожирение"

            # 7. Вывод результата
            result_text = f"Ваш ИМТ: {round(bmi, 1)}\n({status})"
            self.ui.output_result.setText(result_text)

        except ValueError:
            self.ui.output_result.setText("Ошибка:\nвведите только цифры!")
        except AttributeError as e:
            self.ui.output_result.setText("Ошибка имен!\nСмотри консоль PyCharm")
            print(f"ОШИБКА ИМЕНИ: {e}")
        except Exception as e:
            self.ui.output_result.setText("Неизвестная\nошибка")
            print(f"НЕИЗВЕСТНАЯ ОШИБКА: {e}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = BMICalculator()
    application.show()
    sys.exit(app.exec_())