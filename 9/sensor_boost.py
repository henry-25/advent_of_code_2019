from IntCodeCalcComplete import IntCodeCalc

lineA = ''

with open('input.txt') as file:
    for line in file:
        lineA = line

# Part 1

calcA = IntCodeCalc(lineA, [1])
calcA.execute()

# Part 2

calcBoosted = IntCodeCalc(lineA, [2])
calcBoosted.execute()
