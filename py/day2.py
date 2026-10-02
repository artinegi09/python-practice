
def square(a):
    return a*a

def cube(a):
    return square(a)*a

# function definition
# name of funtion -> Amount
# parameters of function -> P, R,T
# return value -> A

def SI(P,R,T):
     A = (P * R * T)/100
     return A

def Amount(P,SI):
    return P+SI 


P = 100
R = 5
T = 4

si = SI(P,R,T)
amt = Amount(P,si)

print(amt)
print(si)


# val = square(56)
# print(val)  

# val2 = cube(56)
# print(val2)  