def gcd(a: int, b: int):
  (x, y, e) = (a, b, 1)
  while(x != y):
    if (x % 2 == 0 and y % 2 == 0):
      (x, y, e) = (x >> 1, y >> 1, e << 1)
    elif (x % 2 == 0):
      x = x >> 1
    elif (y % 2 == 0):
      y = y >> 1
    elif (x > y):
      x = x - y
    else:
      y = y - x
  return e * x

def pulverizer(a: int, b: int) -> (int, int):
  (x, y, s1, t1, s2, t2, c) = (a, b, 1, 0, 0, 1, 1)
  while(x != y):
    if (x % 2 == 0 and y % 2 == 0):
      (x, y, c) = (x >> 1, y >> 1, c + 1)
    elif (x % 2 == 0):
      if (s1 % 2 == 0 and t1 % 2 == 0):
        (x, s1, t1) = (x >> 1, s1 >> 1, t1 >> 1)
      else:
        (x, s1, t1) = (x >> 1, (s1 - b) >> 1, (t1 + a) >> 1)
    elif (y % 2 == 0 or y > x):
      (x, y, s1, t1, s2, t2) = (y, x, s2, t2, s1, t1)
    else:
      (x, y, s1, t1, s2, t2) = (x - y, y, s1 - s2, t1 - t2, s2, t2)
  return (s1, t1, x)

def isPrime(a: int):
  if (a == 0 or a == 1):
    return False
  for i in range(2, a // 2 + 1):
    if(a % i == 0):
      return False
  return True

def __gcd(a: int, b: int, e = 1):
  if (a == 0):
    return e * b
  elif (b == 0):
    return e * a
  if ((a % 2 == 0) and (b % 2 == 0)):
    return __gcd(a >> 1, b >> 1, e << 1)
  elif ((a != 0) and (a % 2 == 0)):
    return __gcd(a >> 1, b, e)
  elif ((b != 0) and (b % 2 == 0)):
    return __gcd(a, b >> 1, e)
  elif (a > b):
    return __gcd(a - b, b, e)
  elif (a <= b):
    return __gcd(b - a, a, e)
