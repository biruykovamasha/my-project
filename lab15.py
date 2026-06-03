# Лабораторная 15.Бирюкова Мария
# Задание.15.1

# import tkinter as tk
# import requests
#
# API_KEY = "2d22a2d9ba43bec304baa1a56e186243"
#
# # 1.обработка запроса
# def get_weather():
#     city = city_entry.get().strip()
#     if not city:
#         result_label.config(text="Введите название города!")
#         return
#
# # 2.формирование и отправка запроса
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": "ru"
#     }
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#
# # 3.обработка ошибок
#         if data.get("cod") != 200:
#             result_label.config(text=f"Ошибка: {data.get('message', 'Неизвестная ошибка')}")
#             return
#
#         temp = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]
#         description = data["weather"][0]["description"]
#
# # 4.обновление интерфейса и обработка исключений
#         text = f"Температура: {temp}°C\nОщущается как: {feels_like}°C\n{description.capitalize()}"
#         result_label.config(text=text)
#
#     except Exception as e:
#         result_label.config(text=f"Не удалось получить данные.\nОшибка: {e}")
#
# # 5.создание графического интерфейса (GUI)
# root = tk.Tk()
# root.title("Погода")
# root.geometry("400x300")
#
# # 6.виджеты и компоновка
# label = tk.Label(root, text="Введите город:")
# label.pack(pady=5)
#
# city_entry = tk.Entry(root, width=30)
# city_entry.pack(pady=5)
#
# button = tk.Button(root, text="Узнать погоду", command=get_weather)
# button.pack(pady=10)
#
# result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
# result_label.pack(pady=10)
#
# root.mainloop()


# # Задание.15.2

import tkinter as tk
from tkinter import messagebox
import requests

# 1.обработка запроса
def get_city_info():
    city = entry_city.get().strip()
    if not city:
        messagebox.showwarning("Ошибка", "Введите название города!")
        return

# 2.формирование и отправка запроса
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json"

    try:
        response = requests.get(url)
        data = response.json()

# 3.проверяем, нашел ли API наш город
        if "results" in data and len(data["results"]) > 0:
            place = data["results"][0]

            name = place.get("name", city)
            country = place.get("country", "Неизвестно")
            region = place.get("admin1", "Неизвестно")
            population = place.get("population", "данных нет")
            elevation = place.get("elevation", "данных нет")

# 4.форматирование и вывод результата
            text = f" Информация о городе: {name.title()}\n\n"
            text += f" Страна: {country}\n"
            text += f" Регион: {region}\n"
            text += f" Население: {population:,} чел.\n"  # :, делает красивые пробелы (напр. 1 000 000)
            text += f" Высота над ур. моря: {elevation} м."

            result_label.config(text=text)
        else:
            result_label.config(
                text=f" Город '{city}' не найден.\nПопробуйте написать название на английском\nили проверить орфографию.")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось подключиться к интернету: {e}")


# 5.настраиваем интерфейс
root = tk.Tk()
root.title("Факты о городах мира")
root.geometry("400x300")
root.config(padx=20, pady=20)

# 6.виджеты и их размещение
tk.Label(root, text="Введите название города:", font=("Arial", 12)).pack(pady=5)

entry_city = tk.Entry(root, font=("Arial", 12), width=30)
entry_city.pack(pady=5)
entry_city.focus()  # Сразу ставим курсор в поле ввода

btn_get = tk.Button(root, text="Узнать факты", font=("Arial", 12), bg="#4CAF50", fg="white", command=get_city_info)
btn_get.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()