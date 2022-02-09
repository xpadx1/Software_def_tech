import sys
import math

def main():
    interactiveChooser = input('Which mode you would like to use? \nType 1 for interactive mode \nType 0 for non interactive \nEnter a number: ')

    if interactiveChooser == '1':
        print('Interactive mode chosen')
        interactive()
    elif interactiveChooser == '0':
        print('Non interactive mode chosen')
        nonInteractive()
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
          if temp.lstrip("-").isdigit() or temp.isdigit(): 
            nums.append(int(temp))
            k += 1
          else:
            print(f'Error. Expected a valid real number, got {temp} instead')

    quadratic(nums[0], nums[1], nums[2])

def nonInteractive():
    fh = open('file.txt', "r")
    content = fh.read()
    result = content.split(' ')
    finalValues = []
    k = 0
    while k < len(result):
        if result[k].lstrip("-").isdigit() or result[k].isdigit():
            finalValues.append(int(result[k]))
            k += 1
        else: 
            print ('Invalid value')
            return
    
    if len(finalValues) == 3:
        quadratic(finalValues[0], finalValues[1], finalValues[2])
    else:
        print('Invalid input')


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

main()


    # result = []
    # k = 0
    # while k < 1:
    #     args = 0
    #     args = input('Enter your argument: ')
    #     if args.lstrip("-").isdigit() or args.isdigit():
    #         result.append(int(args))
    #         k += 1
    #     else:
    #         print(f'Error. Expected a valid real number, got {args} instead')