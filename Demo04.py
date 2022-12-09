import configparser
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import constants as CN
from Demo05 import *
from configparser import ConfigParser
import ciph, os.path

def click_exit1(event=None):
    exit(0)

def click_code1(event=None):
    fileName = filedialog.askopenfilename()
    if fileName == "":
        fileName = None
    else:
        form1.title(fileName)
        text1.delete("1.0", "end")
        file=ConfigParser()
        inifile=ConfigParser()
        file.read(fileName, encoding="utf-8")
        inifile.read("TCD.ini", encoding="utf-8")
        try:
            text1.insert("1.0", ciph.decode(file["main"]["mess"], ciph.codeciph(int(file["main"]["openkey"]), int(inifile["main"]["keyuser"]))))
        except KeyError:
            messagebox.showerror("Ошибка генерации", "Личный ключ не был найден")

def click_save1(event=None):
    if form1.title() == "tk":
        savefile1 = filedialog.asksaveasfilename(initialfile='NoName.txtx', defaultextension=".txtx")
        cp1 = ConfigParser()
        numb = primenum(1000000)
        inifile = ConfigParser()
        inifile.read("TCD.ini", encoding="utf-8")
        cp1.add_section("main")
        try:
            cp1.set("main", "openkey", str(ciph.codeciph(numb[0]+numb[1], int(inifile["main"]["keyuser"]))))
            cp1.set("main", "mess", ciph.code(text1.get(1.0, END), numb[0]+numb[1]))
            cp1.write(open(file=savefile1, mode="w", encoding="utf-8"))
            form1.title(savefile1)
        except KeyError:
            messagebox.showerror("Ошибка генерации", "Личный ключ не был найден")
    else:
        cp1 = ConfigParser()
        inifile = ConfigParser()
        inifile.read("TCD.ini", encoding="utf-8")
        cp1.read(form1.title(), encoding="utf-8")
        try:
            cp1.set("main", "mess", ciph.code(text1.get(1.0, END), ciph.codeciph(int(cp1["main"]["openkey"]), int(inifile["main"]["keyuser"]))))
            cp1.write(open(file=form1.title(), mode="w", encoding="utf-8"))
        except KeyError:
            messagebox.showerror("Ошибка генерации", "Личный ключ не был найден")

def click_saveas1(event=None):
    savefile1 = filedialog.asksaveasfilename(initialfile='NoName.txtx', defaultextension=".txtx")
    cp1 = ConfigParser()
    numb = primenum(1000000)
    inifile = ConfigParser()
    inifile.read("TCD.ini", encoding="utf-8")
    cp1.add_section("main")
    try:
        cp1.set("main", "openkey", str(ciph.codeciph(numb[0] + numb[1], int(inifile["main"]["keyuser"]))))
        cp1.set("main", "mess", ciph.code(text1.get(1.0, END), numb[0] + numb[1]))
        cp1.write(open(file=savefile1, mode="w", encoding="utf-8"))
        form1.title(savefile1)
    except KeyError:
        messagebox.showerror("Ошибка генерации", "Личный ключ не был найден")

def click_cleane1(event=None):
   text1.delete("1.0", "end")
   form1.title("tk")

def click_copy1(event=None):
    text1.event_generate("<<Copy>>")

def click_paste1(event=None):
    text1.event_generate("<<Paste>>")

def genparam():
    numb_linkin_park = primenum(1000000)
    cp2 = ConfigParser()
    cp2.add_section("main")
    cp2.set("main", "keyuser", str(numb_linkin_park[0]))
    cp2.write(open(file="TCD.ini", mode="w", encoding="utf-8"))
    messagebox.showinfo("Параметры", "КЛЮЧ СГЕНЕРИРОВАН!")

def click_params1(event=None):
    top1 = Toplevel(form1)
    top1.geometry("250x150")
    btn1 = Button(top1, text ="Сгенерировать конфигурацию", command = genparam)
    btn1.pack()

def click_needforspeedunderground1(event=None):
    messagebox.showinfo("О программе", "Программа для прозрачного шифрования.\nШарапов К.А., 2032")

def click_forzahorizonzerodawn1(event=None):
    top1 = Toplevel(form1)
    top1.geometry("400x200")
    label = Label(top1, text="Приложение с графическим интерфейсом \n (application with a graphical interface) \n «Блокнот TCD» (файл приложения: TCD). \nОн позволяет: \n создавать / открывать / сохранять зашифрованный тестовый файл, \nдолжно быть предусмотрено ввод и сохранение личного ключа, \n вывод не модальной формы «Справка» , \nвывод модальной формы «О программе».")
    label.pack()
    def destroytop():
        top1.destroy()
        top1.update()
    btn1 = Button(top1, text ="Закрыть", command = destroytop)
    btn1.pack(side=BOTTOM)

form1 = Tk()
form1.geometry("500x500+150+150")
mainMenu1 = Menu()
form1.config(menu=mainMenu1)

menu1=Menu(mainMenu1, tearoff=False)
mainMenu1.add_cascade(menu=menu1, label="Файл")
menu1.add_cascade(label = "Новый", command=click_cleane1, accelerator="Ctrl+N")
menu1.add_cascade(label = "Открыть", command=click_code1, accelerator="Ctrl+O")
menu1.add_cascade(label = "Сохранить", command=click_save1, accelerator="Ctrl+S")
menu1.add_cascade(label = "Сохранить как...", command=click_saveas1)
menu1.add_separator()
menu1.add_cascade(label = "Выход", command=click_exit1, accelerator="Ctrl+Q")
menu2=Menu(mainMenu1, tearoff=False)
mainMenu1.add_cascade(menu=menu2, label="Правка")
menu2.add_cascade(label = "Копировать", command=click_copy1)
menu2.add_cascade(label = "Вставить", command=click_paste1)
menu2.add_separator()
menu2.add_cascade(label = "Параметры...", command=click_params1)
menu3=Menu(mainMenu1, tearoff=False)
mainMenu1.add_cascade(menu=menu3, label="Справка")
menu3.add_cascade(label = "Содержание", command=click_forzahorizonzerodawn1)
menu3.add_separator()
menu3.add_cascade(label = "О программе...", command=click_needforspeedunderground1)

text1=Text()
text1.pack(expand=True, fill=BOTH)

form1.bind("<Control-Key-n>", click_cleane1)
form1.bind("<Control-Key-o>", click_code1)
form1.bind("<Control-Key-s>", click_save1)
form1.bind("<Control-Key-q>", click_exit1)

form1.mainloop()