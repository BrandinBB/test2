import operator # this code is needed to define a variable as an arithmatic operator ex operator.add

#using triple quote for multi line input menu
calc_type = str(input('''Choose Option
1 - Addition
2 - Subtract
3 - Multiply
4 - Divide
Choice = '''))

if calc_type == '1': #This is to set the variable for the result calculation
    calc_operator = operator.add
if calc_type == '2':
    calc_operator = operator.sub
if calc_type == '3':
    calc_operator = operator.mul
if calc_type == '4':
    calc_operator = operator.truediv

num1 = float(input('Type first number ')) #set the number variables per user input
num2 = float(input('Type second number '))

result = calc_operator(num1, num2) #calculate result and set to variable result

print ('Resulting calculation = ' + str(result))