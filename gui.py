import tkinter as tk
import environment
import time
window = tk.Tk()
window.title("cafe robot planning")
window.geometry("500x420")
window.resizable(False, False)
buttonslist = [[0]*len(environment.env) for i in range(len(environment.env))]

def make_grid():
    for i in range(len(environment.env)):
        for j in range(len(environment.env)):
            buttonslist[i][j] = (tk.Button(window, text = environment.env[i][j],width=3))
            buttonslist[i][j].grid(row=i,column=j)

def update_color():
    counter = 0
    for i in range(len(environment.env)):
        for j in range(len(environment.env)):
            if 'TA' in environment.env[i][j] or 'DR' in environment.env[i][j]:
                buttonslist[i][j].config(background="orange")
            elif '-1' in environment.env[i][j]:
                buttonslist[i][j].config(background="black")
            elif 'DW' in environment.env[i][j]:
                buttonslist[i][j].config(background="blue")
                buttonslist[i][j].config(foreground="white")
                buttonslist[i][j].config(text = environment.mapped_name[i][j])
            elif 'CR' in environment.env[i][j]:
                buttonslist[i][j].config(background="brown")
                buttonslist[i][j].config(text = 'CR')
            elif '0' in environment.env[i][j]:
                buttonslist[i][j].config(background="green")
                buttonslist[i][j].config(text = '0')               
            elif 'CM' in environment.env[i][j]:
                buttonslist[i][j].config(background="crimson")
            elif 'ES' in environment.env[i][j]:
                buttonslist[i][j].config(background="red")
            counter += 1

def update_gui():
    window.update()
    time.sleep(0.7)

def setup_gui():
    make_grid()
    update_color()