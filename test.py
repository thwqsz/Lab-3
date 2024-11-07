# git remote add upstream https://github.com/thwqsz/Lab-3.git
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Пример интерфейса")
root.geometry("400x300")

# Метка
label = tk.Label(root, text="Привет! Введите текст:")
label.pack(pady=10)

# Поле ввода
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Функция для кнопки
def on_button_click():
    user_text = entry.get()  # Получаем текст из поля ввода
    label_result.config(text=f"Вы ввели: {user_text}")  # Обновляем метку результатом

# Кнопка
button = tk.Button(root, text="Показать текст", command=on_button_click)
button.pack(pady=10)

# Метка для отображения результата
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Запуск основного цикла
root.mainloop()
