# ------------------------------------
# question 1

Cellphone_models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {
    'make': 'MiMax', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


print(sorted(Cellphone_models, key=lambda i: i['model']))

# ------------------------------------
# question 2

marks = {'Science': [88, 89, 62, 95], 'Math': [77, 78, 84, 80]}


def convert(a, b):
    return {'Science': a, 'Math': b}


x = map(convert, marks['Science'], marks['Math'])
print(list(x))


# ------------------------------------
# question 3
nums = [1, 2, 3, 4, 5, 6, -7, 8, 9.5, -10, 0]
squares = map(
    lambda i: i*i,  filter(lambda i: True if (i > 0) else False, nums))
cubes = map(lambda i: i*i*i, filter(lambda i: True if (i > 0) else False, nums))
print(list(squares))
print(list(cubes))


# ------------------------------------
# question 4
class Circle():
    def radius(self, radius):
        r = radius

    def area(self, r):
        area = 3.142*r*r
        print("Area of the circle is: ", area)

    def peri(self, r):
        peri = 2*3.14*r
        print("Perimeter of the circle is: ", peri)


c = Circle()
radius = 5
c.area(radius)
c.peri(radius)
