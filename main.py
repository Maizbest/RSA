import gcd
import random
import time

def randomInt(upper: int):
  return randomInt(0, upper)

def randomInt(lower: int, upper: int):
  return int(random.random() * (upper - lower)) + lower

def generatePrime():
  q = 1
  while(not gcd.isPrime(q)):
    q = randomInt(1**10, 2**10)
  return q

q = generatePrime()
p = generatePrime()
while(q == p):
  p = generatePrime()

n = q * p
print("Choosen primes: ", q, p)

qp = (q - 1) * (p - 1)
e = 1;
while(e == 1 or gcd.gcd(e, qp) != 1):
  e = randomInt(qp // 2, qp)
publicKey = (e, n)
print("Public key is ", publicKey)

(d, t, g) = gcd.pulverizer(e, qp)
if (d < 0): d += qp 
print("Private key is ", d)

message = "Hello world!"
start =  time.process_time() 
encrypted = [c**e % n for c in [ord(c) for c in message]]
print("Time consumed for encryption, seconds: ",  time.process_time() - start)
print("Encrypted message: ", encrypted)

start =  time.process_time() 
decrypted = [c**d % n for c in encrypted]
print("Time consumed for decryption, seconds: ",  time.process_time() - start)
print("Decrypted message:", "".join([chr(c) for c in decrypted]))


