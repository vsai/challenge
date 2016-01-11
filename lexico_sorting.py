# Summary: Write a function to sort an array of strings based on an arbitrary lexicographic ordering.
# The function will take two parameters: an array of strings to sort and a string specifying the lexicographic order.

def get_priority(word, priority_map):
    # input:  word = 'abc', priority_map = {'a': 1, 'b': 3, 'c': 2}
    # output: ('abc', [1, 3, 2])
    priority_val = map(lambda char: priority_map[char], list(word))
    return (word, priority_val)

def lexico_sorting(arr_words, str_lexico):
    # len(array_of_inputs) = n
    # len(str_lexico) = k
    # requires O(k) memory for the priority map. in this case, k = 26. general case, bounded by # of ascii characters.
    # O(total number of letters) memory additional - this requires more memory because we're storing priorities for each of the words
    # requires O(log(n)) runtime - for python sorting functionality

    # create priority map
    priority_map = {}
    for i in xrange(len(str_lexico)):
        c = str_lexico[i]
        priority_map[c] = i

    arr_priorities = map(lambda word: get_priority(word, priority_map), arr_words)
    arr_priorities_sorted = sorted(arr_priorities, key=lambda priority: priority[1])
    return map(lambda priority: priority[0], arr_priorities_sorted)


# Given Tests
assert(lexico_sorting(["acb", "abc", "bca"], "abc") == ["abc","acb","bca"])
assert(lexico_sorting(["acb", "abc", "bca"], "cba") == ["bca", "acb", "abc"])
assert(lexico_sorting(["aaa","aa",""], "a") == ["", "aa", "aaa"])

# Personal Tests
assert(lexico_sorting([],"") == [])
assert(lexico_sorting([], "asdf") == [])
assert(lexico_sorting(["asdf", "ddf", "", "asdf", "aaaa"], "fsad") == ["", "asdf", "asdf", "aaaa", "ddf"])
