from IntCodeCalcComplete import IntCodeCalc
import pprint


class Robot:

    def __init__(self, x_loc, y_loc):
        self.curr_direction = 'North'
        self.x_loc = x_loc
        self.y_loc = y_loc

    def turn(self, turn_input):
        if turn_input == 0:
            if self.curr_direction == 'North':
                self.curr_direction = 'West'
            elif self.curr_direction == 'West':
                self.curr_direction = 'South'
            elif self.curr_direction == 'South':
                self.curr_direction = 'East'
            elif self.curr_direction == 'East':
                self.curr_direction = 'North'
        else:
            if self.curr_direction == 'North':
                self.curr_direction = 'East'
            elif self.curr_direction == 'East':
                self.curr_direction = 'South'
            elif self.curr_direction == 'South':
                self.curr_direction = 'West'
            elif self.curr_direction == 'West':
                self.curr_direction = 'North'

    def step_forward(self):
        if self.curr_direction == 'North':
            self.y_loc -= 1
        elif self.curr_direction == 'East':
            self.x_loc += 1
        elif self.curr_direction == 'South':
            self.y_loc += 1
        elif self.curr_direction == 'West':
            self.x_loc -= 1


# Part 1

loc_dict = {}

with open('input.txt') as file:
    for line in file:
        line_input = line

p1_calc = IntCodeCalc(line_input, [])
p1_calc_itr = 0
p1_robot = Robot(0, 0)
first = True

while not p1_calc.terminated:
    curr_loc = (p1_robot.x_loc, p1_robot.y_loc)
    if curr_loc in loc_dict and loc_dict[curr_loc] == 1:
        p1_calc.inp.append(1)
    else:
        p1_calc.inp.append(0)
    # if first:
    #     p1_calc.inp = [1]
    #     first = False
    p1_calc.itr = p1_calc_itr
    p1_calc.paused = False
    p1_calc.execute()
    p1_calc_itr = p1_calc.itr
    loc_dict[(p1_robot.x_loc, p1_robot.y_loc)] = p1_calc.collecting_outputs[0]
    p1_robot.turn(p1_calc.collecting_outputs[1])
    p1_robot.step_forward()
    p1_calc.collecting_outputs = []

min_val = 999
max_val = -999
for k in loc_dict.keys():
    if k[0] < min_val:
        min_val = k[0]
    if k[1] < min_val:
        min_val = k[1]
    if k[0] > max_val:
        max_val = k[0]
    if k[1] > max_val:
        max_val = k[1]

print(len(loc_dict))

# hull_grid = [['.' for x in range(0, 90)] for y in range(0, 90)]
# for k in loc_dict.keys():
#     if loc_dict[k] == 1:
#         hull_grid[k[0] + abs(min_val) + 1][k[1] + abs(min_val) + 1] = '#'
# print(min_val)
# print(max_val)
# print(max_val - min_val)
# print('\n'.join([str(hull_row) for hull_row in hull_grid]))
