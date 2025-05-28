from tkinter import *
from PIL import Image, ImageTk
import time

"""TİMUR TOZAR , HASAN DORUK DANYILDIZ"""



konami_giris = []
konami_kodu = ["Up", "Up", "Down", "Down", "Left", "Right", "Left", "Right", "B", "A"]


WINDOW_WIDTH, WINDOW_HEIGHT = 400, 550

hesap = None
s1 = 0
s2 = 0

def yaz(x):
    giris.insert(len(giris.get()), str(x))

def islemler(x):
    global hesap, s1
    hesap = x
    try:
        s1 = float(giris.get())
    except ValueError:
        s1 = 0  
    giris.delete(0, 'end')

def hesapla():
    global s2, hesap, s1
    try:
        s2 = float(giris.get())
    except ValueError:
        s2 = 0  
    
    sonuc = 0
    if hesap == 0: sonuc = s1 + s2
    elif hesap == 1: sonuc = s1 - s2
    elif hesap == 2: sonuc = s1 * s2
    elif hesap == 3: sonuc = s1 / s2 if s2 != 0 else "Hata"

    giris.delete(0, 'end')
    giris.insert(0, str(sonuc))

    if hesap == 0 and s1 == 834 and s2 == 726:
        aktif_yon_tuslari()

def delete():
    giris.delete(0, 'end')

def aktif_yon_tuslari():
    for tus, (x, y) in yönler.items():
        Button(text=tus, font='Verdana 12 bold', width=6, height=2,
               command=lambda t=tus: kaydet_tus(t)).place(x=x, y=y)

def kaydet_tus(tus):
    global konami_giris
    konami_giris.append(tus)

    if konami_giris[-len(konami_kodu):] == konami_kodu:
        giris.delete(0, 'end')
        giris.insert(0, "KOD")
        pencere.after(1000, konami_sonucu)

def konami_sonucu():
    global resim_label
    pencere.geometry("1000x800")  
    
    resim = Image.open("photo.png") 
    resim = resim.resize((890, 500))  
    resim = ImageTk.PhotoImage(resim)

    resim_label = Label(pencere, image=resim)
    resim_label.image = resim  
    resim_label.place(x=100, y=100)


pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
pencere.configure(background='Black')
pencere.resizable(False, False)

giris = Entry(font='Verdana 16 bold', width=20, justify=RIGHT)
giris.place(x=20, y=20)


button_positions = [
    (20, 80), (110, 80), (200, 80),
    (20, 160), (110, 160), (200, 160),
    (20, 240), (110, 240), (200, 240),
    (110, 320), (20, 320)
]
button_texts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for i in range(10):
    Button(bg='#4D4D4D', fg='White', text=button_texts[i], font='Verdana 16 bold',
           width=6, height=2, command=lambda x=button_texts[i]: yaz(x)).place(x=button_positions[i][0], y=button_positions[i][1])

Button(bg='#4D4D4D', fg='White', text=".", font='Verdana 16 bold', width=6, height=2,
       command=lambda: yaz(".")).place(x=200, y=320)

Button(bg='#FF6103', fg='White', text="=", font='Verdana 16 bold', width=6, height=2,
       command=hesapla).place(x=110, y=400)

Button(bg='#B0B0B0', text="C", font='Verdana 16 bold', width=6, height=2,
       command=delete).place(x=200, y=400)


islem_positions = [(285, 80), (285, 160), (285, 240), (285, 320)]
islem_texts = ["+", "-", "x", "/"]

for i in range(4):
    Button(bg='#B0B0B0', font='Verdana 16 bold', width=6, height=2, text=islem_texts[i],
           command=lambda x=i: islemler(x)).place(x=islem_positions[i][0], y=islem_positions[i][1])


yönler = {
    "Up": (160, 420),
    "Down": (160, 480),
    "Left": (80, 450),
    "Right": (240, 450)
}

Button(text="A", font='Verdana 12 bold', width=6, height=2,
       command=lambda: kaydet_tus("A")).place(x=50, y=500)

Button(text="B", font='Verdana 12 bold', width=6, height=2,
       command=lambda: kaydet_tus("B")).place(x=250, y=500)

pencere.mainloop()
