import pprint

# Part 1

input_signal = []
input_pattern = [0, 1, 0, -1]

with open('input.txt') as file:
    for line in file:
        for ch in line:
            input_signal.append(int(ch))


def construct_phase_shift(curr_place, i_pattern, length_signal):
    const_signal_adapter = []
    while len(const_signal_adapter) < length_signal + 1:
        for i in i_pattern:
            i_tmp = curr_place
            while i_tmp > 0:
                const_signal_adapter.append(i)
                i_tmp -= 1
    return const_signal_adapter[1:length_signal + 1]


phase_shift = [[] for i in range(len(input_signal))]
place = 1

while place < len(input_signal) + 1:
    phase_shift[place - 1] = (construct_phase_shift(place, input_pattern, len(input_signal)))
    place += 1

phase = 0
desired_phase = 100
input_signal_final = input_signal[:]

while phase < desired_phase:
    for n, plc in enumerate(input_signal_final):
        val_aggr = 0
        for i, k in enumerate(input_signal):
            val_aggr += phase_shift[n][i] * k
        input_signal_final[n] = abs(val_aggr) % 10
    input_signal = input_signal_final[:]
    phase += 1

pprint.pprint(input_signal[:8])
