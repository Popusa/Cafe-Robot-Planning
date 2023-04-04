import environment as env_lib
import robot
import random
import gui
fail_state_mode = False
start_row = 12
start_col = 4
end_row = 12
end_col = 4
expected_coffee_cups = 21
cafe_robot = robot.robot(start_row,start_col,expected_coffee_cups)

def find_location_in_env(env,item):
    for i in range(len(env)):
        for j in range(len(env)):
            if env[i][j] == item:
                return [i,j] #found

def translate_staff_position(env):
    listloop = 0
<<<<<<< HEAD
    while(len(env_lib.requested_coffee) != len(env_lib.requested_staff)):
        env_lib.requested_coffee.append(find_location_in_env(env,env_lib.requested_staff[listloop]))
=======
    while(len(environment.requested_coffee) != len(environment.requested_staff)):
        environment.requested_coffee.append(find_location_in_env(env,environment.requested_staff[listloop])) #translate from mapped name to location
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
        listloop += 1
    
def restart_state():
    print("I dropped a cup! I must go back and replace it!")
<<<<<<< HEAD
    env_lib.requested_coffee = [[end_row,end_col]]

def check_door_status(row,col):
	if env_lib.door_stat[row][col] == 'CDW' and 'DW' in env_lib.env[row][col]:
		return 'CDW'
=======
    environment.requested_coffee = [[end_row,end_col]] #robot will begin moving back to restart

def check_door_status(row,col):
	if environment.door_stat[row][col] == 'CDW' and 'DW' in environment.env[row][col]:
		return 'CDW' #closed door
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
	else: 
		return 'ODW' #open door

def check_pre_condition(row,col):
    if (cafe_robot.robot_position_row == row - 1 or cafe_robot.robot_position_row == row + 1) and (cafe_robot.robot_position_col == col) or (cafe_robot.robot_position_col == col + 1 or col - 1) and (cafe_robot.robot_position_row == row):
        return True #robot can move there
    else:
        return False #robot cannot move there

def add_pos(row,col):
    cafe_robot.update_pos(row,col)
<<<<<<< HEAD
    env_lib.env[row][col] = 'CR'
=======
    environment.env[row][col] = 'CR' #robot location is now mapped here
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd

def delete_pos(row,col):
    if env_lib.mapped_names[row][col] == 'CR':
        env_lib.env[row][col] = '0'
    else:
<<<<<<< HEAD
        env_lib.env[row][col] = env_lib.mapped_names[row][col]
=======
        environment.env[row][col] = environment.mapped_names[row][col] #mapped location where the robot once was
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd

def update_expected_cups():
    global expected_coffee_cups
    expected_coffee_cups = expected_coffee_cups - 1 #expected cups updated

def give_coffee():
    cafe_robot.update_coffee_cups() #one satisfied customer
    update_expected_cups()
    print("Another Satisfied Customer!")

def open_door(row,col):
    if check_door_status(row,col) == 'CDW':
<<<<<<< HEAD
            env_lib.door_stat[row][col] = 'ODW'
            print("Door at Doorway",env_lib.mapped_names[row][col][2:], "is now opened")
=======
            environment.door_stat[row][col] = 'ODW' #door is now opened
            print("Door at Doorway",environment.mapped_names[row][col][2:], "is now opened")
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
            if fail_state_mode:
                if random.randrange(1,10) == 5: #random chance to fail
                    cafe_robot.update_coffee_cups()          #coffee cup spilled

def enter_doorway(row,col):
	if entered_room == False:                 #robot is in corridor
		move_to(row,col)
		entered_room = True

def exit_doorway(row,col):
	if entered_room == True:                 #robot is in room
		move_to(row,col)
		entered_room = False

def check_failure(): #this function will be called after every door opening move
    if (expected_coffee_cups != cafe_robot.coffee_cups):
        return True
    else:
        return False

def move_to(row,col):
<<<<<<< HEAD
    if check_failure() == True:
        env_lib.failed_state = True
    if check_pre_condition(row,col) == True and env_lib.env[row][col] != '-1':
        if 'DW' in env_lib.env[row][col] and check_door_status(row,col)  == 'CDW':
            open_door(row,col)
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)
            add_pos(row,col)
            env_lib.path.append([row,col])
        else:
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)	
            add_pos(row,col)
            env_lib.path.append([row,col])
        print("robot is in position: ", cafe_robot.robot_position_row,cafe_robot.robot_position_col)
=======
    if check_failure() == True: #if a fail state is reached, the process will be restarted
        environment.failed_state = True
    if check_pre_condition(row,col) == True and environment.env[row][col] != '-1':
        if 'DW' in environment.env[row][col] and check_door_status(row,col)  == 'CDW':
            open_door(row,col)
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)
            add_pos(row,col)
            environment.path.append([row,col]) #keep track of where the robot is going
        else:
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)	
            add_pos(row,col)
            environment.path.append([row,col])
        print("robot is in position: ", cafe_robot.robot_position_row,cafe_robot.robot_position_col) #for testing purposes
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
            

