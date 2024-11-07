from tkinter import *
from pygame import mixer
from PIL import Image, ImageTk  # Импортируем необходимые модули из Pillow
import string
import random

#-----------Работаем со звуком--------
mixer.init()

def play_music():
    mixer.music.load("Playboi_Carti_Bryson_Tiller_-_Fell_In_Luv_55954079.mp3")
    mixer.music.play(loops=-1)

# ---------Класс для анимированного GIF-----------
class AnimatedGIF(Label):
    def __init__(self, master, path, width=None, height=None):
        Label.__init__(self, master)
        self.frames = []
        self.width = width
        self.height = height
        self.load_gif(path)
        self.index = 0
        self.update()

    def load_gif(self, path):
        img = Image.open(path)
        for frame in range(img.n_frames):
            img.seek(frame)
            if self.width and self.height:
                # Изменяем размер каждого кадра
                img.thumbnail((self.width, self.height))
            self.frames.append(ImageTk.PhotoImage(img.copy()))

    def update(self):
        self.configure(image=self.frames[self.index])
        self.index += 1
        if self.index >= len(self.frames):
            self.index = 0
        self.after(100, self.update)  # обновление каждые 100 мс

# ---------Создаем "голое" окно-------
window = Tk()
width = 718
height = 404
window.title("Let's go")
window.geometry(f"{width}x{height}+400+150")

# ------------Создаем фон-----------
background_image = Image.open('zeldabreath_fichavj.png')  # Загружаем изображение через PIL
background_image = ImageTk.PhotoImage(background_image)  # Преобразуем в формат, поддерживаемый Tkinter

lbl_bg = Label(window, image=background_image)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

# --------Создание фрейма, в котором будут хранится все метки-----------
frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

# -------------Функция для сохранения значения из окна ввода-------------
entry_var = StringVar()

def save_entry_value():
    saved_value = entry_var.get()

    # Генерация случайных блоков
    blocks = [''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for _ in range(len(saved_value))]

    # Функция для сдвига строки влево или вправо
    def shift(s, n, direction):
        return s[-n:] + s[:-n] if direction == 'right' else s[n:] + s[:n]

    # Генерация ключа с сдвигами
    result = []
    for i, block in enumerate(blocks):
        shift_amount = int(saved_value[i])
        direction = 'right' if i % 2 == 0 else 'left'
        result.append(shift(block, shift_amount, direction))

    # Отображение ключа
    final_key = '-'.join(result)
    lbl_result.configure(text=final_key)



# ----------Создаём надпись, которая будет пояснять, что именно нужно ввести------------------
lbl_roots = Label(frame, text='Введите DEC-число в 3 знака')
lbl_roots.grid(column=0, row=0)

# ---------Создаем поле ввода-----------
entry = Entry(frame, textvariable=entry_var, width=30)
entry.grid(column=0, row=1, padx=10, pady=15)

# ---------Создаем кнопку сохранения значения-----------
save_button = Button(frame, text="Сгенерировать", command=save_entry_value)
save_button.grid(column=1, row=1, padx=10, pady=15)

# ---------------Сгенерированный ключ-----------
lbl_result = Label(frame, text='Text me your code', font=('Arial', 10))
lbl_result.grid(column=0, row=2)

# -----------Добавление анимации GIF с изменением размера и центрированием-----------
gif_animation = AnimatedGIF(frame, "200.gif", width=200, height=200)  # Уменьшаем до 200x200 пикселей
gif_animation.grid(column=0, row=3, padx=10, pady=10)

play_music() # включаем музыку
window.mainloop()  # запускаем основной цикл
