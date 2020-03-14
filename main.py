# Determine whether a one-to-one character mapping exists from one string, s1, to another string,
# s2.
# For example, given s1 = abc and s2 = bcd, print "true" into stdout since we can map each
# character in "abc" to a character in "bcd".
# Given s1 = foo and s2 = bar, print "false" since the character ‘o’ cannot map to two characters.
# But given s1 = bar and s2 = foo, print "true" since each character in "bar" can be mapped to a
# character in "foo".


def check(s1, s2):
    # assuming if length of both strings should be same for one to one mapping
    if len(s1) != len(s2):
        return False
    res = dict()
    for i, j in zip(s1, s2):
        if i in res.keys() and j != res.get(i):
            return 'false' # if one to one mapping fails
        else:
            res[i] = j
    return 'true'   # if one to one mapping

import sys
if len(sys.argv) > 2:
    s1, s2 = sys.argv[1], sys.argv[2]
else:
    print('false')

print(check(s1, s2))
