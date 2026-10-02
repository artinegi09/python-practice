# Single line Comments
# Data Types
'''
Multiline Comment

1 byte = 8 bits -> [1,1,1,1,1,1,1,1] -> 256 numbers = 2^8

0   [0000 0000]

255 [1111 1111]

2 byte = 2*8 = 16 bits -> 2^16
4 byte = 4*8 = 32bits -> 2^32
[28 bytes] = 28*8 = 224 -> 2^224

int -> -6768 , 0 , 6868667773764876387268476238468234 

char -> 'h' ,'0', '8', ' ', '\n', '', '-'

string -> "Anurag Negi"
        -> "My name is Anurag Negi, I am a Software Engineer. "
'''
# array , dictionary, map,

x = 1080
print(x)
x = 80
print(x)


import sys

print(f"Integer (0): {sys.getsizeof(0)} bytes")
print(f"Float (0.0): {sys.getsizeof(0.0)} bytes")
print(f"Boolean (True): {sys.getsizeof(True)} bytes")
print(f"Empty String: {sys.getsizeof('')} bytes")
print(f"Empty List: {sys.getsizeof([])} bytes")

# Variables, Values, Types
a = -89
b = -78.9
c = True
d = "My name is anurag Negi"
e = [1,2,3,5,10,"Anraug",False,"Mohan",-89.89]
print(a)
print(b)
print(c)
print(d)
print(e)

# Operations
# add,sub,mul,div,mod,
# and,or,not

x = 45
y = 12

add = x+y
sub = x-y
mul = x*y
div = x/y
mod = x%y

print("-------------------------------")
print(add)
print(sub)
print(mul)
print(div)
print(mod)

val1 = True
val2 = False

print("-------------------------------")
print(val1 and val2) #False
print(val1 or val2)  #True
print(not val1)      #False
print(not val2)      #True

'''
A = PRT/100
fun(x) -> x^2 + 56x- 6 -> y

'''