def mark_visited(node, v):
    v.append(node) #keeping track of shortest path for bfs

#0 0 0
#0 0 0
#0 0 0

def check_node_validity(node):
    node_row = node[0]
    node_col = node[1]
    location_name = env_lib.env[node_row][node_col][:2]
    if env_lib.env[node_row][node_col] == '-1' or env_lib.env[node_row][node_col] == 'CM': #Invalid
            return False
<<<<<<< HEAD
    # elif location_name == 'TA':
    #     return False
    elif node_row < 0 or node_row > len(env_lib.env) - 1 or node_col < 0 or node_col > len(env_lib.env) - 1: #Invalid
=======
    elif node_row < 0 or node_row > len(environment.env) - 1 or node_col < 0 or node_col > len(environment.env) - 1: #Invalid
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
        return False
    else:
        return True #Valid

def get_neighbors(node):
    neighbours = []
    node_row = node[0]
    node_col = node[1]
    neighbours.append([node_row - 1,node_col]) #top
    neighbours.append([node_row,node_col + 1]) #right
    neighbours.append([node_row + 1,node_col]) #bottom
    neighbours.append([node_row,node_col - 1]) #left

    for node in neighbours: #First Layer of Error Catching
        node_row = node[0]
        node_col = node[1]
        if (check_node_validity([node_row,node_col])): #Kept for validity
            pass
        else:
            neighbours.remove(node) #Removed for invalidity
    return neighbours

def is_visited(node,v): #very self-explanatory
    if node in v:
        return True
    else:
        return False

def bfs(s, e):
    queue = [(s, [])]  # Start Point, Empty Path
    visited = []
    while len(queue) > 0:
        node, bfs_path = queue.pop(0)
        bfs_path.append(node)
        mark_visited(node, visited)

        if node == e:
            return bfs_path #Get Path

        adj_nodes = get_neighbors(node)
        for node in adj_nodes: #Second Layer of Error Catching
            if check_node_validity(node) == False:
                adj_nodes.remove(node) #Remove Invalid Nodes
        for item in adj_nodes:
            if not is_visited(item, visited):
                queue.append((item, bfs_path[:])) #queue only keeps shortest path in list, while visiting all nodes

# Start-Stop Method

def get_next_goal(): #Stop
        if env_lib.requested_coffee == []: #End (Success State)
            return 'SS'
        else:
            return env_lib.requested_coffee[0] #Current Goal

def start_new_goal(): #Start
    while env_lib.requested_coffee:
        current_goal = get_next_goal()
        if current_goal == 'SS': #Success!
            return
        print(current_goal) #For Testing Purposes
        bfs_path = bfs([cafe_robot.robot_position_row,cafe_robot.robot_position_col],current_goal) #Shortest Path to Goal
        print(bfs_path) #For Testing Purposes
        for step in bfs_path:
<<<<<<< HEAD
            if env_lib.failed_state and not env_lib.restarted_state:
                env_lib.restarted_state = True
                restart_state()
                break
            if step == current_goal:
                if env_lib.failed_state:
                    env_lib.requested_coffee.pop(0)
                    break
                else:
                    env_lib.requested_coffee.pop(0)
                    move_to(step[0],step[1])
                    gui.update_color()
                    gui.update_gui() #Refresh GUI
                    if current_goal == [end_row,end_col]:
=======
            if environment.failed_state and not environment.restarted_state:
                environment.restarted_state = True
                restart_state() #If fail state is reached, process will restart
                break
            if step == current_goal:
                if environment.failed_state:
                    environment.requested_coffee.pop(0) #Reached Starting Position After Failure, Process Can Now Be Restarted
                    break
                else:
                    environment.requested_coffee.pop(0) #Reached Goal Position
                    move_to(step[0],step[1]) #Move Closer to Hand Staff Their Coffee
                    gui.update_color() #Refresh Color of GUI
                    gui.update_gui() #Refresh GUI Positions and Re-check for Any Changed Colors
                    if current_goal == [end_row,end_col]: #Reached End State At The End of The Process
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
                        pass
                    else:
                        give_coffee() #Goal Reached
                    break
            else:
                move_to(step[0],step[1]) #Move to Next Position In BFS Path
                gui.update_color()
<<<<<<< HEAD
                gui.update_gui() #Refresh GUI
    if (env_lib.failed_state):
        print("Fail!")
    else:    
        print("Success!")
    env_lib.staff_visited_checker = env_lib.path
    gui.draw_visited_path()
    if env_lib.failed_state:
        gui.highlight_thirsty_staff()
=======
                gui.update_gui()
    if (environment.failed_state):
        print("Fail!")
    else:    
        print("Success!")
    gui.draw_visited_path() #Draw Path on GUI
    if environment.failed_state:
        gui.highlight_thirsty_staff() #Mark Staff That Did Not Recieve Coffee Due to Failed State
>>>>>>> 153c989d078a7e5dd13be61ee3127a587bfda9fd
