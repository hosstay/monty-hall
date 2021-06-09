import random

print("Monty Hall Problem")

random.seed()

iterations = 100000

success = 0
failure = 0

n = iterations
while n > 0:
    n = n - 1

    doorWithCar = random.randint(1, 3)

    guess = random.randint(1, 3)

    doorToReveal = 0

    if doorWithCar == 1:
        if guess == 1:
            doorToReveal = random.randint(2,3)

        if guess == 2:
            doorToReveal = 3

        if guess == 3:
            doorToReveal = 2

    if doorWithCar == 2:
        if guess == 1:
            doorToReveal = 3

        if guess == 2:
            doorToReveal = 2
            while doorToReveal == 2:
                doorToReveal = random.randint(1, 3)

        if guess == 3:
            doorToReveal = 1

    if doorWithCar == 3:
        if guess == 1:
            doorToReveal = 2

        if guess == 2:
            doorToReveal = 1

        if guess == 3:
            doorToReveal = random.randint(1,2)

    answer = doorToReveal

    #while answer == doorToReveal or answer == guess:
    #    answer = random.randint(1,3)

    answer = guess

    if answer == doorWithCar:
        success = success + 1
    else:
        failure = failure + 1

print(str(success) + ' Successes')
print(str(failure) + ' Failures')

print(str(success / iterations * 100) + '%')
