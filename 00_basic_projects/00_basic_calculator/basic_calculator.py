"""Module providing a function of basic calculator."""
# Basic Math Calculator Application - [Assignment 03]
print('Basic Math Calculator')

a: int = int(input("Enter Value for A: "))
b: int = int(input("Enter Value for B: "))

print('Received values of A = %d _________ B = %d' % (a,b))
# string manipulation with old method modulus %d, %s, %f
print('_______________________________________________')

# simple string concatination method
print("Addition of [A+B]: ", a+b)

# string format method writing sequence number is optional.
print("Subtraction of [A-B]: {}".format(a-b))

# string manipulation with latest f-string
print(f"Division of [A/B]: {a/b}")
print(f"Multiplication of [A*B]: {a*b}")

print('_______________________________________________')
print('Credits: Muhammad Osama Github @codewithosama Email: imosamamumtaz@outlook.com')
