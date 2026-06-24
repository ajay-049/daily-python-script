A=input("Enter the first list of elements separated by spaces: ").split()
B=input("Enter the second list of elements separated by spaces: ").split()
merged_list = A + B
freq = {}
for element in merged_list:
    freq[element] = freq.get(element, 0) + 1
for element, count in freq.items():
    print(f"{element}:{count}")