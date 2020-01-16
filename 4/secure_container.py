# Part 1
# Part 2


def check_pass(pswd):
    two_i_ago = -1
    last_i = 0
    curr_i = 0
    doubles = False
    doubles_num = -1
    for ch in pswd:
        curr_i = int(ch)
        if curr_i < last_i:
            return False
        if curr_i == last_i and not doubles:
            doubles_num = curr_i
            doubles = True
        if curr_i == last_i == two_i_ago and curr_i == doubles_num:
            doubles = False
        two_i_ago = last_i
        last_i = curr_i
    return doubles


num_pass = 0

for i in range(128392, 643281):
    if check_pass(str(i)):
        num_pass += 1

print(num_pass)
