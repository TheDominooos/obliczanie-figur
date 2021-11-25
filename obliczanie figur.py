from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
    
    def area(self):
        return self.side_1 * self.side_2

    def perimeter(self):
        return self.side_1*2 + self.side_2*2


class Square(Rectangle): 
    def __init__(self, side_1):
        super().__init__(side_1, side_1)


class Triangle(Figure):
    def __init__(self, height, side_1, side_2, side_3):
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def area(self):
        return self.side_1 * self.height * 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class Wheel(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


dictionary = {
    1: {
        "shape_class": Square,
        "input": ["Podaj 1 bok: "]
    },
    2: {
        "shape_class": Rectangle,
        "input": ["Podaj 1 bok: ", "Podaj 2 bok: "]
    },
    3: {
        "shape_class": Triangle,
        "input": ["Podaj wysokość: ", "Podaj podstawę: ", "Podaj 2 bok: ", "Podaj 3 bok: "]
    },
    4: {    
        "shape_class": Wheel,
        "input": ["Podaj promień: "]
    }
}

while True:
    try:
        user_choice = int(input("1. Kwadrat\n2. Prostokąt\n3. Trójkąt\n4. Koło\nPodaj numer figury którą chcesz obliczyć: "))
        
        select = dictionary[user_choice]
        inputs = []
        for user_input in select["input"]:
            number = float(input(user_input))
            inputs.append(number)
        shape = select["shape_class"](*inputs)
        break
    except ValueError:
        print("Błędna liczba")
    except KeyError:
        print("Nie ma takiej opcji!")

print("Pole wynosi: ",shape.area())
print("Obwód wynosi: ",shape.perimeter())
