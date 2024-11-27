words = []
n = int(input("რამდენი სიტყვა გსურთ შეიტანოთ? "))
for i in range(n):
    word = input(f"ჩაწერეთ სიტყვა {i+1}: ")
    words.append(word)

result = " ".join(words)

print("შეერთებული სიტყვები:", result)






