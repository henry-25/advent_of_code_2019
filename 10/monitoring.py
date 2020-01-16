import pprint, math

# Part 1

input_file = 'input.txt'
num_y, num_x = 0, 0

with open(input_file) as file:
    for line in file:
        line = line.strip()
        num_y += 1
        num_x = 0
        for ch in line:
            num_x += 1

asteroid_map = [['.' for x in range(0, num_x)] for y in range(0, num_y)]
asteroids_visible = {}
asteroids_list = []
asteroids_relative = {}

num_y, num_x = 0, 0

with open(input_file) as file:
    for line in file:
        line = line.strip()
        num_x = 0
        for ch in line:
            if ch == '#':
                asteroids_visible[(num_x, num_y)] = 0
                asteroids_list.append((num_x, num_y))
            asteroid_map[num_y][num_x] = ch
            num_x += 1
        num_y += 1


def get_visible_asteroids(curr_ast, ast_list):
    tmp_ast_list = ast_list[:]
    tmp_ast_list.remove(curr_ast)
    num_visible = 0
    # Check all asteroids against the current asteroid
    for ast in tmp_ast_list:
        visible = True
        other_ast_list = tmp_ast_list[:]
        other_ast_list.remove(ast)
        if not ast[1] - curr_ast[1] == 0:
            ast_diff = (ast[0] - curr_ast[0])/(ast[1] - curr_ast[1])
        else:
            if ast[0] - curr_ast[0] > 0:
                ast_diff = 1000
            else:
                ast_diff = -1000
        # Check other asteroids to see if they are in sight line
        for ast_other in other_ast_list:
            if visible:
                if not ast[1] - ast_other[1] == 0:
                    ast_diff_comp = (ast[0] - ast_other[0]) / (ast[1] - ast_other[1])
                else:
                    if ast[0] - ast_other[0] > 0:
                        ast_diff_comp = 1000
                    else:
                        ast_diff_comp = -1000
                if ast_diff == ast_diff_comp:
                    dist_ast_org = abs(curr_ast[0] - ast[0]) + abs(curr_ast[1] - ast[1])
                    dist_ast_comp = abs(curr_ast[0] - ast_other[0]) + abs(curr_ast[1] - ast_other[1])
                    same_v_ori = ((curr_ast[1] - ast[1]) >= 0 and (curr_ast[1] - ast_other[1]) >= 0) or ((curr_ast[1] - ast[1]) <= 0 and (curr_ast[1] - ast_other[1]) <= 0)
                    same_h_ori = ((curr_ast[0] - ast[0]) >= 0 and (curr_ast[0] - ast_other[0]) >= 0) or ((curr_ast[0] - ast[0]) <= 0 and (curr_ast[0] - ast_other[0]) <= 0)
                    if dist_ast_comp < dist_ast_org and same_v_ori and same_h_ori:
                        visible = False
        if visible:
            num_visible += 1
    return num_visible


most_asteroids = 0
most_vis_spot = ()
for a in asteroids_visible.keys():
    a_vis = get_visible_asteroids(a, asteroids_list)
    asteroids_visible[a] = a_vis
    if a_vis > most_asteroids:
        most_asteroids = a_vis
        most_vis_spot = a

# Part 2


def get_asteroid_slopes(curr_ast, ast_list):
    tmp_ast_list = ast_list[:]
    tmp_ast_list.remove(curr_ast)
    for ast in tmp_ast_list:
        dir_d = ''
        y = ast[0] - curr_ast[0]
        x = ast[1] - curr_ast[1]
        if y == 0 and x > 0:
            dir_d = ('S', -10000)
        elif y == 0 and x < 0:
            dir_d = ('N', 10000)
        elif x == 0 and y > 0:
            dir_d = ('E', 20000)
        elif x == 0 and y < 0:
            dir_d = ('W', -20000)
        elif x > 0 and y > 0:
            dir_d = ('SE', abs(y)/abs(x))
        elif x > 0 > y:
            dir_d = ('SW', abs(y)/abs(x))
        elif x < 0 < y:
            dir_d = ('NE', abs(y)/abs(x))
        elif x < 0 and y < 0:
            dir_d = ('NW', abs(y)/abs(x))
        if dir_d in asteroids_relative:
            asteroids_relative[dir_d].append(ast)
        else:
            asteroids_relative[dir_d] = [ast]


# print(most_vis_spot)
target_ast = most_vis_spot
get_asteroid_slopes(target_ast, asteroids_list)


i = 1
ori = 0
two_hundreth_asteroid = ()

while i < len(asteroids_list):
    orientations = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    for o in orientations:
        curr_list = [(asteroids_relative[key], key[1]) for key in asteroids_relative if key[0] == o]
        if o in ['SE', 'NW']:
            curr_list = sorted(curr_list, key=lambda x: x[1], reverse=True)
        else:
            curr_list = sorted(curr_list, key=lambda x: x[1])
        for ast_list_slp in curr_list:
            if len(ast_list_slp[0]) > 0:
                a_list = ast_list_slp[0]
                closest_ast = (10000, ())
                for a in a_list:
                    dist = math.sqrt((target_ast[0] - a[0]) ** 2 + (target_ast[1] - a[1]) ** 2)
                    if o == 'NE' and o == 'SW':
                        if dist < closest_ast[0]:
                            closest_ast = (dist, a)
                    elif o == 'SE' and o == 'NW':
                        if closest_ast[0] > 9999:
                            closest_ast[0] = 0
                        if dist > closest_ast[0]:
                            closest_ast = (dist, a)
                    else:
                        if dist < closest_ast[0]:
                            closest_ast = (dist, a)
                print('I:', i, 'closest asteroid', closest_ast[1], 'orientation', o, 'slope', ast_list_slp[1])
                asteroids_relative[(o, ast_list_slp[1])].remove(closest_ast[1])
                i += 1

# print(two_hundreth_asteroid[0] * 100 + two_hundreth_asteroid[1])



