import tkinter as tk
from sgr_eg import sgreg
from tkinter import messagebox
import pygame

music = "Defrag-keygen-shedevr-Muzyka-iz-keygenov-8-bit - 8ми битный шедевр_(tropicmusic.ru).mp3"
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()
pygame.mixer.init()


def close():
    window.destroy()


def calc():
    A = float(arg_A.get())
    lbl_result.configure(text=sgreg(A))
    tk.messagebox.showinfo('Values', f'{sgreg(A)}')


window = tk.Tk()
window.title("Title")
window.geometry('360x240')
bg = tk.PhotoImage(file='Profession-Footballer-PNG-File.png')  # png

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='c')

label_pic = tk.Label(frame, image=bg)
label_pic.place(x=0, y=0)

lbl_A = tk.Label(frame, text='Enter the value:', font=("Arial", 30), bg='#999900', fg='#dddddd')
lbl_A.grid(column=0, row=0, padx=10, pady=20)
arg_A = tk.Entry(frame, width=30)
arg_A.insert(0, '1')
arg_A.grid(column=0, row=1, padx=10, pady=20)

lbl_result = tk.Label(frame, text='')

btn = tk.Button(frame, text='generation', font=('Arival', 15), command=calc)
btn.grid(column=0, row=3)
exit = tk.Button(frame, text='Cancel', font=('Arival', 15), command=close)
exit.grid(column=2, row=3)

frame.mainloop()
