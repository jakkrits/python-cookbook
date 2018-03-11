from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(red=233, green=200, blue=39)
another_color = Color(39, 29, 19)
print(color.blue)