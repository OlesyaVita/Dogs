from tkinter import *
import requests #для того чтобы загружать из интернета
import PIL import Image, ImageTK #чтобы обрабатывать изображения
from io import BytesIO #для обработки картинки


window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")


label = Label()
label.pack(pady=10)

button = Button(text='Загрузить изображение', command=show_image)
button.pack(pady=10)

window.mainloop()




