# 5️⃣ Simple Calculator

# Write a program that:
# 	•	Takes two numbers
# 	•	Takes an operator (+, -, *, /)
# 	•	Performs the operation
# 	•	Prints the result

num_01 = int(input("Enter 1st number: "))
num_02 = int(input("Enter 2nd number: "))

op = input('Select operator: +,-,*,/  ')

if (op == '+'):
    print(f'sum = {num_01+num_02}')
elif (op == '-'):
    print(f'sub = {num_01-num_02}')
elif (op == '*'):
    print(f'mul = {num_01*num_02}')
elif (op == '/'):
    print(f'divide = {num_01/num_02}')
else:
    print('Please select correct operator...')