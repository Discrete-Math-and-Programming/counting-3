# `count_arrangements`
# Inputs: lst (list) a list of non-identical items
#         k (int) indicating the length of each arrangement
#         reps (boolean) indicating whether repetitions are allowed
#         order (boolean) indicating whether order matters
# Output: (lst) a list of tuples of all possible arrangements of length k

# `reps_order`

# `reps_no_order`

# `no_reps_order`

# `no_reps_no_order`


def test():

    from itertools import combinations, combinations_with_replacement, permutations, product
    seq = [1,2,3,4,5]

    results = {}
    test_cases =\
            {
                'reps_order': [
                    {'args': [seq, 3],
                     'expected': list(product(seq, repeat=3)),
                     'key': lambda result: sorted(result)
                     }
                ],
                'reps_no_order': [
                    {'args': [seq, 3],
                     'expected': list(combinations_with_replacement(seq, 3)),
                     'key': lambda result: sorted(
                         [tuple(sorted(x)) for x in result])}
                ],
                'no_reps_no_order': [
                    {'args': [seq, 3],
                     'expected': list(combinations(seq, 3)),
                     'key': lambda result: sorted(
                         [tuple(sorted(x)) for x in result])}
                ],
                'no_reps_order': [
                    {'args': [seq, 3],
                     'expected': list(permutations(seq, 3)),
                     'key': lambda result: sorted(result)}
                ],
            } 


    for funcname, cases  in test_cases.items():
        if funcname not in globals():
            results[funcname] = "Not Implemented"
        else:
            try:
                results[funcname] =  "OK" if all(
                    [case['key'](eval(funcname)(*case['args'])) == case['expected']
                     for case in cases]) else "Not OK"
            except Exception as e:
                results[funcname] = "Error -- " + str(e)

    print("Function Name            | Status")
    print("-------------------------|--------")
    for key, value in results.items():
        print(f"{key:<24} | {value}")
