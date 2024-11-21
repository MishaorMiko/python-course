x=0
while True:
  number1 = float(input('print a number1:'))
  operation =str(input('print a operation:'))
  number2 = float(input('print a number2:'))
  x+=1
  if x==3:
      break
  elif operation=="+":
        print( "eki san kosyndisy:", number1+number2)
  elif operation=="-":
        print('eki san азайтындысы',number1-number2)
  elif operation=="*":
        print(number1*number2)
  elif operation=="/":
        print(number1/number2)
  elif operation=="**":
        print(number1**number2)
  elif operation=="%":
        print(number1%number2)
  elif operation=="//":
        print(number1//number2)
  elif operation=="**/":
        print(number1**(1/number2))
  else:
        print('error')
