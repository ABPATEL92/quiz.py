print("Welcome to the quiz")

qustions = 3
score = 0
a = "correct"
b = "incorrect"

ans = input("What is my favourite graphics card?")
if ans.lower() == 'rtx 4090':
    print(a)
    score +=1
else:
    print(b)

ans = input("What is my channel called?")
if ans.lower() == 'abp coder':
    print(a)
    score +=1
else:
    print(b)

ans = input("Is coding boring to me:(y/n)")
if ans.lower() == 'n':
    print(a)
    score +=1
else:
    print(b)

cal = 100 / qustions
percent = cal * score

ans = input("Do you want to know your score:(y/n)")
if ans.lower() == 'y':
    print("You got", percent, "% with a score of", score)
else:
    quit()

