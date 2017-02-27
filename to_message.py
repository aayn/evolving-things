from random import choice, randrange
from string import printable, ascii_letters
from functools import partial

def edit_distance(s1,s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


def rand_char():
    return choice(ascii_letters)

def add_char(msg):
    add_index = randrange(len(msg))
    return msg[0:add_index] + rand_char() + msg[add_index:]

def del_char(msg):
    del_index = randrange(len(msg))
    return msg[0:del_index] + msg[del_index + 1:]

def mutate_str(msg):
    mut_index = randrange(len(msg))
    t = list(msg)
    t[mut_index] = rand_char()
    return ''.join(t)

def new_child(curr, final):
    child = None
    if len(curr) < len(final):
        c = randrange(2)
        child = add_char(curr) if c == 0 else mutate_str(curr)
    elif len(curr) > len(final):
        c = randrange(2)
        child = del_char(curr) if c == 0 else mutate_str(curr)
    else:
        child = mutate_str(curr)

    return child

def evolution():
    final = input("Enter final evolved string:\n")
    start = input("Enter start string:\n")
    noc = int(input("Number of children/gen:"))

    make_child = partial(new_child, final=final)
    dist = partial(edit_distance, s2=final)
    curr = start
    gens = 0
    while True:
        if curr == final:
            break
        child_list = []
        for i in range(noc):
            child_list.append(make_child(curr))
        distances = list(map(dist, child_list))
        best_child = (child_list[distances.index(min(distances))])
        print(best_child)
        curr = best_child
        gens += 1

    print("This took {} generations".format(gens))

evolution()
