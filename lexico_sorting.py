# Summary: Write a function to sort an array of strings based on an arbitrary lexicographic ordering.
# The function will take two parameters: an array of strings to sort and a string specifying the lexicographic order.

def get_new_word(word, priority_map):
    new_cs = map(lambda char: priority_map[char], list(word))
    return ''.join(new_cs)

def lexico_sorting(arr_words, str_lexico):
    # len(array_of_inputs) = n
    # len(str_lexico) = k
    # memory: O(2k + 2n) = O(k+n) ~= O(n)
    # requires O(log(n)) runtime - for python sorting functionality

    # create priority map
    priority_map = {}
    priority_map_reverse = {}
    for i in xrange(len(str_lexico)):
        c = str_lexico[i]
        new_c = chr(ord('a') + i)
        priority_map[c] = new_c
        priority_map_reverse[new_c] = c

    new_arr_words = map(lambda word: get_new_word(word, priority_map), arr_words)
    new_arr_words.sort()
    return map(lambda word: get_new_word(word, priority_map_reverse), new_arr_words)


# Given Tests
assert(lexico_sorting(["acb", "abc", "bca"], "abc") == ["abc","acb","bca"])
assert(lexico_sorting(["acb", "abc", "bca"], "cba") == ["bca", "acb", "abc"])
assert(lexico_sorting(["aaa","aa",""], "a") == ["", "aa", "aaa"])

# Personal Tests
assert(lexico_sorting([],"") == [])
assert(lexico_sorting([], "asdf") == [])
assert(lexico_sorting(["asdf", "ddf", "", "asdf", "aaaa"], "fsad") == ["", "asdf", "asdf", "aaaa", "ddf"])
