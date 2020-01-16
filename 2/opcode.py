# Part 1

# op_arr = []
# i = 0
#
# with open('input.txt') as file:
#     for line in file:
#         op_arr = line.split(',')
#
# op_arr[1] = 12
# op_arr[2] = 2
#
# while i < len(op_arr):
#     if int(op_arr[i]) == 1:
#         n_val = int(op_arr[i + 1])
#         t_val = int(op_arr[i + 2])
#         op_arr[int(op_arr[i + 3])] = int(op_arr[n_val]) + int(op_arr[t_val])
#         i += 4
#     elif int(op_arr[i]) == 2:
#         n_val = int(op_arr[i + 1])
#         t_val = int(op_arr[i + 2])
#         op_arr[int(op_arr[i + 3])] = int(op_arr[n_val]) * int(op_arr[t_val])
#         i += 4
#     elif int(op_arr[i]) == 99:
#         print('Finished')
#         break
#     else:
#         print('Error read in', op_arr[i])
#         break
#     print(op_arr)


# Part 2

noun = 0
verb = 0

for noun in range(100):
    for verb in range(100):
        op_arr = []
        i = 0
        with open('input.txt') as file:
            for line in file:
                op_arr = line.split(',')

        op_arr[1] = int(noun)
        op_arr[2] = int(verb)

        while i < len(op_arr):
            if int(op_arr[i]) == 1:
                n_val = int(op_arr[i + 1])
                t_val = int(op_arr[i + 2])
                op_arr[int(op_arr[i + 3])] = int(op_arr[n_val]) + int(op_arr[t_val])
                i += 4
            elif int(op_arr[i]) == 2:
                n_val = int(op_arr[i + 1])
                t_val = int(op_arr[i + 2])
                op_arr[int(op_arr[i + 3])] = int(op_arr[n_val]) * int(op_arr[t_val])
                i += 4
            elif int(op_arr[i]) == 99:
                break
            else:
                print('Error read in', op_arr[i])
                break
        if op_arr[0] == 19690720:
            print((100 * noun) + verb)
            print(op_arr)
            noun = 10000
            verb = 10000
            break
        verb += 1
    noun += 1
