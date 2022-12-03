class robot:
    def __init__(self, robot_position_row, robot_position_col,coffee_cups):
        self.robot_position_row = robot_position_row
        self.robot_position_col = robot_position_col
        self.coffee_cups = coffee_cups

    def update_pos(self,row,col):
        self.robot_position_row = row
        self.robot_position_col = col

    def update_coffee_cups(self):
        self.coffee_cups = self.coffee_cups - 1