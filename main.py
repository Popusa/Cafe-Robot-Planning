import tkinter as tk
import numpy as np
import environment as env
import robot as rbt
import operations as ops
import gui
import time

def execute_task():
    ops.start_new_goal()
    gui.window.after(0, execute_task)

if __name__=="__main__":
    gui.setup_gui()
    # ops.translate_staff_position(env.env)
    # gui.window.after(0,execute_task)
    gui.window.mainloop()