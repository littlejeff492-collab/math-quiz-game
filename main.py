import random

score = 0
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = int(input(f"What is {a} + {b}? "))
    if answer == a + b:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {a+b}")

print(f"Your final score: {score}/5")
