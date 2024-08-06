"""Module providing a function printing python version.""" #why we use this?
# Data Types
# String                    |    str
# Integer                   |    int
# Boolean                   |    bool
# Floating Point Numbers    |    float

name:str = 'Muhammad Osama'
age:int = 23
status:bool = False
height:float = 5.6
bio:str = '''My paragraph falls their for storage ad est aliqua deserunt. Excepteur laborum fugiat esse reprehenderit ex esse sit ut occaecat officia Lorem. Amet tempor consectetur Lorem excepteur labore. Anim nostrud reprehenderit exercitation non esse incididunt culpa eiusmod laborum do exercitation occaecat cillum. Labore dolor pariatur consequat ad nulla ex et aliquip sit anim. Eiusmod anim nisi labore est tempor id dolor occaecat duis mollit pariatur officia. Aliquip esse amet tempor nulla culpa cillum magna sunt aliqua ex tempor cillum incididunt.'''

print('My age is', name)
print('My height is', height)
print('My status is', status)
print('My paragraph:\n', bio)

# strip methods examples
print('1.','     My age is   ', '24')
print('1.','     My age is   '.lstrip(), '24')
print('1.','     My age is   '.rstrip(), '24')
