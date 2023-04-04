from operations import *
from gui import *

def execute_task():
    if env_lib.requested_coffee == []:
        return
<<<<<<< HEAD
    start_new_goal()
    window.after(0, execute_task)

if __name__=="__main__":
    setup_gui()
    translate_staff_position(env_lib.env)
    env_lib.requested_coffee.append([end_row,end_col])
    window.after(0,execute_task)
    window.mainloop()
=======
    ops.start_new_goal() # Begin!
    gui.window.after(0, execute_task)

if __name__=="__main__":
    gui.setup_gui()
    ops.translate_staff_position(env.env)
    env.requested_coffee.append([ops.end_row,ops.end_col]) #Adding Start Position to The End of The List As The Ending Position For The Robot
    gui.window.after(0,execute_task)
    gui.window.mainloop()
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
