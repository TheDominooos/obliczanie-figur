import random

randomNumberOne = random.randint(1, 100)
randomNumberTwo = random.randint(1, 100)
operationType = random.randint(1, 4)
if operationType == 1:
    print ("%d + %d = ?" % (randomNumberOne, randomNumberTwo))
    result = randomNumberOne + randomNumberTwo
elif operationType == 2:
    print ("%d - %d = ?" % (randomNumberOne, randomNumberTwo))
    result = randomNumberOne - randomNumberTwo
elif operationType == 3:
    print ("%d * %d = ?" % (randomNumberOne, randomNumberTwo))
    result = randomNumberOne * randomNumberTwo
else:
    print ("%d / %d = ? (Wynik zaokrąglij do dwóch miejsc po przecinku)" % (randomNumberOne, randomNumberTwo))
    result = randomNumberOne / randomNumberTwo
    result = round(result, 2)

while True:
        try:
            userInput = float(input())
            break
        except ValueError:
            print("To nie jest liczba!")
if userInput == result:
    print("Wynik prawidłowy")
else:
    print("Wynik błędny")