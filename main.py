number1=float(input('print a number:'))
number2=float(input('print a number:'))
operation=int(input('print a number of operation:'))
if operation==1:
  print(number1+number2)
elif operation==2:
  print(number1-number2)
elif operation==3:
  mult=number1*number2
  print(mult)
elif operation==4:
  print(number1/number2)
elif operation==5:
  print(number1**number2)
elif operation==6:
  print(number1%number2)
elif operation==7:
  print(number1//number2)
elif operation==8:
  print(number1**(1/number2))
else:
  print('error')