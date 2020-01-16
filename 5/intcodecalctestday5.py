from IntCodeCalcComplete import IntCodeCalc

# Part 1

op_arr = ''

with open('input.txt') as file:
    for line in file:
        op_arr = line.strip()

my_calc = IntCodeCalc(op_arr, [5])
my_calc.execute()
print(my_calc.output_val)
