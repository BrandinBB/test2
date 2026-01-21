calc_type = str(input('''Choose Option
1 - Addition
2 - Subrtract
Choice = '''))

num1 = float(input('Type first number '))
num2 = float(input('Type second number '))

if calc_type == '1':
    result = (num1 + num2)
if calc_type == '2':
    result = (num1 - num2)

print ('Resulting calculation = ' + str(result))