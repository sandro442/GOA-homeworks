string = "გაახვიე,იხვის,ტოლმა"
delimiter = ","

result = []
word = ""
for char in string:
    if char == delimiter:
        result.append(word)
        word = ""
    else:
        word += char

if word:
    result.append(word)

print(result)  

