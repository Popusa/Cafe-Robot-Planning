import environment
import robot
import random
import gui
fail_state_mode = False
start_row = 12
start_col = 4
end_row = 12
end_col = 4
expected_coffee_cups = 5
cafe_robot = robot.robot(start_row,start_col,expected_coffee_cups)

def find_location_in_env(env,item):
    for i in range(len(env)):
        for j in range(len(env)):
            if env[i][j] == item:
                return [i,j]

def translate_staff_position(env):
    listloop = 0
    while(len(environment.requested_coffee) != len(environment.requested_staff)):
        environment.requested_coffee.append(find_location_in_env(env,environment.requested_staff[listloop]))
        listloop += 1
    
def restart_state():
    print("I dropped a cup! I must go back and replace it!")
    environment.requested_coffee = [[end_row,end_col]]

def check_door_status(row,col):
	if environment.door_stat[row][col] == 'CDW' and 'DW' in environment.env[row][col]:
		return 'CDW'
	else: 
		return 'ODW'

def check_pre_condition(row,col):
    if (cafe_robot.robot_position_row == row - 1 or cafe_robot.robot_position_row == row + 1) and (cafe_robot.robot_position_col == col) or (cafe_robot.robot_position_col == col + 1 or col - 1) and (cafe_robot.robot_position_row == row):
        return True
    else:
        return False

def add_pos(row,col):
    cafe_robot.update_pos(row,col)
    environment.env[row][col] = 'CR'

def delete_pos(row,col):
    if environment.mapped_names[row][col] == 'CR':
        environment.env[row][col] = '0'
    else:
        environment.env[row][col] = environment.mapped_names[row][col]

def update_expected_cups():
    global expected_coffee_cups
    expected_coffee_cups = expected_coffee_cups - 1

def give_coffee():
    cafe_robot.update_coffee_cups()
    update_expected_cups()
    print("Another Satisfied Customer!")

def open_door(row,col):
    if check_door_status(row,col) == 'CDW':
            environment.door_stat[row][col] = 'ODW'
            print("Door at Doorway",environment.mapped_names[row][col][2:], "is now opened")
            if fail_state_mode:
                if random.randrange(1,10) == 5:
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
    if check_failure() == True:
        environment.failed_state = True
    if check_pre_condition(row,col) == True and environment.env[row][col] != '-1':
        if 'DW' in environment.env[row][col] and check_door_status(row,col)  == 'CDW':
            open_door(row,col)
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)
            add_pos(row,col)
            environment.path.append([row,col])
        else:
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)	
            add_pos(row,col)
            environment.path.append([row,col])
        print("robot is in position: ", cafe_robot.robot_position_row,cafe_robot.robot_position_col)
            

def mark_visited(node, v):
    v.append(node)

#0 0 0
#0 0 0
#0 0 0

def check_node_validity(node):
    node_row = node[0]
    node_col = node[1]
    location_name = environment.env[node_row][node_col][:2]
    if environment.env[node_row][node_col] == '-1' or environment.env[node_row][node_col] == 'CM': #Invalid
            return False
    # elif location_name == 'TA':
    #     return False
    elif node_row < 0 or node_row > len(environment.env) - 1 or node_col < 0 or node_col > len(environment.env) - 1: #Invalid
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
        if (check_node_validity([node_row,node_col])):
            pass
        else:
            neighbours.remove(node)
    return neighbours

def is_visited(node,v):
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
                adj_nodes.remove(node)
        for item in adj_nodes:
            if not is_visited(item, visited):
                queue.append((item, bfs_path[:]))

# Start Stop Method

def get_next_goal(): #Stop
        if environment.requested_coffee == []: #End (Success State)
            return 'SS'
        else:
            return environment.requested_coffee[0] #Current Goal

def start_new_goal(): #Start
    while environment.requested_coffee:
        current_goal = get_next_goal()
        if current_goal == 'SS':
            return
        print(current_goal)
        bfs_path = bfs([cafe_robot.robot_position_row,cafe_robot.robot_position_col],current_goal) #Shortest Path to Goal
        print(bfs_path)
        for step in bfs_path:
            if environment.failed_state and not environment.restarted_state:
                environment.restarted_state = True
                restart_state()
                break
            if step == current_goal:
                if environment.failed_state:
                    environment.requested_coffee.pop(0)
                    break
                else:
                    environment.requested_coffee.pop(0)
                    move_to(step[0],step[1])
                    gui.update_color()
                    gui.update_gui() #Refresh GUI
                    if current_goal == [end_row,end_col]:
                        pass
                    else:
                        give_coffee() #Goal Reached                    
                    break
            else:
                move_to(step[0],step[1])
                gui.update_color()
                gui.update_gui() #Refresh GUI
    if (environment.failed_state):
        print("Mission Failed!")
    else:    
        print("Mission Accomplished!")