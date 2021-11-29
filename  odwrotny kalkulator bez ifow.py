import random
import operator

a={
'+': operator.add,
'-': operator.sub,
'*': operator.mul,
'/': operator.truediv
}
randomNumberOne = random.randint(1, 100)
randomNumberTwo = random.randint(1, 100)
operationType = random.choice(['+', '-', '*', '/'])

result = a[operationType](randomNumberOne, randomNumberTwo)

print("%d " % (randomNumberOne) + operationType + " %d = ?" % (randomNumberTwo))
while True:
        try:
            userInput = float(input())
            break
        except ValueError:
            print("To nie jest liczba!")
comparison={
'True': 'prawidłowy',
'False': 'błędny'
}
trueOrFalse = (userInput == result)
trueOrFalse = str(trueOrFalse)

print("Wynik " + comparison[trueOrFalse])
