from operator import itemgetter

a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]


print(sorted(a, key=itemgetter(1)))