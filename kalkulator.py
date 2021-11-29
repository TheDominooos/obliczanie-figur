while True:
    try:
        numberOne = float(input("Podaj pierwszą liczbę: "))
        break
    except ValueError:
        print("To nie jest liczba!!!")    
while True:
    try:
        numberTwo = float(input("Podaj drugą liczbę: "))
        break
    except ValueError:
        print("To nie jest liczba!!!")    
while True:
    try:
        operationType = int(input("Wybierz rodzaj działania:\n1.Dodawanie\n2.Odejmowanie\n3.Mnożenie\n4.Dzielenie\n"))
        if operationType == 5:
            print("Nie ma takiego działania!")
            continue
        break
    except ValueError:
        print("Nie ma takiego działania!")
if operationType == 1:
    print("Wynik wynosi: %0.2f" % float(numberOne + numberTwo))
elif operationType == 2:
    print("Wynik wynosi: %0.2f" % float(numberOne - numberTwo))
elif operationType == 3:
    print("Wynik wynosi: %0.2f" % float(numberOne * numberTwo))
elif operationType == 4:
    try:
        print("Wynik wynosi: %0.2f" % float(numberOne / numberTwo))
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")
