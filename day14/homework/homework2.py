start=int(input("შეიყვანეთ დიაპაზონის დაწყების რიცხვი: "))
end=int(input("შეიყვანეთ დიაპაზონისდასრულების რიცხვი: "))
for num in range(start, end + 1):
    if num % 2 == 0 and num % 3 == 0:
        print(num, "ეს ციფრები არის 3-ის და 2-ისჯერადები")
    else:
        print(num, "არ არის 3-ის და 2-ის ჯერადი")
