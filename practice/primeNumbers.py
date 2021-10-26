def primeCheck(num):
  if num == 2 or num == 3:
      return True
  if num < 2 or num%2 == 0:
      return False
  if num < 9:
      return True
  if num%3 == 0:
      return False
  a = int(num**1/2)
  b = 5
  while b <= a:
    if num%b == 0:
        return False
    if num%(b+2) == 0:
        return False
    b=b+6
  return True

def divisors(num):
    for i in range(2,num):
        if num%i == 0:
            print(i, end=',')
    print('')

print(primeCheck(15))
print(primeCheck(2))

divisors(1024)