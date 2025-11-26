# <!-- 1)მომხმარებელს შემოატანინეთ საყვარელი სპორტი  და ტერმინალში დაბეჭდეთ ის

# 2)მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი, საცხოვრებელი ქალაქი,ჰობი შემდეგ 
# კი დაბეჭდეთ გრძელი წინადადება მაგ. შენი სახელია "სახელი და გვარი" შენი ასაკია "ასაკი" და ასე შემდეგ.

# 3)მოხმარებელს შემოატანინეთ რიცხვი და მაგ რიცხვს გამოაკელით 20 და გაამრავლეთ 3 ზე

# 4)მოხმარებელს შემოატანინეთ რიცხვები ანუ num,num1,num2...და ასე შემდეგ და საბოლოოდ
#  გამოითვალეთ მაგ რიცხების საშუალო არითმეტიკული
# მაგალიტად: 
# 2, 2, 2 = 2 + 2 + 2 = 6 / 3 = 2 ანუ რიცხვების ჯამი გავყოთ რაოდენობაზე(მინიმუმ 3 რიცხვის 
# ცვლადი გქონდეთ შექმნილი

# 5)აუცილებლად გადახედეთ დღევანდელი გაკვეთილის ჩანაწერს

# 6)აუცილებლად გადადით resources_61 ში და გადახედეთ რესურსებსაც -->



# user = input("enter sport")


user_name = input("user_name")
user_age = input("user_age")
user_livs = input("user livs")
user_hobies = input("user_hobies")

print(user_name + user_age + user_livs + user_hobies)

user_number = int(input("enter number"))
result = user_number - 20 
print(result*3)

num1 = int(input("enter number"))
num2 = int(input("enter number"))
num3 = int(input("enter number"))
sum = num1 + num2 + num3
result = sum // 3
print(result)
