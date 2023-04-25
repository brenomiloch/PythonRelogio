import tkinter as tk
from tkinter import *
import os
import locale
from time import strftime

root = tk.Tk()
root.title('Relogio')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600,320)
root.configure(background='#1d1d1d')

def get_recado():
    username = os.getlogin()
    recado.config(text='Olá ' + username)

def get_datatimes():
    
    locale.setlocale(locale.LC_TIME, "pt-BR.UTF-8")
    data_relogio = strftime(' %a, %d %b %Y')
    #os.environ['TZ'] = 'Europe/London'
    data.config(text=data_relogio)

def get_horas():
    locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")
    hora_relogio = strftime('%H:%M:%S')
    horas.config(text=hora_relogio)
    horas.after(1000, get_horas)

tela = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()

recado = Label(root, bg='#1d1d1d',fg='#0A4D68', font=('Montserrat', 15))
recado.pack()

data = Label(root, bg='#1d1d1d',fg='#0A4D68', font=('Montserrat', 15))
data.pack(pady=2)

horas = Label(root, bg='#1d1d1d',fg='#0A4D68', font=('Montserrat', 64, 'bold'))
horas.pack(pady=2)

get_recado()
get_datatimes()
get_horas()

root.mainloop()