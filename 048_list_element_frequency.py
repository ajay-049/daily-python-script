A=input("Enter a list of elements separated by spaces: ").split()
freq = {}
for element in A:
    freq[element] = freq.get(element, 0) + 1
for element, count in freq.items():
    print(f"{element}: {count}")