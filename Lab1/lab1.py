
import sys
import math

a = int(input('Number a: '))
b = int(input('Number b: '))
c = int(input('Number c: '))

if a == 0 or b == 0 or c == 0: sys.exit('Numbers should not be equal to zero! Try again')

def quadratic(a, b, c):
    discrim = b ** 2 - 4 * a * c
    if discrim < 0:
        print( f'Equation is: {a}x^2 + {b}x + {c} = 0 \nThere are 0 roots' )
        print('Discriminant value is negative.')
        return
    if discrim == 0:
        x = -b / 2 * a
        print( f'Equation is: {a}x^2 + {b}x + {c} = 0 \nThere are 1 root \nx === {x}')
        return
    if discrim >= 0:
        x1 = ( -b + math.sqrt(discrim) ) / 2 * a
        x2 = ( -b - math.sqrt(discrim) ) / 2 * a
        print( f'Equation is: {a}x^2 + {b}x + {c} = 0 \nThere are 2 roots \nx1 === {x1} \nx2 === {x2}')
        return

quadratic(a, b, c)
print('biba')