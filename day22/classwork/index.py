list_of_odd = []
list_of_even = []
for i in range(1000):
    if i % 2 == 0:
        list_of_even.append(i)
        print(list_of_even)
    elif i % 2 != 0:
        list_of_odd.append(i)
        print(list_of_odd)