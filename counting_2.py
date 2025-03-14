
# Implement two versions of a powerset function.
# Both will take as input a set represented as a list of integers.
# Name the version that uses recursion powerset_rec and the version that uses
# iteration powerset_iter.


def test():

    results = {}
    test_cases =\
            {'powerset_rec': [
                {'args': [[]],
                 'expected': [[]],
                 'key': lambda x: sorted(x)},
                {'args': [[1,2,3]],
                 'expected': sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
                 'key': lambda x: sorted(x)}],
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
