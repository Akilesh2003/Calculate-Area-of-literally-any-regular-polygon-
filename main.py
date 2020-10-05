#Please note that the formula used provides only an approximate value of area.
from math import tan, pi

n_sides = int(input("Hello! Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("""
The area of the polygon is: """,p_area)
print("""
Thank you for using my polygon area calculator!""")

