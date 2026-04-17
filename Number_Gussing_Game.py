import random
r = random.randrange(0, 101)  # number between 0 to 100
# r = random.randint(0, 101)  # number between 0 to 101
count = 0

num = int(input("Enter a number between 0 to 100: "))

while num != r:
    count += 1
    if num < r:
        print("Higher the number.")
    elif num > r:
        print("Lower the number.")
    num = int(input("Try again: "))

# When guessed correctly
count += 1
print(f"Yeah! You got it in {count} tries 🎉")