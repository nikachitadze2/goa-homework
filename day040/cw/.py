# 1)შექმენით სია სადაც გექნებათ რიცხვები მოცემული და 

# ახალ სიაში ჩაამატეთ ისეთი რიცხვები რომლებიც იყოფა 3ზეც და 5 ზეც

# 2)შექმენით სია სადაც გექნებათ მოცემული სახელები, შემდეგ ახალ სიაში ჩაამატეთ ისეთი
# სახელები სახელები რომლის სიმბოლოების რაოდენობაც არის ლუწი რიცხვი

# 3) ახსენით კომენტარებით რაში გვჭირდება list comprehension


numbers = [5, 10, 15, 20, 30]
result = []

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        result.append(num)
print(result)



names = ["Giorgi", "Nika", "Ani", "giga", "Luka",]
even = []
for name in names:
    if len(name) % 2 == 0:
        even.append(name)
print(even)


# List comprehension არის მოკლე და სწრაფი გზა 
# mag:
# even = [ for i in numbers if i % 2 == 0]
