
age = int(input("please enter your age: "))
print(age > 13 and age < 19)



score = int(input("enter your score: "))
is_A = score >= 9
is_B = score >= 8 and score < 9
is_C = score >= 7 and score < 8
is_D = score >= 6 and score < 7
is_F = score < 6 

print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_F)




true = True
false = False

print(true and true)
print(false and false)
print(true and false)
print(false and true)

print(true or true)
print(false or false)
print(true or false)
print(false or true)


#>
print(4>5)
print(8>5)
#<
print(13<6)
print(36<40)
#>=
print(20>=17)
print(47>=23)
#<=
print(50<=19)
print(12<=12)
#==
print(23==12)
print(34==19)
#!=
print(14!=14)
print(15!=45)





a = 18
b = 15
c = 8

is_a_greatest = a > b and a > c
is_b_middle = (b > a and b < c) or (b > c and b < a)
is_c_least = c < a and c < b

print(is_a_greatest)
print(is_b_middle)
print(is_c_least)


score = 78

is_pass = score == 50 or score > 50
is_high_pass = score > 75 and score < 90
is_perfect = score == 100
is_failing = score < 50

print(is_pass)
print(is_high_pass)
print(is_perfect)
print(is_failing)
