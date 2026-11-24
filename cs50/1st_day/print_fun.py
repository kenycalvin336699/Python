name = input("What is your name? ")
print("hello,", name) # or you can do ptint("hello, " + name)

# but the best way to write string variables is 
print(f"hello, {name}") # using fstring or f <- best thing *****

'''
one more thing 
Using + like print("hello, " + name)
only works if name variable is string either python throw error 
in short + only work if both are strings or same data type either use (collon)

the thing is that + inside print function shows taht it is one argument 
("hello, " + name) <- this is one argument adding two string "hello, " and name
but 
("hello,", name) <- this is two argument "hello" and name which is saprated by ,(collon)
'''

# notes or commants
'''
print(*objects, sep=' ', end='\n', file=None, flush=False)

this is how print function look like 
objects mean strings datatype or whatever user want to print like "hello," and name here
sep=' ' show when you sapratte paremeter with , it by default add space and end = '\n' add new line 
at the end of the function by default you can over write it
use \ for print escape character like @ "" etc ... like that
python("my name is \"keny\""")
prints 
my name is "keny"
'''

print("hello, ", end = 'end over written ')
print(name)

print("hello, ", name, sep='sepration over written ')
