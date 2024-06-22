
def calculate(num1,num2,op):
    if op=='+':
        result =num1+num2
    elif op =='-':
       result =num1-num2
    elif op =='*':
        result =num1*num2
    elif op =='/':
        result =num1/num2
    elif op =='^':
        result = num1**num2
    return result

continue_calculating = True
while continue_calculating is True:

   number1= float(input('Enter first number: \n'))
   op =input('Enter Operator(+,-,*,/,^):\n')
   number2=float(input('Enter second number:\n'))
   result= calculate(number1,number2,op)
   print('=',result)
   yes_or_no = input('Do you want to continue?(y/n):')
   if yes_or_no == 'n':
      continue_calculating = False
      print("Thank You")


