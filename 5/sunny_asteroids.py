# Part 1
# Part 2

op_arr = []
i = 0
inp = 5

with open('input_p2.txt') as file:
    for line in file:
        line = line.strip()
        op_arr = line.split(',')

# print(op_arr)

while i < len(op_arr):
    op_arr[i] = str(op_arr[i])
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
    elif int(op_arr[i]) == 3:
        op_arr[int(op_arr[i + 1])] = inp
        i += 2
    elif int(op_arr[i]) == 4:
        print(op_arr[int(op_arr[i + 1])])
        i += 2
    elif int(op_arr[i]) == 99:
        break
    elif int(op_arr[i]) == 5 or ("05" in op_arr[i]):
        while len(op_arr[i]) < 4:
            op_arr[i] = "0" + op_arr[i]
        if int(op_arr[i][1]) == 0 and not int(op_arr[int(op_arr[i + 1])]) == 0:
            if int(op_arr[i][0]) == 0:
                i = int(op_arr[int(op_arr[i + 2])])
            elif int(op_arr[i][0]) == 1:
                i = int(op_arr[i + 2])
            else:
                print("5 did not jump")
                i += 3
        elif int(op_arr[i][1]) == 1 and not int(op_arr[i + 1]) == 0:
            if int(op_arr[i][0]) == 0:
                i = int(op_arr[int(op_arr[i + 2])])
            elif int(op_arr[i][0]) == 1:
                i = int(op_arr[i + 2])
            else:
                i += 3
        else:
            i += 3
    elif int(op_arr[i]) == 6 or ("06" in op_arr[i]):
        while len(op_arr[i]) < 4:
            op_arr[i] = "0" + op_arr[i]
        if int(op_arr[i][1]) == 0 and int(op_arr[int(op_arr[i + 1])]) == 0:
            if int(op_arr[i][0]) == 0:
                i = int(op_arr[int(op_arr[i + 2])])
            elif int(op_arr[i][0]) == 1:
                i = int(op_arr[i + 2])
            else:
                i += 3
        elif int(op_arr[i][1]) == 1 and int(op_arr[i + 1]) == 0:
            if int(op_arr[i][0]) == 0:
                i = int(op_arr[int(op_arr[i + 2])])
            elif int(op_arr[i][0]) == 1:
                i = int(op_arr[i + 2])
            else:
                i += 3
        else:
            i += 3
    elif int(op_arr[i]) == 7 or ("07" in op_arr[i]):
        while len(op_arr[i]) < 4:
            op_arr[i] = "0" + op_arr[i]
        if int(op_arr[i][0]) == 0 and int(op_arr[i][1]) == 0:
            if int(op_arr[int(op_arr[i + 1])]) < int(op_arr[int(op_arr[i + 2])]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        elif int(op_arr[i][0]) == 0 and int(op_arr[i][1]) == 1:
            if int(op_arr[i + 1]) < int(op_arr[int(op_arr[i + 2])]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        elif int(op_arr[i][0]) == 1 and int(op_arr[i][1]) == 0:
            if int(op_arr[int(op_arr[i + 1])]) < int(op_arr[i + 2]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        else:
            if int(op_arr[i + 1]) < int(op_arr[i + 2]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        i += 4
    elif int(op_arr[i]) == 8 or ("08" in op_arr[i]):
        while len(op_arr[i]) < 4:
            op_arr[i] = "0" + op_arr[i]
        if int(op_arr[i][0]) == 0 and int(op_arr[i][1]) == 0:
            if int(op_arr[int(op_arr[i + 1])]) == int(op_arr[int(op_arr[i + 2])]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        elif int(op_arr[i][0]) == 0 and int(op_arr[i][1]) == 1:
            if int(op_arr[int(op_arr[i + 2])]) == int(op_arr[i + 1]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        elif int(op_arr[i][0]) == 1 and int(op_arr[i][1]) == 0:
            if int(op_arr[i + 2]) == int(op_arr[int(op_arr[i + 1])]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        else:
            if int(op_arr[i + 1]) == int(op_arr[i + 2]):
                op_arr[int(op_arr[i + 3])] = 1
            else:
                op_arr[int(op_arr[i + 3])] = 0
        i += 4
    elif len(op_arr[i]) > 1:
        op_c = op_arr[i][-2:]
        op_mode = list(reversed(op_arr[i][:-2]))
        num_inp = len(op_mode)
        if num_inp == 1 and int(op_c) in [1, 2, 5, 6, 7, 8]:
            op_mode.append(0)
            num_inp += 1
        if int(op_c) == 1:
            aggr = 0
            for pos, mode in enumerate(op_mode):
                if int(mode) == 0:
                    aggr += int(op_arr[int(op_arr[i + 1 + pos])])
                else:
                    aggr += int(op_arr[i + 1 + pos])
            op_arr[int(op_arr[i + num_inp + 1])] = aggr
            i += num_inp + 2
        elif int(op_c) == 2:
            aggr = 1
            for pos, mode in enumerate(op_mode):
                if int(mode) == 0:
                    aggr *= int(op_arr[int(op_arr[i + 1 + pos])])
                else:
                    aggr *= int(op_arr[i + 1 + pos])
            op_arr[int(op_arr[i + num_inp + 1])] = aggr
            i += num_inp + 2
        elif int(op_c) == 3:
            op_arr[int(op_arr[i + 1])] = inp
            i += 2
        elif int(op_c) == 4:
            if int(op_mode[0]) == 0:
                print(op_arr[int(op_arr[i + 1])])
            else:
                print(int(op_arr[i + 1]))
            i += 2
        elif int(op_c) == 99:
            break
        else:
            print('Error read in', i, op_arr[i])
            break
    else:
        print('Error read in', i, op_arr[i])
        break
