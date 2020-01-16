import pprint

portal_locations = {}
open_spaces = []
wall_spaces = []

with open('input_example.txt') as file:
    for line_num, line in enumerate(file):
        for ch_num, ch in enumerate(line):
            if ch:
                if ch == '.':
                    open_spaces.append((line_num, ch_num))
                elif ch == '#':
                    wall_spaces.append((line_num, ch_num))
                elif ch.isalpha():
                    if ch in portal_locations:
                        portal_locations[ch].append((line_num, ch_num))
                    else:
                        portal_locations[ch] = [(line_num, ch_num)]

for k in portal_locations.keys():
    print(k, portal_locations[k])

# print(portal_locations)
# print(open_spaces)
# print(wall_spaces)
