pid = str(input("Podaj pesel: "))

year_of_birth = pid[0 : 2]
month_of_birth = int(pid[2 : 4])
day_of_birth = int(pid[4 : 6])
gender = int(pid[9])
control_number = 0
index = 0

for number in pid:
    if index == 0 or index == 4 or index == 8:
        control_number += (int(number)*1) % 10
    if index == 1 or index == 5 or index == 9:
        control_number += (int(number)*3) % 10
    if index == 2 or index == 6:
        control_number += (int(number)*7) % 10
    if index == 3 or index == 7:
        control_number += (int(number)*9) % 10
    index+=1

print("suma kontrolna: %d" % (control_number))
control_number = control_number % 10
control_number = 10 - control_number
print("liczba kontrolna: %d" % (control_number))

if len(pid) != 11:
    print("Nieprawidłowa ilość cyfr")
    quit()
if control_number != int(pid[10]):
    print("Liczba kontrolna się nie zgadza")
    quit()
if pid.isdigit() == False:
    print("Pesel musi zawierać same cyfry!")
    quit()

if 81 <= int(month_of_birth) <= 92:
    birth_century = 18
    month_of_birth = int(month_of_birth) - 80
elif 1 <= int(month_of_birth) <= 12:
    birth_century = 19
elif 21 <= int(month_of_birth) <= 32:
    birth_century = 20
    month_of_birth = int(month_of_birth) - 20
elif 41 <= int(month_of_birth) <= 52:
    birth_century = 21
    month_of_birth = int(month_of_birth) - 40
else:
    print("Liczba miesiąca urodzenia się nie zgadza")
    quit


dateOfBirth = "%d.%d.%d%s" % (day_of_birth, month_of_birth, birth_century, year_of_birth)
print(dateOfBirth)

if(gender % 2 == 0):
    print("Płeć: Kobieta")
else:
    print("Płeć: Mężczyzna")