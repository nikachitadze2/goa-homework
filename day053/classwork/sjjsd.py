# 1)კომენტარის სახით ახსენით split და join მეთოდის დანიშნულება (მოიყვანეთ მაგალითები თითოეულზე)

# 2)შექმენით join მეთოდის კლონი, ანუ შექმენით იგივე join მეთოდი თვითონ join-ის გამოყენების გარეშე. (შექმენით იგივე დანიშნულების მქონე ფუნქცია)

# 3)შექმენით .split() მეთოდის კლონი

# 1) split- ყოფს სტრინგს ნაწილებად დასაყოფად 
#     join- ელემენტებს ერთ სტრინგად აქცევს (აერთიანებს)

# 2
# vqmnit funqcias
def my_join(words):  
    text=" "
    # carieli texti sadac sityva gaertiandeba
    for w in words:   
        #  gaivlis siashi myof sityvebze
        text = text + w + ""
# vamatebt situvas
    return text

print(my_join(["hello", "world"]))


# 3

def my_split(text):
    words = []
    word= ""
# simboloebis naxva
    for c in text:
        # gadis yvela simboloze
        if c == " ":
            # amowmebs aris tu ara sfeisi
            words.append(word)
# sfeisis shemtxvevashi vamatebt sityvas siasi
        else:
            word += c
# tu ar aris vamatebt simbolos sityvas
    words.append(word)
    return words

print(my_split("hello world"))
