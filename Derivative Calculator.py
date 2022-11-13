input_function = input('What function would you like to differentiate? ')
input_function = input_function.replace(' ', '')
function = input_function.split('+')

power = []  # two empty lists, one for the coefficients and one for the exponents so that when these values are found
co = []                                                                # they can be appended into each specific list

for func in function:
    if func.count('^') == 0:  # checks for a caret, which thus checks if there is an exponent present
        if func[:func.index('x')] == '':
            coefficient = str(1)  # if there is no coefficient it sets it = 1 and appends it to the list
            co.append(coefficient)
        if func[:func.index('x')] == '-':
            coefficient = str(-1)
            co.append(coefficient)
        else:
            coefficient = func[:func.index('x')]  # however if there is a coefficient it appends that to the list
            co.append(coefficient)
        for i in func:
            if i == 'x':  # when there is no caret, thus no exponent, it sets the power = 1
                pow_dne = 1
                power.append(pow_dne)  # appends it to the power list
    else:  # this is for when there is an exponent
        if func[:func.index('^') - 1] == '':  # this deals with when there is no coefficient and sets it = 1
            coefficient = 1
            co.append(coefficient)  # appends this to the list of coefficients
        else:
            coefficient = func[:func.index('^') - 1]  # however here, this is for when there is a coefficient
            co.append(coefficient)  # then, that value is appended to the coefficient list
        for i in func:
            if i == '^':
                if func[func.index('^') + 1] == '(':  # this is for when the exponent input is in parentheses
                    start = func.index('(') + 1  # a range is used, produced in terms of the index of the parentheses
                    try:
                        end = func.index(')')  # when the user forgets a closing bracket an error message alerts them
                    except:
                        print('OOPS! ERROR: did you forget a closing bracket?')
                        continue
                    power.append(func[start:end])  # once the index of the parentheses is found it isolates the exponent
                else:                                                                 # and appends it to the power list
                    pow_sing = func[func.index('^') + 1]  # this is for when the exponent is not in parentheses
                    power.append(pow_sing)

print(co)
print(power)

d_final = []  # this is an empty list for the derivative of each separate function

for y in range(len(power)):  # a for loop relative to the length of the power list is used to differentiate specific
    if int(power[y]) - 1 == 1:                                           # circumstances of exponents in derivatives
        derivative = f'{int(co[y]) * int(power[y])}x'  # this is for when the exponent of the derivative is 1
        d_final.append(derivative)
    elif int(power[y]) - 1 == 0:
        derivative = f'{int(co[y]) * int(power[y])}'  # this is for when the exponent of the derivative is 0, thus the x
        d_final.append(derivative)                                                                     # term disappears
    else:
        derivative = f'{int(co[y]) * int(power[y])}x^{int(power[y]) - 1}'  # and this is for when the exponent of the
        d_final.append(derivative)                                             # derivative is not 0 or 1 (most cases)
print(d_final)
print(*d_final, sep=' + ')  # This final line is to separate each derivative in the list and insert a '+' in between
# each to ensure that the original format of the input function is maintained
