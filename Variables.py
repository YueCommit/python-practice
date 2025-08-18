my_boolean = True
my_int = 42
my_float = 3.14159
my_string = "Assess"
my_string2 = "Education"
my_multi_line_sting = ''''
Assess
Education 
Advance
'''''

print(my_boolean)
print(my_multi_line_sting)

print(type(my_boolean))


# Calculate the result of the expression:
# (52 - 52) + (64 / 8) + the remainder of 42 / 8
result = (52 - 52) + (64 / 8) + (42 % 8)
print(result)


# Set up Our variables
num1 = 3.14
num2 = 2
num3 = 16.00

#Create some expressions and store their results
add_result = num1 + num2
subtract_check = num2 - num1
divide_check = num3 / num2
exponent_result = num3 ** num2
remainder_result = num3 % num2
greater_than_check = num1 > num2
multiple_ops_check = round((divide_check * 5) ** num1, 2)

#print results

print(add_result)
print(subtract_check)
print(divide_check)
print(exponent_result)
print(remainder_result)
print(greater_than_check)
print(multiple_ops_check)