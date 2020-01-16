import pprint


class Moon:

    def __init__(self, name, x_pos, y_pos, z_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.x_vel, self.y_vel, self.z_vel = 0, 0, 0

    def __repr__(self):
        return self.name + ': (' + str(self.x_pos) + ',' + str(self.y_pos) + ',' + str(self.z_pos) + '), vel:(' + str(self.x_vel) + ',' + str(self.y_vel) + ',' + str(self.z_vel) + ')'

    def __str__(self):
        return self.name + ': (' + str(self.x_pos) + ',' + str(self.y_pos) + ',' + str(self.z_pos) + '), vel:(' + str(self.x_vel) + ',' + str(self.y_vel) + ',' + str(self.z_vel) + ')'

    def recalc_vel(self, other_moons):
        for o_moon in other_moons:
            if self.x_pos > o_moon.x_pos:
                self.x_vel -= 1
            elif self.x_pos < o_moon.x_pos:
                self.x_vel += 1
            if self.y_pos > o_moon.y_pos:
                self.y_vel -= 1
            elif self.y_pos < o_moon.y_pos:
                self.y_vel += 1
            if self.z_pos > o_moon.z_pos:
                self.z_vel -= 1
            elif self.z_pos < o_moon.z_pos:
                self.z_vel += 1

    def tick(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel


def calc_energy(all_moons):
    tot_energy = 0
    for moon in all_moons:
        potential_energy = abs(moon.x_pos) + abs(moon.y_pos) + abs(moon.z_pos)
        kinetic_energy = abs(moon.x_vel) + abs(moon.y_vel) + abs(moon.z_vel)
        tot_energy += (potential_energy * kinetic_energy)
        print('Moon: ' + moon.name + ' potential energy: ' + str(potential_energy) + ' kinetic energy: ' + str(kinetic_energy))
    return tot_energy


moons = ['Io', 'Europa', 'Ganymede', 'Callisto']
i = 0

with open('input.txt') as file:
    for line in file:
        x, y, z = 0, 0, 0
        line = line.strip().replace('<', '').replace('>', '').split(',')
        for pos in line:
            pos = pos.strip().split('=')
            if pos[0] == 'x':
                x = int(pos[1])
            elif pos[0] == 'y':
                y = int(pos[1])
            else:
                z = int(pos[1])
        moon_name = moons[i]
        moons[i] = Moon(moon_name, x, y, z)
        i += 1

time = 0

# Part 1

# while time < 2772:
#     for m in moons:
#         tmp_moons = moons[:]
#         tmp_moons.remove(m)
#         m.recalc_vel(tmp_moons)
#     for m in moons:
#         m.tick()
#     time += 1

x_zero_at = [0]
y_zero_at = [0]
z_zero_at = [0]

while len(x_zero_at) < 2 or len(y_zero_at) < 2 or len(z_zero_at) < 2:
    all_vel_x_zero, all_vel_y_zero, all_vel_z_zero = True, True, True
    for m in moons:
        tmp_moons = moons[:]
        tmp_moons.remove(m)
        m.recalc_vel(tmp_moons)
        if not m.x_vel == 0:
            all_vel_x_zero = False
        if not m.y_vel == 0:
            all_vel_y_zero = False
        if not m.z_vel == 0:
            all_vel_z_zero = False
    for m in moons:
        m.tick()
    time += 1
    if all_vel_x_zero and len(x_zero_at) < 2:
        x_zero_at.append(time)
        # print('Time', time)
        # pprint.pprint(moons)
    if all_vel_y_zero and len(y_zero_at) < 2:
        y_zero_at.append(time)
        # print('Time', time)
        # pprint.pprint(moons)
    if all_vel_z_zero and len(z_zero_at) < 2:
        z_zero_at.append(time)
        # print('Time', time)
        # pprint.pprint(moons)

x_jump = abs(x_zero_at[0] - x_zero_at[1])
y_jump = abs(y_zero_at[0] - y_zero_at[1])
z_jump = abs(z_zero_at[0] - z_zero_at[1])

i, lcm = 2, 1

while i < min(x_jump, y_jump, z_jump) + 1:
    if x_jump % i == 0 and y_jump % i == 0 and z_jump % i == 0:
        lcm = i
    i += 1

print(x_jump, y_jump, z_jump, lcm)
print((x_jump * y_jump * z_jump)/lcm)


