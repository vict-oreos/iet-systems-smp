from math import gcd
def gcd1(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=gcd1(b,a%b)
    x=y1
    y=x1-(a//b)*y1
    return g,x,y
def inverse(e,phi):
    g,x,y=gcd1(e,phi)
    if g!=1:
        raise Exception("Modular inverse does not exist")
    return x%phi
def gkeys():
    p=67
    q=19
    n=p*q
    phi=(p-1)*(q-1)
    e=17
    if gcd(e,phi)!=1:
        raise Exception("e and phi are not coprime")
    d=inverse(e,phi)
    return p,q,n,phi,e,d
def encrypt(message,e,n):
    return [pow(ord(char),e,n) for char in message]
def decrypt(text,d,n):
    return ''.join(chr(pow(char,d,n)) for char in text)
p,q,n,phi,e,d=gkeys()
print("p =",p)
print("q =",q)
print("n =",n)
print("e =",e)
print("d =",d)
message="HELLO"
print("Encrypted:",encrypt(message,e,n))
print("Decrypted:",decrypt(encrypt(message,e,n),d,n))