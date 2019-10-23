#Linear Search Algorithm.

def LinearSearch(my_list, n, item):
    for i in range(n):
        if item == my_list[i]:
            return i
    return False

my_list = []

n = int(input("Enter no of Elements : "))

for i in range(n):
    element = int(input("Enter Element : "))
    my_list.append(element)

item = int(input("Enter an element to be searched : "))

val = LinearSearch(my_list, n, item)
if val:
    print("Element Found at : %d"%(val+1))
else:
    print("Element not found.")
