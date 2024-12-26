def string_to_array(s):
    if s:
        return s.split()
    else:
        return [""]

def string_to_number(s):
    return int(s)

def string_to_number(s):
    return int(s)
def fake_bin(x):
    stringg = ""
    for char in x:   
        if int(char) < 5:
            stringg += "0"
        else:
            stringg += "1"
    return stringg
def high_and_low(numbers):
    string_list = numbers.split()
    num_list = []
    for i in string_list:
        num_list.append(int(i))
    highest = max(num_list)
    lowest = min(num_list)
    highest_str = str(highest)
    lowest_str = str(lowest)
    result = highest_str + " " + lowest_str
    return result