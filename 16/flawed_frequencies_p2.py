import pprint

# Part 2

input_signal = []
input_pattern = [0, 1, 0, -1]

with open('input_p2_example.txt') as file:
    for line in file:
        for ch in line:
            input_signal.append(int(ch))

message_offset = input_signal[:7]
val = int(str(message_offset[0]) + str(message_offset[1]) + str(message_offset[2]) + str(message_offset[3]) + str(message_offset[4]) + str(message_offset[5]) + str(message_offset[6]))

while len(input_signal) < val:
    input_signal += input_signal

phase = 0
input_signal_final = input_signal[:]
while phase < 1:
    for i, k in enumerate(input_signal):
        input_signal_final[i] =
    phase += 1

print(len(input_signal))
