# `count_arrangements`
# Inputs: lst (list) a list of non-identical items
#         k (int) indicating the length of each arrangement
#         reps (boolean) indicating whether repetitions are allowed
#         order (boolean) indicating whether order matters
# Output: (lst) a list of tuples of all possible arrangements of length k


def count_arrangements(lst, k, reps, order):
    from itertools import combinations, combinations_with_replacement, permutations, product
    if reps and order:
        return lstist(product(lst, repeat=k))
    elif reps and not order:
        return list(combinations_with_replacement(lst, k))
    elif not reps and order:
        return list(permutations(lst, k))
    else:
        return list(combinations(lst, k))

# `reps_order`

# `reps_no_order`

# `no_reps_order`

# `no_reps_no_order`


def test():

    from itertools import combinations, combinations_with_replacement, permutations, product
    seq = [1,2,3,4,5]

    results = {}
    test_cases =\
            {'no_reps_no_order': [
                {'args': [seq, 3],
                 'expected': sorted(list(combinations(seq, 3))),
                 'key': lambda x: x}
                ],
             'powerset_iter': [
                {'args': [[]],
                 'expected': [[]],
                 'key': lambda x: sorted(x)},
                {'args': [[1,2,3]],
                 'expected': sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
                 'key': lambda x: sorted(x)}]
            } 


    for funcname, cases  in test_cases.items():
        try:
            results[funcname] =  "OK" if all([case['key'](eval(funcname)(*case['args'])) == case['expected'] for case in cases]) else "Not OK"
        except NameError:
            results[funcname] = "Not Implemented"
        except Exception as e:
            results[funcname] = "Error -- " + str(e)

    print("Function Name            | Status")
    print("-------------------------|--------")
    for key, value in results.items():
        print(f"{key:<24} | {value}")
