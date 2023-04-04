from operations import *
from gui import *

def execute_task():
    if env_lib.requested_coffee == []:
        return
    start_new_goal()
    window.after(0, execute_task)

if __name__=="__main__":
    setup_gui()
    translate_staff_position(env_lib.env)
    env_lib.requested_coffee.append([end_row,end_col])
    window.after(0,execute_task)
    window.mainloop()