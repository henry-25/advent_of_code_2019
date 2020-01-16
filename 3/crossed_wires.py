import pprint


def get_visited_points(directions):
    v_points = set()
    v_points_timed = set()
    curr_loc = (0, 0, 0)
    for d in directions:
        if d[0] == 'R':
            num_times = int(d[1:])
            while num_times:
                curr_loc = (curr_loc[0] + 1, curr_loc[1], curr_loc[2] + 1)
                v_points.add((curr_loc[0], curr_loc[1]))
                v_points_timed.add(curr_loc)
                num_times -= 1
        elif d[0] == 'L':
            num_times = int(d[1:])
            while num_times:
                curr_loc = (curr_loc[0] - 1, curr_loc[1], curr_loc[2] + 1)
                v_points.add((curr_loc[0], curr_loc[1]))
                v_points_timed.add(curr_loc)
                num_times -= 1
        elif d[0] == 'D':
            num_times = int(d[1:])
            while num_times:
                curr_loc = (curr_loc[0], curr_loc[1] - 1, curr_loc[2] + 1)
                v_points.add((curr_loc[0], curr_loc[1]))
                v_points_timed.add(curr_loc)
                num_times -= 1
        elif d[0] == 'U':
            num_times = int(d[1:])
            while num_times:
                curr_loc = (curr_loc[0], curr_loc[1] + 1, curr_loc[2] + 1)
                v_points.add((curr_loc[0], curr_loc[1]))
                v_points_timed.add(curr_loc)
                num_times -= 1
        else:
            print('INVALID INSTRUCTION', d)
    return v_points, v_points_timed


intersected_points = {'wire1': set(), 'wire2': set()}
intersected_points_timed = {'wire1': set(), 'wire2': set()}

with open('input.txt') as file:
    for n, line in enumerate(file):
        line = line.strip().split(',')
        if n == 0:
            intersected_points['wire1'] = get_visited_points(line)[0]
            intersected_points_timed['wire1'] = get_visited_points(line)[1]
        else:
            intersected_points['wire2'] = get_visited_points(line)[0]
            intersected_points_timed['wire2'] = get_visited_points(line)[1]

# pprint.pprint(intersected_points)

# Part 1

# both_points = intersected_points['wire1'].intersection(intersected_points['wire2'])

# shortest_path = 100000
# for point in both_points:
#     path = abs(point[0]) + abs(point[1])
#     if path < shortest_path:
#         shortest_path = path
#
# print(shortest_path)
# pprint.pprint(both_points)

# Part 2

both_points = intersected_points['wire1'].intersection(intersected_points['wire2'])


def pairs(shared_points, timed_points):
    for x1, y1 in shared_points:
        for x2, y2, t2 in timed_points:
            if x1 == x2 and y1 == y2:
                yield (x1, y1, t2)


wire1_timed = list(pairs(both_points, intersected_points_timed['wire1']))
wire2_timed = list(pairs(both_points, intersected_points_timed['wire2']))


shortest_time = 100000000

for a1, a2, a3 in wire1_timed:
    for b1, b2, b3 in wire2_timed:
        print(a1 == b1, a2 == b2, a1, b1, a2, b2)
        if a1 == b1 and a2 == b2:
            print(a3 + b3)
            if a3 + b3 < shortest_time:
                shortest_time = a3 + b3

print(shortest_time)
#
# pprint.pprint(t_list)
#
# for t in t_list:
#     print(abs(t[2]) + abs(t[3]))
