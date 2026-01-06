try:
    number = int(input("Enter a number: "))  
    print("You entered:", number)           
except:
    print("This is not a number!")            



my_list = [1, 2, 3]  

try:
    print(my_list[10])  
except:
    print("This index does not exist!")



try:
    result = 5 + "hello"  
    print(result)
except:
    print("You cannot add number and text!")
