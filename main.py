import environment as env
import operations as ops
import gui

def execute_task():
    if env.requested_coffee == []:
        return
    ops.start_new_goal()
    gui.window.after(0, execute_task)

if __name__=="__main__":
    gui.setup_gui()
    ops.translate_staff_position(env.env)
    env.requested_coffee.append([ops.end_row,ops.end_col])   
    gui.window.after(0,execute_task)
    gui.window.mainloop()