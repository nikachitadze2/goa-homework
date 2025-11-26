password = "nika"
user_password = input("Enter your password")
while user_password != password:
    user_password = input("Enter your password")
print("corect")


# != -- არ უდრის


num = 1

while num < 21:
    print(num)
    num = num + 1

for i in range(1,20):
    if i % 2 == 0:
        print(i)
    