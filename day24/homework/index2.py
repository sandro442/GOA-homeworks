words = ['hello', 'world', 'python']
delimiter = ","
result = ""
for i, word in enumerate(words):
    result += word
    if i < len(words) - 1:
        result += delimiter

print(result)  
