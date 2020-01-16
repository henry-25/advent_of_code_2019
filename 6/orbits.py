import pprint

# Part 1


def get_child_planets(curr_planet, planet_dict):
    if curr_planet not in planet_dict:
        s = curr_planet
        return {s}
    else:
        planets_orbiting = set()
        for p in planet_dict[curr_planet]:
            planets_orbiting.add(p)
            planets_orbiting = planets_orbiting.union(get_child_planets(p, planet_dict))
        return planets_orbiting


def get_shortest_path(curr_planet, destination, visited_planets, path, orbiting_planets, planets_orbiting):
    if curr_planet == destination:
        print(path - 2)
    if curr_planet in orbiting_planets:
        for planet in orbiting_planets[curr_planet]:
            if planet not in visited_planets:
                p = visited_planets[:]
                p.append(curr_planet)
                get_shortest_path(planet, destination, p, path + 1, orbiting_planets, planets_orbiting)
    if curr_planet in planets_orbiting:
        for planet in planets_orbiting[curr_planet]:
            if planet not in visited_planets:
                p = visited_planets[:]
                p.append(curr_planet)
                get_shortest_path(planet, destination, p, path + 1, orbiting_planets, planets_orbiting)


orbiting_around = {}
orbiting = {}
objects = set()

with open('input.txt') as file:
    for line in file:
        line = line.strip().split(')')
        if line[1] in orbiting:
            orbiting[line[1]].append(line[0])
        else:
            orbiting[line[1]] = [line[0]]
        if line[0] in orbiting_around:
            orbiting_around[line[0]].append(line[1])
        else:
            orbiting_around[line[0]] = [line[1]]
        objects.add(line[0])
        objects.add(line[1])

# num_obj = 0
#
# for pla in objects:
#     num_obj += len(get_child_planets(pla, orbiting))
#
# num_obj -= 1

# print(num_obj)

get_shortest_path('YOU', 'SAN', ['YOU'], 0, orbiting, orbiting_around)

# pprint.pprint(objects)
# pprint.pprint(orbiting)
# pprint.pprint(orbiting_around)
