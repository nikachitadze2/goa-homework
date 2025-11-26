# students= [ "nika",  "nika", "gio", "luka"]
# students.append("vano")
# students.pop("luka")
# print(students.count("nika"))

# # list ინდექსი არის ერთ ერთი კოლექციის და მონაცემთა ტიპი რომელიც შეცვლადია , იდექსები გააჩნია

# students= ("nika","gio", "luka")
# students.clear()
# print(students)

# # tuple არის დალაგებული მარა შეუცვლელი კოლექცაია


# fruit = {"banana", "apple"}
# vagetebels = {"tomato", "potato"}
# set3 = fruit.union(vagetebels)
# print(set3)

# #set არის დაულაგებელი კოლექცია რომელშიც ინახება მხოლოდ უნიკალური ელემენტი , ორი ერთნაირი არ შეიძლება

# students= [ "nika",  "nika", "gio", "luka"]
# print(students)


user_data ={
"city": "tbilisi",
"name":"nika",
"age": 16,
}
print(user_data)


# 1)შექმენით dictionary სადაც შენახული იქნება შენი სახელი, ასაკი და ქალაქი.

# შემდეგ ამოიღეთ კონკრეტული მნიშვნელობა და შეინახე ცვლადში.

# ასევე შეცვალეთ რომელიმე მნიშვნელობა რაც გექნება dictionary ში.

# წაშალე ერთი ელემენტი.

# for ციკლის მეშვეობით გამოიტანე თითოეული key და value (არ ამიხსნია ჯერ და მაინტერესებს თუ იზამთ :)) )


# ასევე გამოიტანეთ მხოლოდ value ები

person= {
    "name": "nika",
    "age": 16,
    "city": "თბილისი"
}

user_age = person.get( "age")

person["name"] = "vaja"

person.pop("age")



