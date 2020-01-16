class IntCodeCalc:

    def __init__(self, op_data, inp):
        self.op_arr = op_data.split(',')
        additional_memory = [0 for i in range(len(self.op_arr) * 1000)]
        self.op_arr = self.op_arr + additional_memory
        self.inp = inp
        self.itr = 0
        self.output_val = 0
        self.collecting_outputs = []
        self.relative_base = 0
        self.terminated = False
        self.paused = False

    def evaluate_one(self):
        i = self.itr
        while len(self.op_arr[i]) < 5:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_c = self.op_arr[i][-2:]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        aggr = 0
        for pos, mode in enumerate(op_modes):
            if pos < len(op_modes) - 1:
                if int(mode) == 0:
                    aggr += int(self.op_arr[int(self.op_arr[i + 1 + pos])])
                elif int(mode) == 1:
                    aggr += int(self.op_arr[i + 1 + pos])
                elif int(mode) == 2:
                    aggr += int(self.op_arr[self.relative_base + int(self.op_arr[i + 1 + pos])])
        while len(op_modes) < 3:
            op_modes.append("0")
        if int(op_modes[2]) == 2:
            self.op_arr[int(self.op_arr[i + len(op_c) + 1]) + self.relative_base] = aggr
        else:
            self.op_arr[int(self.op_arr[i + len(op_c) + 1])] = aggr
        self.itr += len(op_c) + 2

    def evaluate_two(self):
        i = self.itr
        while len(self.op_arr[i]) < 5:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_c = self.op_arr[i][-2:]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        num_inp = len(op_c)
        aggr = 1
        for pos, mode in enumerate(op_modes):
            if pos < len(op_modes) - 1:
                if int(mode) == 0:
                    aggr *= int(self.op_arr[int(self.op_arr[i + 1 + pos])])
                elif int(mode) == 1:
                    aggr *= int(self.op_arr[i + 1 + pos])
                elif int(mode) == 2:
                    aggr *= int(self.op_arr[self.relative_base + int(self.op_arr[i + 1 + pos])])
        while len(op_modes) < 3:
            op_modes.append("0")
        if int(op_modes[2]) == 2:
            self.op_arr[int(self.op_arr[i + num_inp + 1]) + self.relative_base] = aggr
        else:
            self.op_arr[int(self.op_arr[i + num_inp + 1])] = aggr
        self.itr += num_inp + 2

    def evaluate_three(self):
        i = self.itr
        if len(self.inp) > 0:
            while len(self.op_arr[i]) < 3:
                self.op_arr[i] = "0" + self.op_arr[i]
            op_modes = list(reversed(self.op_arr[i][:-2]))
            if int(op_modes[0]) == 0:
                self.op_arr[int(self.op_arr[i + 1])] = self.inp[0]
            elif int(op_modes[0]) == 1:
                self.op_arr[i + 1] = self.inp[0]
            elif int(op_modes[0]) == 2:
                self.op_arr[int(self.op_arr[i + 1]) + self.relative_base] = self.inp[0]
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
        elif int(op_modes[0]) == 1:
            self.output_val = int(self.op_arr[i + 1])
        elif int(op_modes[0]) == 2:
            self.output_val = self.op_arr[self.relative_base + int(self.op_arr[i + 1])]
        # print(self.output_val)
        self.collecting_outputs.append(int(self.output_val))
        self.itr += 2

    def evaluate_five(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        if int(op_modes[0]) == 0:
            if not int(self.op_arr[int(self.op_arr[i + 1])]) == 0:
                if int(op_modes[1]) == 0:
                    i = int(self.op_arr[int(self.op_arr[i + 2])])
                elif int(op_modes[1]) == 1:
                    i = int(self.op_arr[i + 2])
                elif int(op_modes[1]) == 2:
                    i = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
            else:
                i += 3
        elif int(op_modes[0]) == 1:
            if not int(self.op_arr[i + 1]) == 0:
                if int(op_modes[1]) == 0:
                    i = int(self.op_arr[int(self.op_arr[i + 2])])
                elif int(op_modes[1]) == 1:
                    i = int(self.op_arr[i + 2])
                elif int(op_modes[1]) == 2:
                    i = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
            else:
                i += 3
        elif int(op_modes[0]) == 2:
            if not int(self.op_arr[self.relative_base + int(self.op_arr[i + 1])]) == 0:
                if int(op_modes[1]) == 0:
                    i = int(self.op_arr[int(self.op_arr[i + 2])])
                elif int(op_modes[1]) == 1:
                    i = int(self.op_arr[i + 2])
                elif int(op_modes[1]) == 2:
                    i = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
            else:
                i += 3
        else:
            i += 3
        self.itr = i

    def evaluate_six(self):
        i = self.itr
        while len(self.op_arr[i]) < 4:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        if int(op_modes[0]) == 0:
            if int(self.op_arr[int(self.op_arr[i + 1])]) == 0:
                if int(op_modes[1]) == 0:
                    i = int(self.op_arr[int(self.op_arr[i + 2])])
                elif int(op_modes[1]) == 1:
                    i = int(self.op_arr[i + 2])
                elif int(op_modes[1]) == 2:
                    i = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
            else:
                i += 3
        elif int(op_modes[0]) == 1:
            if int(self.op_arr[i + 1]) == 0:
                if int(op_modes[1]) == 0:
                    i = int(self.op_arr[int(self.op_arr[i + 2])])
                elif int(op_modes[1]) == 1:
                    i = int(self.op_arr[i + 2])
                elif int(op_modes[1]) == 2:
                    i = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
            else:
                i += 3
        elif int(op_modes[0]) == 2:
            if int(self.op_arr[self.relative_base + int(self.op_arr[i + 1])]) == 0:
                if int(op_modes[1]) == 0:
                    i = int(self.op_arr[int(self.op_arr[i + 2])])
                elif int(op_modes[1]) == 1:
                    i = int(self.op_arr[i + 2])
                elif int(op_modes[1]) == 2:
                    i = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
            else:
                i += 3
        else:
            i += 3
        self.itr = i

    def evaluate_seven(self):
        i = self.itr
        while len(self.op_arr[i]) < 5:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        val_a, val_b = 0, 0
        if int(op_modes[0]) == 0:
            val_a = int(self.op_arr[int(self.op_arr[i + 1])])
        elif int(op_modes[0]) == 1:
            val_a = int(self.op_arr[i + 1])
        elif int(op_modes[0]) == 2:
            val_a = int(self.op_arr[self.relative_base + int(self.op_arr[i + 1])])
        if int(op_modes[1]) == 0:
            val_b = int(self.op_arr[int(self.op_arr[i + 2])])
        elif int(op_modes[1]) == 1:
            val_b = int(self.op_arr[i + 2])
        elif int(op_modes[1]) == 2:
            val_b = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
        val_c = 1 if val_a < val_b else 0
        if int(op_modes[2]) == 0:
            self.op_arr[int(self.op_arr[i + 3])] = val_c
        elif int(op_modes[2]) == 1:
            self.op_arr[i + 3] = val_c
        elif int(op_modes[2]) == 2:
            self.op_arr[int(self.op_arr[i + 3]) + self.relative_base] = val_c
        self.itr += 4

    def evaluate_eight(self):
        i = self.itr
        while len(self.op_arr[i]) < 5:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        val_a, val_b = 0, 0
        if int(op_modes[0]) == 0:
            val_a = int(self.op_arr[int(self.op_arr[i + 1])])
        elif int(op_modes[0]) == 1:
            val_a = int(self.op_arr[i + 1])
        elif int(op_modes[0]) == 2:
            val_a = int(self.op_arr[self.relative_base + int(self.op_arr[i + 1])])
        if int(op_modes[1]) == 0:
            val_b = int(self.op_arr[int(self.op_arr[i + 2])])
        elif int(op_modes[1]) == 1:
            val_b = int(self.op_arr[i + 2])
        elif int(op_modes[1]) == 2:
            val_b = int(self.op_arr[self.relative_base + int(self.op_arr[i + 2])])
        val_c = 1 if val_a == val_b else 0
        if int(op_modes[2]) == 0:
            self.op_arr[int(self.op_arr[i + 3])] = val_c
        elif int(op_modes[2]) == 1:
            self.op_arr[i + 3] = val_c
        elif int(op_modes[2]) == 2:
            self.op_arr[int(self.op_arr[i + 3]) + self.relative_base] = val_c
        self.itr += 4

    def evaluate_nine(self):
        i = self.itr
        while len(self.op_arr[i]) < 3:
            self.op_arr[i] = "0" + self.op_arr[i]
        op_modes = list(reversed(self.op_arr[i][:-2]))
        if int(op_modes[0]) == 0:
            self.relative_base += int(self.op_arr[int(self.op_arr[i + 1])])
        elif int(op_modes[0]) == 1:
            self.relative_base += int(self.op_arr[i + 1])
        elif int(op_modes[0]) == 2:
            self.relative_base += int(self.op_arr[self.relative_base + int(self.op_arr[i + 1])])
        self.itr += 2

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
        elif op == 9 or int(op) % 100 == 9:
            self.evaluate_nine()
        elif op == 99 or int(op) % 100 == 99:
            self.terminated = True
            return -1
        else:
            print('Error read in', self.itr, op)
            self.itr = len(self.op_arr)

    def execute(self):
        while self.itr < len(self.op_arr):
            self.op_arr[self.itr] = str(self.op_arr[self.itr])
            self.evaluate_instr()
            if self.terminated or self.paused:
                break
