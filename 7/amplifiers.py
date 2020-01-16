import pprint
from IntCodeCalc import IntCodeCalc


amp_software = []
with open('input.txt') as file:
    for line in file:
        amp_software = line.strip()

highest_signal = 0
best_phases = ()

poss_phases = [5, 6, 7, 8, 9]
max_thruster = 0
max_seq = ()

for a in poss_phases:
    remaining_phases_b = poss_phases[:]
    remaining_phases_b.remove(a)
    for b in remaining_phases_b:
        remaining_phases_c = remaining_phases_b[:]
        remaining_phases_c.remove(b)
        for c in remaining_phases_c:
            remaining_phases_d = remaining_phases_c[:]
            remaining_phases_d.remove(c)
            for d in remaining_phases_d:
                remaining_phases_e = remaining_phases_d[:]
                remaining_phases_e.remove(d)
                for e in remaining_phases_e:
                    first_phase = True
                    a_itr, b_itr, c_itr, d_itr, e_itr = 0, 0, 0, 0, 0
                    a_calc = IntCodeCalc(amp_software[:], [a, 0])
                    b_calc = IntCodeCalc(amp_software[:], [b])
                    c_calc = IntCodeCalc(amp_software[:], [c])
                    d_calc = IntCodeCalc(amp_software[:], [d])
                    e_calc = IntCodeCalc(amp_software[:], [e])

                    while not e_calc.terminated:
                        if first_phase:
                            first_phase = False
                        else:
                            a_calc.inp.append(e_calc.output_val)
                        a_calc.itr = a_itr if a_itr else 0
                        a_calc.paused = False
                        a_calc.execute()
                        a_itr = a_calc.itr
                        b_calc.inp.append(a_calc.output_val)
                        b_calc.itr = b_itr if b_itr else 0
                        b_calc.paused = False
                        b_calc.execute()
                        b_itr = b_calc.itr
                        c_calc.inp.append(b_calc.output_val)
                        c_calc.itr = c_itr if c_itr else 0
                        c_calc.paused = False
                        c_calc.execute()
                        c_itr = c_calc.itr
                        d_calc.inp.append(c_calc.output_val)
                        d_calc.itr = d_itr if d_itr else 0
                        d_calc.paused = False
                        d_calc.execute()
                        d_itr = d_calc.itr
                        e_calc.inp.append(d_calc.output_val)
                        e_calc.itr = e_itr if e_itr else 0
                        e_calc.paused = False
                        e_calc.execute()
                        e_itr = e_calc.itr
                    if e_calc.output_val > max_thruster:
                        max_thruster = e_calc.output_val
                        max_seq = (a, b, c, d, e)

print(max_thruster)
print(max_seq)
