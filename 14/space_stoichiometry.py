import pprint, math

# def combine_common(element, list_of_elements):
#     for e in list_of_elements:
#         if e[]


# Part 1

stoichiometry_dict, extra_ore = {}, {}

with open('input_example.txt') as file:
    for line in file:
        line = line.strip().split('=>')
        out_ingredients = line[1].strip().split(' ')
        if out_ingredients[1] in stoichiometry_dict:
            stoichiometry_dict[out_ingredients[1]][int(out_ingredients[0])] = [(int(i.strip().split(' ')[0]), i.strip().split(' ')[1]) for i in line[0].split(',')]
        else:
            stoichiometry_dict[out_ingredients[1]] = {int(out_ingredients[0]): [(int(i.strip().split(' ')[0]), i.strip().split(' ')[1]) for i in line[0].split(',')]}
        extra_ore[out_ingredients[1]] = 0

print(extra_ore)
desired_output = [(1, 'FUEL')]
ore_used = 0
while len(desired_output) > 0:
    element_type = desired_output[0][1]
    element_quantity = desired_output[0][0]
    del desired_output[0]
    quantity_producable = next(iter(stoichiometry_dict[element_type].keys()))
    num_required = math.ceil(element_quantity / quantity_producable)
    output_info = stoichiometry_dict[element_type][quantity_producable]
    for ingredient in output_info:
        ingredient_type = ingredient[1]
        ingredient_amount = ingredient[0] * num_required
        if ingredient_type == 'ORE':
            ore_ratio = quantity_producable / ingredient[0]
            if element_quantity * ore_ratio < extra_ore[element_type]:
                extra_ore[element_type] -= element_quantity * ore_ratio
                ore_used += element_quantity * ore_ratio
                print('Using extra ore', ore_used, extra_ore)
            else:
                ore_used += element_quantity * ore_ratio
                extra_ore[element_type] += ingredient_amount - (element_quantity * ore_ratio)
                print('Using newly produced ore', ore_used, extra_ore)
        else:
            desired_output.append((ingredient_amount, ingredient_type))

for k in extra_ore.keys():
    ore_used += extra_ore[k]

print(ore_used)