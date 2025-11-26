# 1) მომხმარებელს შემოატანინეთ სიტყვა. ტერმინალში კი დაბეჭდეთ ეს სიტყვა ისე რომ იყოს:

# 1. ყველა პატარა ასო;
# 2. ყველა დიდი ასო;
# 3. პირველი ასო დიდი, ხოლო ყველა დანარჩენი პატარა.

# 2) მომხმარებელს შემოატანინეთ სამი წინადადება და თითოეულზე გამოიყენეთ სხვადასხვა სტრინგის მეთოდი:
# პირველ წინადადებაზე — .lower()
# მეორე წინადადებაზე — .upper()
# მესამე წინადადებაზე — .capitalize()

# 3) ცვლადში შეინახე შენი სახელი. მომხმარებელს შეეკითხე თავისი სახელი, იმ შემთხვევაში თუ თქვენი სახელები 
# ემთხვევა დაბეჭდეთ "Our names are similar!", თუ არ ემთხვევა დაბეჭდეთ "We have different names". გაითვალისწინეთ,
#  რომ მომხმარებელმა შეიძლება თქვენნაირი სახელი შემოიტანოს, თუმცა სახელის ასოები შესაძლოა იყოს სხვადასხვა შრიფტის
#  ზომით, ამიტომ ამან თქვენ პროგრამაში შეფერხება არ უნდა გამოიწვიოს (გამოიყენეთ ნასწავლი სტრინგის მეთოდები)

# 4) ცვლადში შეინახე წინადადება, დაწერე ისეთი პროგრამა რომ მხოლოდ წინადადების პირველი სიტყვა იყოს დიდი ასოთი,
#  დანარჩენი კი იყოს პატარა.

# 5) კომენტარის სახით ჩამოწერეთ ყველა სტრინგის მეთოდი, რომელიც ისწავლეთ. თითოეულს მიუწერეთ დეტალური
#  განმარტება და მათზე მოიყვანეთ თითო-თითო მაგალითი.


word = input("enter word")
print(word.upper())
print(word.capitalize())
print(word.lower())

proposal = input("enter proposal")
print(proposal.upper())
proposal = input("enter proposal")
print(proposal.lower())
proposal = input("enter proposal")
print(proposal.capitalize())


my_name = "nika"
your_name = input("enter your name")
if my_name == your_name:
    print("Our names are similar!".lower())
else:
    print("We have different names")

proposal = "nika roGOR XAr"
print(proposal.upper())
# upper() ასოებს გარდაქმნის დიდ ასოებად
name = "nika"
print(name.upper())

# lowercase ასოებს გარდაქმნის პატარა ასოებად
name = "NIKA"
print(name.lower())

#capitalize სიტყვის პირველ ბგერას გარდარქმნის დიდად
name = "nika"
print(name.capitalize())

#isupper ასრულებს ბულიონის როლს თუ დიდი ასეობითაა გამოვა true
name = "NIKA"
print(name.isupper())

#isalpha amowmebs patara asoebitaa tu ara teqsti
name = "nika"
print(name.isalpha())

# find() პოულობს სიტყვაში ნებისმიერ კონკრეტულ ასოს რომელ ადგილზე მდებარეობს
name = "nika"
print(name.find("კ"))

