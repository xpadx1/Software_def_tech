import sys
import math

def main():
    interactiveChooser = int(input('Which mode you would like to use? \nType 1 for interactive mode \nType 0 for non interactive \nEnter a number: '))

    if interactiveChooser == 1:
        print('Interactive mode chosen')
        interactive()
    elif interactiveChooser == 0:
        # nonInteractive()
        print('Non interactive mode chosen')
    else:
        print('Type 1 or 0 please! \n')
        main()

def interactive():
    variables = ['a', 'b', 'c']
    nums = []
    k = 0
    while k < len(variables):
          temp = 0
          temp = input(f'Number {variables[k]}: ')
          if not temp.isdigit(): 
            print(f'Error. Expected a valid real number, got {temp} instead')
          else:
            nums.append(int(temp))
            k += 1

    def quadratic(a, b, c):
        discrim = b ** 2 - 4 * a * c
        if discrim < 0:
            print( f'Equation is: {a}x^2 + {b}x + {c} = 0 \nThere are 0 roots' )
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

    quadratic(nums[0], nums[1], nums[2])

# def nonInteractive():

main()
