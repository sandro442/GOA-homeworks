string = "hello world"
old = "world"
new = "python"
result = ""
i = 0
while i < len(string):
    if string[i:i+len(old)] == old:
        result += new
        i += len(old)
    else:
        result += string[i]
        i += 1

print(result) 
