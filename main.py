from operations import *
from gui import *

def execute_task():
    if env_lib.requested_coffee == []:
        return
    start_new_goal() # Begin!
    gui.window.after(0, execute_task)

if __name__=="__main__":
    gui.setup_gui()
    translate_staff_position(env_lib.env)
    env_lib.requested_coffee.append([end_row,end_col]) #Adding Start Position to The End of The List As The Ending Position For The Robot
    gui.window.after(0,execute_task)
    gui.window.mainloop()
