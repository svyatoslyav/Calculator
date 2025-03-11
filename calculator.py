from tkinter import *
import random
import keyboard

def set_theme(theme):
    global button
    window.config(bg=theme)
    if theme == "white":
        display.config(bg='lightgray', fg='black')
        for button in buttons:
            button.config(bg="lightgray",fg="black")
    elif theme == "black":
        display.config(bg='gray', fg='white')
        for button in buttons:
            button.config(bg="gray",fg="white")
    elif theme == "steelblue2":
        display.config(bg='steelblue1', fg='black')
        for button in buttons:
            button.config(bg="steelblue1",fg="black")
    elif theme == "blue4":
        display.config(bg='blue3', fg='white')
        for button in buttons:
            button.config(bg="blue3",fg="white")
    elif theme == "springgreen1":
        display.config(bg='springgreen2', fg='white')
        for button in buttons:
            button.config(bg="springgreen2", fg="white")
    elif theme == "darkgreen":
        display.config(bg='green', fg='white')
        for button in buttons:
            button.config(bg="green", fg="white")
    elif theme == "lightpink":
        display.config(bg='pink', fg='black')
        for button in buttons:
            button.config(bg="pink", fg="black")
    elif theme == "gold2":
        display.config(bg='gold3', fg='black')
        for button in buttons:
            button.config(bg="gold3", fg="black")
    elif theme == "mediumorchid2":
        display.config(bg='mediumorchid3', fg='white')
        for button in buttons:
            button.config(bg="mediumorchid3", fg="white")

def on_button_click(button):
    if button == "=":
        try:
            res=eval(display.get())
            try:
                res = int(res)
            except TypeError:
                1
        except ZeroDivisionError:
            display.insert(END, "Error")
        except Exception as e:
            print(e)
            pass
        else:
            if display.get()[-1]!="=":
                display.insert(END, "=")
            display.insert(END, res)
    elif button == "C":
        display.delete(0, END)
    else:
        display.insert(END, button)

window = Tk()
window.title("Калькулятор")
window.geometry("385x360")
display = Entry(window, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = []
button_texts = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+', '(', ')']
row_val = 1
col_val = 0

for text in button_texts:
    button = Button(window, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

colorlist = ["white","black","steelblue2","navy","springgreen1","darkgreen","lightpink","mediumorchid2","gold2"]
menubar = Menu(window)
theme_menu = Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("white"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("black"))
theme_menu.add_command(label="Блакитна", command=lambda: set_theme("steelblue2"))
theme_menu.add_command(label="Темно-синя", command=lambda: set_theme("blue4"))
theme_menu.add_command(label="Світло-зелена", command=lambda: set_theme("springgreen1"))
theme_menu.add_command(label="Темно-зелена", command=lambda: set_theme("darkgreen"))
theme_menu.add_command(label="Рожева", command=lambda: set_theme("lightpink"))
theme_menu.add_command(label="Фіолетова", command=lambda: set_theme("mediumorchid2"))
theme_menu.add_command(label="Золота", command=lambda: set_theme("gold2"))
theme_menu.add_command(label="Випадкова", command=lambda: set_theme(random.choice(colorlist)))
menubar.add_cascade(label="Налаштування", menu=theme_menu)
window.config(menu=menubar)

keyboard.add_hotkey("=",lambda: on_button_click("="))
keyboard.add_hotkey("c",lambda: on_button_click("C"))

window.mainloop()
