import sys

if len(sys.argv) > 1:
  try:
    n=int(sys.argv[1])
  except ValueError:
    try: 
      n=int(raw_input("Numeric value not entered. Enter a number: "))
    except ValueError:
      print("Sorry that was a non-numeric value, setting n to 100")
      n = 100
else:
  try:
    n=int(raw_input("Enter a number: "))
  except ValueError:
    try: 
      n=int(raw_input("Numeric value not entered. Enter a number: "))
    except ValueError:
      print("Sorry that was a non-numeric value, setting n to 100")
      n = 100

print "Fizz buzz counting up to " + str(n)

for num in range(1,n):
  if (num%3 == 0) and (num%5 == 0):
    print("fizzbuzz")
  elif num%3 == 0:
    print("fizz")
  elif num%5 == 0:
    print("buzz")
  else:
    print(num)