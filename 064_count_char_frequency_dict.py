A=input("Enter a string: ")
count={}
for char in A:
    count[char] = count.get(char, 0) + 1
print(count)