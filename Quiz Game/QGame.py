questions = (
"Question 1 (a)",
"Question 2 (b)",
"Question 3 (c)",
"Question 4 (d)",
"Question 5 (e)"
)


options = (
    "A.A1",
    "B.A2",
    "C.A3",
    "D.A4",
    "E.A5"
)

answers = ("A","B","C","D","E")

guesses = []

score = 0

qnum = 0


for question in questions:
    print("--------------------------")
    print(question)
    print("Answer:")
    ans = input()
    guesses.append(ans)
    if ans == (options[qnum][0]):
        score +=1
    qnum +=1
print(score)