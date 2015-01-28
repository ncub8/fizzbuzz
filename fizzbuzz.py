n = 200
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