def isEven_or_isOdd(x):
    if type(x) != int:
        print('not a number')
    elif x % 2 == 0:
        print('even')
    else:
        print('odd')

isEven_or_isOdd('g')