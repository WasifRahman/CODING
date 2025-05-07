
#! *
#! **
#! ***
n = 3
for i in range(1,n+1,1): # or range(n+1)
    print("*" * i)

#! *
#! ***
#! *****
n=5
for i in range(1,n+1,2):
    print(i*"*")

# or,
n=3 # 3 karon n+1 e 3 porjonto ..i er value 0,1,2,3 (0 er jonno ekta gap ase)
for i in range(n+1):
    print((2*i-1)*"*")

#!   *
#!  ** 
#! ***
n = 3
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)

#!   *
#!  ***
#! *****
n = 3
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

#! Diamond Pattern
n = 3
# Upper part
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
# Lower part
for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))

#! Hollow Square Pattern
n = 5
for i in range(n):
    if i == 0 or i == n-1:
        print('*' * n)
    else:
        print('*' + ' ' * (n-2) + '*')

#! Right-Angled Triangle Pattern
n = 4
for i in range(1, n+1):
    print('*' * i)

#! Inverted Right-Angled Triangle Pattern
n = 4
for i in range(n, 0, -1):
    print('*' * i)

#! Pyramid Pattern
n = 4
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

#! Inverted Pyramid Pattern
n = 4
for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))

#! Pascal's Triangle
n = 5
for i in range(n):
    print(' ' * (n-i), end='')
    print(' '.join(map(str, str(11**i))))

#! Pascal's Triangle (Alternative Method)
def print_pascals_triangle(n):
    for line in range(1, n+1):
        C = 1
        for i in range(1, line+1):
            print(C, end=' ')
            C = C * (line - i) // i
        print()

n = 5
print_pascals_triangle(n)

#! Floyd's Triangle
n = 5
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=' ')
        num += 1
    print()

#! Butterfly Pattern
n = 4
# Upper part
for i in range(1, n+1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)
# Lower part
for i in range(n, 0, -1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)

#! Zig-Zag Pattern
n = 9
for i in range(1, 4):
    for j in range(1, n+1):
        if ((i+j) % 4 == 0) or (i == 2 and j % 4 == 0):
            print('*', end='')
        else:
            print(' ', end='')
    print()

#! Spiral Matrix
def spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    left, right, top, bottom = 0, n-1, 0, n-1
    num = 1
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left-1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top-1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    for row in matrix:
        print(' '.join(map(str, row)))

n = 5
spiral_matrix(n)


#! Number Pyramid
n = 5
for i in range(1, n+1):
    print(' ' * (n-i) + ' '.join(map(str, range(1, i+1))))

#! Hourglass Pattern
n = 5
for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))
for i in range(2, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

#! Hollow Diamond Pattern
n = 5
for i in range(1, n+1):
    if i == 1:
        print(' ' * (n-i) + '*')
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i-3) + '*')
for i in range(n-1, 0, -1):
    if i == 1:
        print(' ' * (n-i) + '*')
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i-3) + '*')


#! Magic Square
def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    for row in magic_square:
        print(' '.join(str(x) for x in row))

n = 3
generate_magic_square(n)


#! Sierpinski Triangle
def sierpinski_triangle(order, size):
    if order == 0:
        print('*' * size)
    else:
        sierpinski_triangle(order - 1, size // 2)
        print(' ' * (size // 2), end='')
        sierpinski_triangle(order - 1, size // 2)
        print()
        sierpinski_triangle(order - 1, size // 2)
        sierpinski_triangle(order - 1, size // 2)

order = 2
size = 8
sierpinski_triangle(order, size)


#! Koch Snowflake
import turtle
def koch_snowflake(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch_snowflake(order - 1, size / 3)
        turtle.left(60)
        koch_snowflake(order - 1, size / 3)
        turtle.right(120)
        koch_snowflake(order - 1, size / 3)
        turtle.left(60)
        koch_snowflake(order - 1, size / 3)

turtle.speed(0)
for _ in range(3):
    koch_snowflake(3, 300)
    turtle.right(120)
turtle.done()

#! Fractal Tree
import turtle

def fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        fractal_tree(branch_length - 15, t)
        t.left(40)
        fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

t = turtle.Turtle()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
fractal_tree(100, t)
turtle.done()

#! Mandelbrot Set
import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 256

r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.show()

