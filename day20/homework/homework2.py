# 1-დან 30-მდე
numbers = list(range(1, 31))

# 5-ის და 3-ის ჯერადები
multiples_of_5_and_3 = [num for num in numbers if num % 5 == 0 and num % 3 == 0]

print("5-ის და 3-ის ჯერადები: " + str(multiples_of_5_and_3))
