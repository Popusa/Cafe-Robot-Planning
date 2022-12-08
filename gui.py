import tkinter as tk
import environment
window = tk.Tk()
window.title("cafe robot planning")
window.geometry("500x500")
window.resizable(False, False)
buttonslist = [[0]*len(environment.env) for i in range(len(environment.env))]

def make_grid():
    for i in range(len(environment.env)):
        for j in range(len(environment.env)):
            buttonslist[i][j] = (tk.Button(window, text = environment.env[i][j]))
            buttonslist[i][j].grid(row=i,column=j)
def update_color():
    counter = 0
    for i in range(len(environment.env)):
        for j in range(len(environment.env)):
            if 'TA' in buttonslist[i][j]['text'] or 'DR' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="orange")
            elif '-1' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="black")
            elif 'DW' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="blue")
                buttonslist[i][j].config(foreground="white")
            elif 'CR' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="brown")
            elif '0' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="green")
            elif 'CM' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="crimson")
            elif 'ES' in buttonslist[i][j]['text']:
                buttonslist[i][j].config(background="red")
            counter += 1

def setup_gui():
    make_grid()
    update_color()