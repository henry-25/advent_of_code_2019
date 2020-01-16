class IntCodeCalc:

    def __init__(self, op_data, inp):
        self.op_arr = op_data.split(',')
        self.inp = inp
        self.itr = 0
        self.output_val = 0
        self.terminated = False
        self.paused = False

    def evaluate_one(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_c = self.op_arr[i][-2:]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        num_inp = len(op_c)
        aggr = 0
        for pos, mode in enumerate(op_modes):
            if int(mode) == 0:
                aggr += int(self.op_arr[int(self.op_arr[i + 1 + pos])])
            else:
                aggr += int(self.op_arr[i + 1 + pos])
        self.op_arr[int(self.op_arr[i + num_inp + 1])] = aggr
        self.itr += num_inp + 2

    def evaluate_two(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_c = self.op_arr[i][-2:]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        num_inp = len(op_c)
        aggr = 1
        for pos, mode in enumerate(op_modes):
            if int(mode) == 0:
                aggr *= int(self.op_arr[int(self.op_arr[i + 1 + pos])])
            else:
                aggr *= int(self.op_arr[i + 1 + pos])
        self.op_arr[int(self.op_arr[i + num_inp + 1])] = aggr
        self.itr += num_inp + 2

    def evaluate_three(self):
        i = self.itr
        if len(self.inp) > 0:
            self.op_arr[int(self.op_arr[i + 1])] = self.inp[0]
            del self.inp[0]
            self.itr += 2
        else:
            self.paused = True

    def evaluate_four(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        if int(op_modes[0]) == 0:
            self.output_val = self.op_arr[int(self.op_arr[i + 1])]
        else:
            self.output_val = int(self.op_arr[i + 1])
        self.itr += 2

    def evaluate_five(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        if int(self.op_arr[i][1]) == 0 and not int(self.op_arr[int(self.op_arr[i + 1])]) == 0:
            if int(self.op_arr[i][0]) == 0:
                i = int(self.op_arr[int(self.op_arr[i + 2])])
            elif int(self.op_arr[i][0]) == 1:
                i = int(self.op_arr[i + 2])
            else:
                print("5 did not jump")
                i += 3
        elif int(self.op_arr[i][1]) == 1 and not int(self.op_arr[i + 1]) == 0:
            if int(self.op_arr[i][0]) == 0:
                i = int(self.op_arr[int(self.op_arr[i + 2])])
            elif int(self.op_arr[i][0]) == 1:
                i = int(self.op_arr[i + 2])
            else:
                i += 3
        else:
            i += 3
        self.itr = i

    def evaluate_six(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        if int(self.op_arr[i][1]) == 0 and int(self.op_arr[int(self.op_arr[i + 1])]) == 0:
            if int(self.op_arr[i][0]) == 0:
                i = int(self.op_arr[int(self.op_arr[i + 2])])
            elif int(self.op_arr[i][0]) == 1:
                i = int(self.op_arr[i + 2])
            else:
                i += 3
        elif int(self.op_arr[i][1]) == 1 and int(self.op_arr[i + 1]) == 0:
            if int(self.op_arr[i][0]) == 0:
                i = int(self.op_arr[int(self.op_arr[i + 2])])
            elif int(self.op_arr[i][0]) == 1:
                i = int(self.op_arr[i + 2])
            else:
                i += 3
        else:
            i += 3
        self.itr = i

    def evaluate_seven(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        if int(self.op_arr[i][0]) == 0 and int(self.op_arr[i][1]) == 0:
            if int(self.op_arr[int(self.op_arr[i + 1])]) < int(self.op_arr[int(self.op_arr[i + 2])]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        elif int(self.op_arr[i][0]) == 0 and int(self.op_arr[i][1]) == 1:
            if int(self.op_arr[i + 1]) < int(self.op_arr[int(self.op_arr[i + 2])]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        elif int(self.op_arr[i][0]) == 1 and int(self.op_arr[i][1]) == 0:
            if int(self.op_arr[int(self.op_arr[i + 1])]) < int(self.op_arr[i + 2]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        else:
            if int(self.op_arr[i + 1]) < int(self.op_arr[i + 2]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        self.itr += 4

    def evaluate_eight(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        if int(self.op_arr[i][0]) == 0 and int(self.op_arr[i][1]) == 0:
            if int(self.op_arr[int(self.op_arr[i + 1])]) == int(self.op_arr[int(self.op_arr[i + 2])]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        elif int(self.op_arr[i][0]) == 0 and int(self.op_arr[i][1]) == 1:
            if int(self.op_arr[int(self.op_arr[i + 2])]) == int(self.op_arr[i + 1]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        elif int(self.op_arr[i][0]) == 1 and int(self.op_arr[i][1]) == 0:
            if int(self.op_arr[i + 2]) == int(self.op_arr[int(self.op_arr[i + 1])]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        else:
            if int(self.op_arr[i + 1]) == int(self.op_arr[i + 2]):
                self.op_arr[int(self.op_arr[i + 3])] = 1
            else:
                self.op_arr[int(self.op_arr[i + 3])] = 0
        self.itr += 4

    def evaluate_instr(self):
        op = self.op_arr[self.itr]
        if op == 1 or int(op) % 100 == 1:
            self.evaluate_one()
        elif op == 2 or int(op) % 100 == 2:
            self.evaluate_two()
        elif op == 3 or int(op) % 100 == 3:
            self.evaluate_three()
        elif op == 4 or int(op) % 100 == 4:
            self.evaluate_four()
            return -1
        elif op == 5 or int(op) % 100 == 5:
            self.evaluate_five()
        elif op == 6 or int(op) % 100 == 6:
            self.evaluate_six()
        elif op == 7 or int(op) % 100 == 7:
            self.evaluate_seven()
        elif op == 8 or int(op) % 100 == 8:
            self.evaluate_eight()
        elif op == 99 or int(op) % 100 == 99:
            self.terminated = True
            return -1
        else:
            print('Error read in', self.itr, op)

    def execute(self):
        while self.itr < len(self.op_arr):
            # print(self.op_arr[self.itr])
            self.op_arr[self.itr] = str(self.op_arr[self.itr])
            self.evaluate_instr()
            if self.terminated or self.paused:
                break
