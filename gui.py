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
    for i in range(len(environment.env)):
        for j in range(len(environment.env)):
            if 'TA' in environment.env[i][j] or 'DR' in environment.env[i][j]:
                if [i,j] in environment.path and environment.env[i][j] in environment.requested_staff:
                    buttonslist[i][j].config(background="white")
                    buttonslist[i][j].config(text = environment.mapped_names[i][j])
                else:
                    buttonslist[i][j].config(background="orange")
                    buttonslist[i][j].config(text = environment.mapped_names[i][j])
            elif '-1' in environment.env[i][j]:
                buttonslist[i][j].config(background="black")
            elif 'DW' in environment.env[i][j]:
                if environment.door_stat[i][j] == 'CDW':
                    buttonslist[i][j].config(background="red")
                    buttonslist[i][j].config(foreground="white")
                else:                 
                    buttonslist[i][j].config(background="blue")
                    buttonslist[i][j].config(foreground="white")
                buttonslist[i][j].config(text = environment.mapped_names[i][j])
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

def update_gui():
    window.update()
    time.sleep(0.1)

def setup_gui():
    make_grid()
    update_color()

def draw_visited_path():
    listloop = 0
    while len(environment.path) != listloop:
        visited_pos = environment.path[listloop]
        buttonslist[visited_pos[0]][visited_pos[1]].config(background="yellow")
        buttonslist[visited_pos[0]][visited_pos[1]].config(foreground="blue")
        buttonslist[visited_pos[0]][visited_pos[1]]['text'] = environment.mapped_names[visited_pos[0]][visited_pos[1]]
        listloop = listloop + 1
        for pos in environment.path:
            if environment.env[pos[0]][pos[1]][:2] == 'TA' or environment.env[pos[0]][pos[1]][:2] == 'DR':
                buttonslist[pos[0]][pos[1]].config(background="white")
                buttonslist[pos[0]][pos[1]].config(text = environment.mapped_names[pos[0]][pos[1]])

def highlight_thirsty_staff():
    for i in range(len(environment.env)):
        for j in range(len(environment.env)):
            if environment.env[i][j][:2] == 'DR' or environment.env[i][j][:2] == 'TA' and \
                environment.env[i][j] in environment.requested_staff and environment.env[i][j] not in environment.path:
                buttonslist[i][j].config(background="red")
                buttonslist[i][j].config(text = environment.mapped_names[i][j])