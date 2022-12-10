import environment
import robot
import random
import time
import gui
start_row = 12
start_col = 4
expected_coffee_cups = 5
cafe_robot = robot.robot(start_row,start_col,expected_coffee_cups)
visited = []

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
     cafe_robot.update_pos(start_row,start_col)

def check_door_status(row,col):
	if environment.door_stat[row][col] == False and 'DW' in environment.env[row][col]:
		return 'closed'
	else: 
		return 'open'

def check_pre_condition(row,col):
    if (cafe_robot.robot_position_row == row - 1 or cafe_robot.robot_position_row == row + 1) and (cafe_robot.robot_position_col == col) or (cafe_robot.robot_position_col == col + 1 or col - 1) and (cafe_robot.robot_position_row == row):
        return True
    else:
        return False

def add_pos(row,col):
    cafe_robot.update_pos(row,col)
    environment.env[row][col] = 'CR'

def delete_pos(row,col):
    if environment.mapped_name[row][col] == 'CR':
        environment.env[row][col] = '0'
    else:
        environment.env[row][col] = environment.mapped_name[row][col]

def give_coffee():
    if expected_coffee_cups >= 1:
        cafe_robot.update_coffee_cups()
        expected_coffee_cups = expected_coffee_cups - 1
        environment.requested_coffee.pop(0)
    else:
        restart_state()
    if expected_coffee_cups == 0 and environment.requested_coffee == []:
        environment.success_state = True

def open_door(row,col):
    if check_pre_condition(row,col) == True and check_door_status(row,col) == 'open':
            environment.door_stat[row][col] = True
            print("Door at ",row, " ", col, " is now opened")
            if random.randrange(1, 10) == 3:
                cafe_robot.update_coffee_cups()          #coffee cup spilled

# def enter_doorway(row,col):
# 	if entered_room == False:                 #robot is in corridor
# 		move_to(row,col)
# 		entered_room = True

# def exit_doorway(row,col):
# 	if entered_room == True:                 #robot is in room
# 		move_to(row,col)
# 		entered_room = False

def check_failure(): #this function will be called after every door opening move
    if (expected_coffee_cups != cafe_robot.coffee_cups):
        return True
    else:
        return False

def move_to(row,col):
    if check_failure() == True:
        restart_state()
        return
    if check_pre_condition(row,col) == True and environment.env[row][col] != '-1':
        if 'DW' in environment.env[row][col] and check_door_status(row,col)  == 'closed':
            open_door(row,col)
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)
            add_pos(row,col)
            environment.path.append([row,col])
        else:
            delete_pos(cafe_robot.robot_position_row,cafe_robot.robot_position_col)	
            add_pos(row,col)
            environment.path.append([row,col])
        print("Moved to pos", row," ", col)
    else:
        print('invalid location')
            

def mark_visited(node, v):
    v.append(node)

#0 0 0
#0 0 0
#0 0 0
def get_neighbors(node):
    neighbours = []
    node_row = node[0]
    node_col = node[1]
    neighbours.append(environment.env[node_row - 1][node_col]) #top
    neighbours.append(environment.env[node_row][node_col + 1]) #right
    neighbours.append(environment.env[node_row + 1][node_col]) #bottom
    neighbours.append(environment.env[node_row][node_col - 1]) #left
    for node in neighbours:
        if environment.env[node[0],node[1]] == '-1':
            neighbours.remove(node)
    return neighbours

def is_visited(node,v):
    if node in v:
        return True
    else:
        return False

def bfs(s, e):
    queue = [(s, [])]  # Start Point, Empty Path

    while len(queue) > 0:
        node, bfs_path = queue.pop(0)
        bfs_path.append(node)
        mark_visited(node, visited)

        if node == e:
            return bfs_path #Get Path

        adj_nodes = get_neighbors(node)
        for item in adj_nodes:
            if not is_visited(item, visited):
                queue.append((item, bfs_path[:]))

    return None  #Invalid Path

# Start Stop Method

def get_next_goal(): #Stop
        if environment.requested_coffee == []: #End (Success State)
            return 'SS'
        else:
            return environment.requested_coffee[0] #Current Goal

def start_new_goal(): #Start
    current_goal = get_next_goal()
    if current_goal == 'SS' or environment.success_state:
        return
    else:
        bfs_path = bfs([cafe_robot.robot_position_row,cafe_robot.robot_position_col],current_goal) #Shortest Path to Goal
        for step in bfs_path:
            gui.update_gui()
            if step == current_goal:
                give_coffee() #Goal Reached
                break
            else:
                move_to(step[0],step[[1]])
        start_new_goal() #Recursive Function Call to Get Next Goal
