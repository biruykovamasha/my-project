# Лабораторная 13.Бирюкова Мария.
# Задача 13.1

class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

# создаём экземпляр (конкретный ресторан)
newRestaurant = Restaurant("Вкусный уголок", "Итальянская")

# выводим атрибуты по-отдельности
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# вызываем методы
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Задача 13.2

class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

# создаём три разных ресторана
rest1 = Restaurant("Вкусный уголок", "Итальянская")
rest2 = Restaurant("Японский", "Японская")
rest3 = Restaurant("Казахский", "Казахская")

# вызываем describe_restaurant() для каждого
print("Ресторан 1")
rest1.describe_restaurant()

print("\nРесторан 2")
rest2.describe_restaurant()

print("\nРесторан 3")
rest3.describe_restaurant()

# Задача 13.3

class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.rating = 0          # начальный рейтинг

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")   # показывает рейтинг

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

    def update_rating(self, new_rating):   # новый метод
        self.rating = new_rating
        print(f"Рейтинг обновлён! Теперь {self.restaurant_name} имеет рейтинг {self.rating}")

# создаём ресторан
rest = Restaurant("Вкусный уголок", "Итальянская")
rest.describe_restaurant()  # рейтинг покажет 0

# меняем рейтинг
rest.update_rating(5)
rest.describe_restaurant()  # рейтинг станет 5