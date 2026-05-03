def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new =""
    return new.join(char for char in string_ if char not in vowels)

def square_digits(num):
    result1 = ""

    for digit in str(num):
        idk1 = int(digit) ** 2

        result1 += str(idk1)
    return int(result1)

def high_and_low(numbers):

    num_list = numbers.split()
    
    int_list = [int(x) for x in num_list]

    maximum = max(int_list)
    minimum = min(int_list)
    

    return str(maximum) + " " + str(minimum)

def filter_list(l):
    new_list = []
    for x in l:

        if type(x) == int:
            new_list.append(x)
    return new_list

def descending_order(num):

    s = str(num)
    

    res_list = sorted(s)
    

    res_str = "".join(res_list)

    return int(res_str)
