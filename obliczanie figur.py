from abc import ABC, abstractmethod
import math


class Figure():
    @abstractmethod
    def area():
        pass

    def perimeter():
        pass

class Rectangle(Figure):
    def __init__(self, p1, p2):
        self.side_1 = p1
        self.side_2 = p2
    
    def area(self):
        return self.side_1 * self.side_2

    def perimeter(self):
        return self.side_1*2 + self.side_2*2


class Square(Rectangle):
    def __init__(self, p1):
        self.side_1 = p1
        self.side_2 = p1


class Triangle(Figure):
    def __init__(self, p1, p2, p3, p4):
        self.height = p1
        self.side_1 = p2
        self.side_2 = p3
        self.side_3 = p4
    
    def area(self):
        return self.side_1 * self.height * 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class Wheel(Figure):
    def __init__(self, p1):
        self.radius = p1
    def area(self):
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


while True:
    try:
        user_choice = int(input("1. Kwadrat\n2. Prostokąt\n3. Trójkąt\n4. Koło\nPodaj numer figury którą chcesz obliczyć: "))
        break
    except ValueError:
        print("Nie ma takiej opcji!")
        quit()


while True:
    try:
        if user_choice == 1:
            shape = Square(float(input("Podaj bok: ")))
        elif user_choice == 2:
            shape = Rectangle(float(input("Podaj 1 bok: ")), float(input("Podaj 2 bok: ")))
        elif user_choice == 3:
            shape = Triangle(float(input("Podaj wysokość: ")), float(input("Podaj podstawę: ")), float(input("Podaj 2 bok: ")), float(input("Podaj 3 bok: ")))
        elif user_choice == 4:
            shape = Wheel(float(input("Podaj promień: ")))
        else:
            print("Nie ma takiej opcji!")
        break
    except ValueError:
        print("Błędna liczba")

print("Pole wynosi: ",shape.area())
print("Obwód wynosi: ",shape.perimeter())