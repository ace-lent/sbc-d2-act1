import random

bet = input("Place bet (3 numbers with spaces): ").split()
bet = [int(num) for num in bet]

result = [random.randint(1, 9) for i in range(3)]

print(f"The result is: {result}")

if bet == result:
    print("Scenario 1: You win!")
elif bet[1:] == result[1:]:
    print("Scenario 2: You almost won")
elif bet[0] == result[0] or bet[1] == result[1] or bet[2] == result[2]:
    print("Scenario 3: You partially got it")
else:
    print("Scenario 4: You lost")
