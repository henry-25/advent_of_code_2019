from IntCodeCalcComplete import IntCodeCalc
from pprint import pprint

# Part 1

with open('input.txt') as file:
    for line in file:
        input_line = line

my_calc = IntCodeCalc(input_line, [])
my_calc.op_arr[0] = 2
my_calc.execute()


arcade_screen = [[0 for i in range(0, 23)] for j in range(0, max(my_calc.collecting_outputs) + 1)]
ind = 0
num_blocks = 0

# Part 2
# my_calc.collecting_outputs[0] = 2

while ind < len(my_calc.collecting_outputs):
    if my_calc.collecting_outputs[ind + 2] == 2:
        num_blocks += 1
    arcade_screen[my_calc.collecting_outputs[ind]][my_calc.collecting_outputs[ind + 1]] = my_calc.collecting_outputs[ind + 2]
    ind += 3

print('\n'.join([str(arcade_line) for arcade_line in arcade_screen]))
