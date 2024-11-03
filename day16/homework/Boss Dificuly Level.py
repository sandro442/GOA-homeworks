user_list = []


for i in range(4):
    element = input("შეიყვანეთ ელემენტი: ")
    user_list.append(element)


user_list.append("default")


for item in user_list:
    print(item)


numbers = [9, 5, 94, 711, 52, 96, 71, 8]


min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number

print("ყველაზე პატარა ციფრი:", min_number)


import random
random_item = numbers[3]
print("შემთხვევითი ელემენტი:", random_item)
