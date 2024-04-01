import itertools

def print_permutations(lst):
    permutations = list(itertools.permutations(lst))
    for permutation in permutations:
        print(permutation)


print_permutations([1, 2, 3])