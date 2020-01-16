from IntCodeCalcComplete import IntCodeCalc

# Part 1

with open('input.txt') as file:
    for line in file:
        line_inp = line

calc_read = IntCodeCalc(line_inp, [])
calc_read.execute()
