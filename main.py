def main():
    x = int(input('Enter your input: '))
    y = int(input('Enter your input: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    if x > 0:
        if y > 0:
            quadrant = 1
        elif y < 0:
            quadrant = 4
    elif x < 0:
        if y > 0:
            quadrant = 2
        elif y < 0:
            quadrant = 3

    print(f'Quadrant: {quadrant}')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
