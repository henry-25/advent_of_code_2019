from IntCodeCalcComplete import IntCodeCalc

# Part 1

op_arr = []
i = 0

with open('input.txt') as file:
    for line in file:
        op_arr = line.strip()

my_calc = IntCodeCalc(op_arr, [])
my_calc.op_arr[1] = 12
my_calc.op_arr[2] = 2
my_calc.execute()

print(my_calc.op_arr[0])

# Part 2

for noun in range(100):
    for verb in range(100):
        my_calc = IntCodeCalc(op_arr, [])
        my_calc.op_arr[1] = noun
        my_calc.op_arr[2] = verb
        my_calc.execute()
        if my_calc.op_arr[0] == 19690720:
            print((100 * noun) + verb)
            noun = 10000
            verb = 10000
            break
        verb += 1
    noun += 1
