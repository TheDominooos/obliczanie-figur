from obliczanie_figur import *

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

def test_if_negative():
    assert shape.perimeter < 0

# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False