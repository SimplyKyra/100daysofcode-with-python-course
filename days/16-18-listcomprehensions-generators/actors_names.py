import random

def gen_pairs(the_names, number  = 10):
    for i in range(0, number):
        name1 = random.choice(the_names).split()[0]
        name2 = random.choice(the_names).split()[0]
        while name2 == name1:
            name2 = random.choice(the_names).split()[0]
        yield f"{name1} teams up with {name2}"

def gen_pairs_theirs():
    first_name2 = [name.split()[0].title() for name in NAMES]
    while True:
        first, second = None, None
        while first == second:
            first, second = random.sample(first_name2, 2)

            yield f'{first} teams up with {second}'



NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos', \
         'julian sequeira', 'sandra bullock', 'keanu reeves', \
         'julbob pybites', 'bob belderbos', 'julian sequeira', \
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

print(NAMES)

capital_names = [name.title() for name in NAMES]

print(capital_names)

swapped_names = [temp.split()[1] + " " + temp.split()[0] for temp in NAMES]

print(swapped_names)

def reverse_first_last_names(name):
    first, last = name.split()
    return f'{last} {first}'


swapped_names2 = [reverse_first_last_names(name) for name in NAMES]

print(swapped_names2)

pairs = gen_pairs(capital_names)
for _ in range(10):
    print(next(pairs))


pairs2 = gen_pairs_theirs()
for _ in range(10):
    print(next(pairs2))

import itertools

itertools.islice(pairs2, 10)
list(itertools.islice(pairs2, 10))

