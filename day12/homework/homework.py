# 1 დავალება👇

# for loop


for i in range(1,50,2):
    print(i)

print("--------------------")
# while loop

i=1
while i < 50:
    print(i)
    i+=2    

print("------------------")    
# 2 დავალება 👇
# Quadrilateral


size=5
for i in range (size):
    print(('*' * size))
    
print("-------------------------------")
# while loop Quadrilateral


size=5
i=0
while i <size:
    print('*' * size)
    i+=1

print("-------------------------------------")
# 3 დავალება 👇
# for loop rectangle


height=5
width=3
for i in range (height):
    print('*' *  width)    

print("----------------------------")
# while loop rectangle


height=5
width=3
i=0
while i < height:
    print('*' * width)
    i+=1    

# 4 დავალება👇
print("-----------------------------------")


for num1 in range (1,4):
    for num in range(1,4):
        print("(num1): " + str(num1) + ", (num): " + str(num))


print("----------------------------")



# difycult project

while True:
    username= input("enter username : ")
    password= input("enter password: ")
    email = input("enter email: ")
    confirm= input("Confirm registration  Usename:" + str(username) + ",password:" + password + ", email:" + str(email) + ":")
    if confirm.lower() == 'yes':
        print("registration succesful!")
        break
    else:
        print("try again.")
