# name = "hello world"

# #uppercase a string
# print(name.upper())

# #caplitalize a string
# print(name.capitalize())

# #reverse a string [begin, end, step]
# print(name[::-1])

# #leetspeak
# leetspeak = input("Enter a sentence: ").upper()
# sentence = ""
# for x in leetspeak:
#     if x == "A":
#         sentence += "4"
#     elif x == "E":
#         sentence += "3"
#     elif x == "G":
#         sentence += "6"
#     elif x =="L":
#         sentence += "1"
#     elif x == "O":
#         sentence += "0"
#     elif x == "S":
#         sentence += "5"
#     elif x == "T":
#         sentence += "7"
#     else:
#         sentence += x

# print(sentence)

# #long-long vowels
# word = input("Enter a word: ")
# if "aa" in word:
#     print(word.replace("aa", "aaaaa"))
# elif "ee" in word:
#     print(word.replace("ee", "eeeee"))
# elif "ii" in word:
#     print(word.replace("ii", "iiiii"))
# elif "oo" in word:
#     print(word.replace("oo", "ooooo"))
# elif "uu" in word:
#     print(word.replace("uu", "uuuuu"))

#caesar cipher
alphabet = "abcdefghijklmnopqrstuvwxyz "
alphabet_two = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
cipher = "bcdefghijklmnopqrstuvwxyza "
cipher_two = "BCDEFGHIJKLMNOPQRSTUVWXYZA "
phrase_one = input("What do you want to decrypt?: ")
phrase_two = input("What do you want to cipher?: ")

def remove_password(list):
    translate = ""
    for x in list:
        if x in cipher:
            translate += cipher[alphabet.index(x)]
        if x in cipher_two:
            translate += cipher_two[alphabet_two.index(x)]
    print(translate)

def add_password(list):
    translate = ""
    for x in list:
        if x in alphabet:
            translate += alphabet[cipher.index(x)]
        if x in alphabet_two:
            translate += alphabet_two[cipher_two.index(x)]
    print(translate)

remove_password(phrase_one)
add_password(phrase_two)






