
try:
    num = int(input("chawere ricxvi an cifri: "))
    print("sheni sheyvanili ricxvia:", num)
except ValueError:
    print("es ricxvi ar aris")


numbers = [10, 20, 30]

try:
    print(numbers[100000000])
except IndexError:
    print("aseti indeqsi siashi ararsebobs")


try:
    result = 5 + "10"
except TypeError:
    print("strings da intejers shoris damateba arsheidzleba"))
