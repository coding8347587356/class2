ask = input("Enter a string - ")

vowel = {
    "A": 0,
    "E": 0,
    "I": 0,
    "O": 0,
    "U": 0
}


for i in ask:
    if i in vowel:
        vowel[i] += 1

print(vowel)

number = input("Enter a number - ")

count = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

for a in number:
    if a in count:
        count[a]+=1

pangram = True
for b in count.values():
    if b == 0 :
        pangram = False

if pangram:
    print("Entered number is a pangram")
else:
    print("Entered number is not a pangram")