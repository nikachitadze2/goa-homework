try:
    ("print('hello'")
except SyntaxError:
    print("სუნტაქსები არასწორადაა")

try:
    exec("if True print('hi')")
except SyntaxError:
    print("არასწორია ეს კოდი გთხოვთ შეამოწმოთ")

try:
    exec("for i in range(5) print(i)")
except SyntaxError:
    print("ამ ციკლში შეცდომაა")


try:
    print(x)
except NameError:
    print("ცვლადი არ არსებობს")

try:
    a = b + 2
except NameError:
    print("b არ არის განსაზღვრული")

try:
    myfunc()
except NameError:
    print("ფუნქცია არ არსებობს")



try:
    nums = [1, 2, 3]
    print(nums[9])
except IndexError:
    print("ინდექსი არასწორია")

try:
    word = "python"
    print(word[10])
except IndexError:
    print("სიმბოლო ვერ idzebneba")


try:
    arr = []
    arr[0]
except IndexError:
    print("სია ცარიელია")





try:
    print(5 + "5")
except TypeError:
    print("mati typebi gansxvavdeba radgan stringi da intejeri ver sheertdeba")


try:
    x = len(10)
except TypeError:
    print("len aq ver imushavebs")

try:
    res = "hi" * "2"
except TypeError:
    print("aqac shecdomaa tipebshi")


try:
    num = int("abc")
except ValueError:
    print("es stringi ricxvad ver gadaiqceva tu ricxvi ara")


try:
    age = int(input())
except ValueError:
    print("შეიყვანე რიცხვი")

try:
    import math
    math.sqrt(-4)
except ValueError:
    print("უარყოფითი რიცხვია")
