A={'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(A.items(), key=lambda item: item[1]))
print(sorted_dict)