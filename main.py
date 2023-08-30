import time

num1 = 0
num2 = 0
while True:
  try:
          num1 = int(input("Enter First Number: "))
          num2 = int(input("Enter Second Number: "))
  except ValueError:
     print("That's not a number! Please wait. ")
     time.sleep(3)
     continue
  else:
     print('Got It')
     break
    

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("That's not a allowed operation. ")

print(num1, ch , num2, ":", result)

ae = input("Are you satisfied with your experience?")
if ae == 'Yes':
    print('<3 Thank you!')
    print('Made by Benjamin Kim')
else :
    print('Made by Benjamin Kim')
    
