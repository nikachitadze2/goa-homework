# 1) ცვლადში შეინახეთ ნებისმიერი სიტყვა, შემდეგ კი მომხმარებელსაც შემოატანინეთ
#  რაიმე სიტყვა, თუ თქვენი სიტყვები ერთმანეთს დაემთხვევა გამოუტანეთ "Our words are similar !",
# სხვა შემთხვევაში - "We have different words". hint: დაგჭირდებათ პირობითი განცხადებები და სტრინგის მეთოდები.
#  ეს შემოწმება უნდა იყოს case-insensitive

# 2) გადაიმეორეთ განვლილი მასალა (Py, HTML, CSS)
name = "niks"
username = input("enter your name")
if username == name:
    print("Our words are similar !")
else:
    print("We have different words")