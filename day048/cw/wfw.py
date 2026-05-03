# capitalize() სტრინგის პირველ ასოს დიდს ხდის დანარჩენს კი პატარას
inp = input("enter smth: ")
san = inp.capitalize()
print(san)
# count() == ითვლის სიაში რამდენჯერ მეორდება ერთიდაიგივე
list2 = ["ანდრია","გიორგი","ნიკოლოზი"]
print(list2.count("ანდრია"))
# endswith() თუ ენდსვითში ჩაწერილი სიტყვა არის ცვლადში აბრუნებს true  - ს
home = "Hello it is home."
checking = home.endswith(".")
print(checking)
# find() ეძებს სტრინგს, შემდეგ თუ იპოვის მას პრინტავს იმ ნომერზე სადაცაა
listt = "სალამი ნიკა."
findd = listt.find("ს")
print(findd)
# index() სადაც არის ნაპოვნი სიაში იმ სიას პრინტავს
indexingg = ["agagagag", "kgamskgkas", "gjaksk"]
print(indexingg.index("agagagag"))
# isalnum() როდესაც ყველა მაგალითად სტრინგი არის ან ციფრი აბრუნებს თრუს 
txt = "idk123"
x = txt.isalnum()
print(x)



# isalpha() აბრუნებს True-ს, თუ სტრიქონში ყველა სიმბოლო ანბანის მიხედვითაა


txt2 = "abgz"

y= txt2.isalpha()
print(y)