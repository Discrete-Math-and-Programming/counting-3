# Combinations and Permutations 

## Reading

* [Levin's 3.4](https://discrete.openmathbooks.org/dmoi4/sec_counting-combperm.html) and [3.5](https://discrete.openmathbooks.org/dmoi4/sec_counting-multisets.html).
* Solve the exercises of the chapters. You can ask in class those that challenged you. Lack of questions means you understood the material.

## Coding

In basic counting there are two parameters:

* whether we allow for repetitions or not;
* whether we care about the order of the elements or not.

This gives us four possibilities for a basic counting problem. You are required
to implement functions for each of these possibilities. The task will always be
counting the number of ways to choose `k` elements from a set of `n` elements.
Therefore in each case your function will take a list of `n` non-identical
elements and an integer `k` and return the number of ways to choose `k`
elements from the list. The functions you are required to implement are: 

* `no_reps_no_order`
* `no_reps_order`
* `reps_no_order`
* `reps_order`

These should be called by a general function `count_arrangements` that will
take the list of `n` elements and the integer `k` and two keyword parameters
`reps` and `order`. The keyword parameters should default to `False`. The
function should call the appropriate function based on the values of the
keyword parameters.

We are not after the actual number of arrangements but the arranements
themselves. Therefore, your functions should return a list of lists. Each list
should represent an arrangement. The lists should be sorted in lexicographic
order.

Python has a built-in module `itertools` that implements all the functions. You are NOT 
allowed to use this module. You can use it to test your functions though.
