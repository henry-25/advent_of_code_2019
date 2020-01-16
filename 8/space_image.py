import pprint

# Part 1

# layers = {'layer1': []}
# layers_num_zeros = {'layer1': 0}
# layers_num_ones = {'layer1': 0}
# layers_num_twos = {'layer1': 0}
# i = 1
#
# with open('input.txt') as file:
#     for line in file:
#         pixels = line
#         for ch in pixels:
#             layer = 'layer' + str(i)
#             layers[layer].append(int(ch))
#             if int(ch) == 0:
#                 layers_num_zeros[layer] += 1
#             elif int(ch) == 1:
#                 layers_num_ones[layer] += 1
#             elif int(ch) == 2:
#                 layers_num_twos[layer] += 1
#             if len(layers[layer]) == 150:
#                 i += 1
#                 layers['layer' + str(i)] = []
#                 layers_num_zeros['layer' + str(i)] = 0
#                 layers_num_ones['layer' + str(i)] = 0
#                 layers_num_twos['layer' + str(i)] = 0
#
# least_zeros = 10000
# least_zeros_layer = ''
#
# for key in layers_num_zeros:
#     if len(layers[key]) > 0 and layers_num_zeros[key] < least_zeros:
#         least_zeros = int(layers_num_zeros[key])
#         least_zeros_layer = key

# Part 2

image = [[2 for i in range(0, 25)] for j in range(0, 6)]
i = 0
y_coord = 0
x_coord = 0

with open('input.txt') as file:
    for line in file:
        for ch in line:
            i += 1
            if image[y_coord][x_coord] == 2:
                image[y_coord][x_coord] = int(ch)
            x_coord += 1
            if x_coord == 25:
                x_coord = 0
                if i % 150 == 0:
                    y_coord = 0
                else:
                    y_coord += 1

pprint.pprint(image)
