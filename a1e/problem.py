# Objektorientierte Programmierung (OO)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Prozedurale Programmierung
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

# Funktionale Programmierung
def area(radius):
    return 3.14159 * radius ** 2

# Hauptprogramm
if __name__ == "__main__":
    radius = 5

    # Objektorientierte Programmierung
    circle = Circle(radius)
    oo_area = circle.area()
    print("OO - Fläche des Kreises:", oo_area)

    # Prozedurale Programmierung
    procedural_area = calculate_circle_area(radius)
    print("Prozedural - Fläche des Kreises:", procedural_area)

    # Funktionale Programmierung
    functional_area = area(radius)
    print("Funktional - Fläche des Kreises:", functional_area)
