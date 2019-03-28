#%% [markdown]
# # Introduction to Python
#%% [markdown]
# The program was introduced by Guido von Rossum in 1990 and Python 3 was released in 2008
#%% [markdown]
# * Low Level vs high-level 
# * General vs targeted to an application domain
# * Interpreted vs compiled
#%% [markdown]
# ## Basic Elements
# 
# A Python **program** is a sequence of definitions and commmands. The definitions are evaluated by the interpreter and the commands executed in the shell
# 
# A **command**, often called a **statement**, instructs the interpreter to do something

#%%
print("I am a command, print me!!")

#%% [markdown]
# ## Objects, expressions, and numerical types
# 
# **Objects** are the core thing that Python programs manipulate. Every Object has a **type** that define the kind of things that the program can do with the object. 
# 
# * Types are either scalar or non-scalar. **Scalar** objects are indivisible.
# * Python uses four types of scalars: *int*, *float*, *bool*, *None*
# * Objects and **operators** can be combined to form **expressions**, each of which denotes and object of some type
# 
# The operator == is used to test if two expressions are equal, and the != operator is used to test if two expressions are unequal.
# 
# The built-in Python function **type** can be used to test the type of an object

#%%
y = 5.0 + 5.0
print(type(y))
type("abc")


#%%
type(3)


#%%
type("a,b,c")

#%% [markdown]
#  The operators on types **int** and **float** are:
#  * i+j
#  * i-j
#  * i * j
#  * i//j (integer division)
#  * i/j 
#  * i%j (modulus operator)
#  * i**j
#  
#  The operators in type **bool** are:
#  * **a and b**
#  * **a or b**
#  * **not a**
#%% [markdown]
# ## Variables and assignment
# 
# **Variables** provide a way to associate names with objects

#%%
pi = 3.14
radius = 11.2
area = pi*(radius**2)
radius = 14.3
print(area)
area = pi*(radius**2)
print(area)

def area(radius):
    pi = 3.14
    return pi*(radius**2)

#%% [markdown]
# First, two **float** objects are bound to names *pi* and *radius*. Then, the name *area* is bound to another **float**. Finally, radius is bound to another **float** object
# 
# **IMPORTANT**
# In python **a variable is just a name**. An assignment statement associate the name to the left of the = symbol with the object denoted by the expression to the right. 
# 
# ** An object can have one, more than one, or no name associated to it**
# 
# It is critically important to write programs that are easy to read, for example

#%%
a = 3.1415; 
b = 11.2; 
c = a*(b**2)

pi = 3.1415
diameter = 11.2
area = pi*(diameter**2)

#%% [markdown]
# For Python, both expressions are the same. For a humam reader, however, they are quite different. 
# 
# Another way to improve the readability of the code is to add comments. Text following the symbol # is not interpreted by Python

#%%
pi = 2
radius = 5
side = 4
# Substract area of the square s from area of circle c
areaC = pi*radius**2 # Esto es un comentario
# hola
areaS = side*side
difference = areaC-areaS

#%% [markdown]
# Python allows multiple assignment, such as:

#%%
x, y = 2, 3
x, y = y, x
print("x = ",x ,", y = ",y)

#%% [markdown]
# ## Branching Programs
# 
# So far we have seen **straight-line programs**. They execute one statement after another in the order in which they appear, and stop when they run out of statemnets.
# 
# **Branching** programs are more interesting. The simplest branching statement is a **conditional**       

#%%
if boolean expression:
    block of code
else:
    block of code

#%% [markdown]
# Consider de following program:

#%%
x = 5
if x%2 == 0:
    print("Even")
else:
    print("Odd")
print("Done with conditional")

#%% [markdown]
# **Indentation** is semantically meaningful in Python. Additionally, when either the true block or the false block of a conditional contains another conditional, the conditional statement are said to be **nested**

#%%
x = 1
y = 3
z = 1

if x < y:
    if x < z:
        print("x is least")
    else:
        print("x is second")
else:
    print("x is first")


#%%
if x < y and x < z:
    print("x is least")
elif y < z:
    print("y is least")
else:
    print("z is least")

#%% [markdown]
# ## Type and Input

#%%
type("a")


#%%
type(3*4.6)


#%%
type({})


#%%
type([])

#%% [markdown]
# **Indexing** can be used to extract individual characters from a string or list. **Slicing** is used to extract substrings of arbitrary length
#%% [markdown]
# ### Input
# 
# Python 2 had two functions that could be used to get input directly from a user, *input* and *raw_input*. In Python 3 just the former can be used

#%%
name = input('Enter your name: ')
print("Are you really, ", name,'?')


#%%
n = input("Enter an int: ")
#print(type(n))
if type(n) == int:
    print(n," is an integer")
else:
    print(n," is NOT an integer")

#%% [markdown]
# **Type conversions** (also called **type casts**) are used often in python code

#%%
n = float(input("Enter an int: "))
if type(n) == float:
    print(n," is a float")
else:
    print(n," is NOT an integer")

#%% [markdown]
# ## Iteration
#%% [markdown]
# The **iteration** mechanism, like a conditional statement, begins with a test. If the test evaluates to TRUE, the program executes the loop body once, and then goes back to reevaluate the test. The process is reapeated until the test evaluates to FALSE

#%%
x = 10
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

#%% [markdown]
# # Simple Numerical Problems
#%% [markdown]
# Now is the time to combine simple Python constructs to write some simple programs
#%% [markdown]
# ## Exhaustive Enumeration
#%% [markdown]
# Consider de problem of printing the integer cube root, if it exist, of an integer

#%%
# Find de cube root of a perfect cube
x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("cube root of "+ str(x) +" is "+ str(ans))

#%% [markdown]
# The problem above will terminate for ALL integers. Whenever you write a loop, you should think about an appropriate **decrementing function**. This is a function that has the following properties
# 
# * It maps a set of program variables into an integer
# * When the loop is entered, its value is nonnegative
# * When its value is <= , the loop terminates
# * Its value is decreased every time through the loop
# 
# In the previous problem the function was abs(x)-ans**3
# 
# Just for fun, try the executing the code

#%%
max = int(input("Enter a positive integer: "))
i = 0
while i < max:
    i = i + 1
    print(i)

#%% [markdown]
# ## For Loops
# 
# The while loop is highly stylized. The **for** loop can be used to simplify programs containing this kind of highly stylized iteration

#%%
for variable in sequence:
    code_block

#%% [markdown]
# Inside the for loop the process continues until the sequence is exhausted or a **break** statement is executed within the code block.
# 
# Consider the code

#%%
x = 10
for i, j in enumerate(range(5,x)):
    print("i=",i, "j=",j)

#%% [markdown]
# Now think about the code

#%%
x = 4
for i in range(x):
    print(i)
    x = 5

#%% [markdown]
# The *range* function in the line with *for* is evaluated just before the first iteration of the loop, and not reevaluated for subsequent iterations

#%%
x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2

#%% [markdown]
# Reimplementing the cube root procedure

#%%
# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
for ans in range(abs(x)+1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print (x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of "+ str(x), " is "+str(ans))

#%% [markdown]
# ## Approximate Solutions and Bisection Search
#%% [markdown]
# What happen if we had to find the square root of 2?? The value is not a rational number. The right thing to do is to ask the program to find an **approximation** to the square root. You should try to find and answer that is "close enough" (within some *epsilon*) of the actual number

#%%
x = 0.25 # Try 0.25 What happens?
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print("numGuesses = ", numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of ',x)
else:
    print(ans , " is close to square root of ", x)


#%%
x = 0.25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1,x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print("low = ", low, "high = ", high, " ans = ", ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print("numGuesses = ", numGuesses)
print(ans ," is close to square root of ",x)
        

#%% [markdown]
# ## Few words about using Floats
# 
# Some times numbers of type **float** do not produce good approximation to real numbers. See the following example

#%%
x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, "= 1.0")
else:
    print(x, "is not 1.0")
    print(x == 10.0*0.1)

#%% [markdown]
# for these reason it is better to  write abs(x-y) < 0.0001 rather than x == y
#%% [markdown]
# ## Newton-Raphson
# 
# A **polynomial** with one variable is either zero or the sum of a finite number of nonzero terms (e.g. $3x^2 + 2x +3$). A **root** of the polynomial p is a solution to the equation p = 0. So, of example te problem of finding an approximation to the square root of 24 can be formulated as finding an x such that $x^2 - 24 = 0$
# 
# Newton proved a theorem that implies that if a value, call it guess, is an approximation to a root of a polynomial, then **guess - p(guess)/p'(guess)**, is a better approximation.

#%%
# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.0001
y = 45
guess = y/2.0
while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
print("Square root of ", y, " is about ", guess)

#%% [markdown]
# # Functions and Abstraction by Specification
#%% [markdown]
# So far, we have introduced numbers, assignments, input/output, comparisons, and looping. How powerfull if that?? In a theoretical sense, it is as powerful as you will ever need. Such lenguages are called **Turing Complete**. The pieces of code we have seen lack of general utility. The most important **linguistic** feature provided by Python to generalize and reuse the code is the **function**.
# 
# In Python each **function definition** is of the form

#%%
def functionName(formalParamters):
    functionBody

#%% [markdown]
# The function max_ can be expressed by

#%%
def max_(x, y):
    if x > y:
        return x
    else:
        return y

#%% [markdown]
# The sequence of names (x, y in this example) within the parentheses following the function name are the **formal parameters** of the function. when the function is used, the **actual parameters** are bound to the formal parameters. The **return** statement can be used only within the body of a function

#%%
max_(7,9)

#%% [markdown]
# ## Keyword arguments and Default Values
# 
# In Python there are two ways that formal parameters get bound to actual parameters. The most common method is the **positional method**. The first formal is bounded to the first actual, the second formal to the second actual and so on. Python also support **keyword arguments** in which formals are bound to actuals using the name of the formal parameter

#%%
def printName(firstName, lastName, reverse=False):
    if reverse:
        print(lastName + "," + firstName)
    else:
        print(firstName, lastName)


#%%
printName("Olga","Toro", False)
printName("Olga", "Toro", True)
printName("Olga", "Toro", reverse=False)
printName("Olga", lastName="Toro")


#%%
printName("Olga", lastName="Toro", reverse=False)

#%% [markdown]
# Keyword arguments are commonly used in conjunction with default parameter values

#%%
def printName(firstName, lastName, reverse = False):
    if reverse:
        print(lastName + "," + firstName)
    else:
        print(firstName, lastName)

printName("Olga", lastName="Toro")
printName("Olga", lastName="Toro", reverse=True)

#%% [markdown]
# ## Scoping
# 
# Let's look at another small example

#%%
def f(x):
    y = 5
    x = x + y
    print("x =", x)
    return x

x = 3
y = 2
z = f(x)
print("z =", z)
print("x =", x)
print("y =", y)

#%% [markdown]
# It is important to note that though the actual and formal parameters have the same name, they are not the same variable. Each function define a new **name space**, also called a **scope**. The formal parameter x and the **local variable** y exist only within the scope of the definition of f

#%%
def f(x):
    def g():
        x = "abc"
        print("x =", x)
    def h():
        z = x
        print("z =", z)
    x = x + 1
    print("x =", x)
    h()
    g()
    print("x =", x)
    return g

x = 3
z = f(x)
print("x =", x)
print("z =", z)
z()

#%% [markdown]
# ## Specifications
# 
# For inexperienced programmers writting a function such as **testFindRoot()** seems a waste of time. Experienced programmers know that this additional effort pays back.
# 
# A **specification** of a function defines a contract between the implementer and those who will be writting programs that use that function. The contract can be thought as containing two parts
# 
# * **Asumptions:** Describe conditions that must be met by the users of the function. Typically, they describe constraints on the actual parameters
# 
# * **Garantees:** Describe conditions that must be met by the function, provided that it has been called in a way that satisfies the assumptions
# 
# Thus, it is easy to see that a function provides both **decomposition** and **abstraction**

#%%
def findRoot(x, power, epsilon):
    """
    x and epsilon int or float, power an int,
    epsilon > 0 & power >=1
    returns float y such that y**power is within epsilon of x.
    If such a float does not exist, it returns None
    """
    if x < 0 and power%2 == 0:
        return None
    low = min(-1.0, x)
    print(type(x))
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1,4):
            print('Testing x = ' + str(x) +
                  ' and power = '+ str(power))
            res = findRoot(x, power, epsilon)
            if res == None:
                print("No root")
            else:
                print(' ' + str(res**power) + '~=' + str(x))
                
testFindRoot()
help(findRoot)

#%% [markdown]
# ## Recursion
# 
# In general a recursive definition is made up to two parts. There is at least one **base case** that directly specifies the results for a special case, and there is at least one **recursive (inductive) case** that defines the answer in terms of the answer to the question on some other input, typically a simpler version of the same problem.
# 
# The classic example is the *factorial function*
# 
# 1! = 1
# 
# (n + 1) != (n + 1) n!
# 
# where the first equation defines the base case and the second defines the factorial for all natural numbers, except the base case.

#%%
def factI(n):
    """
    Assumes that n is an int > 0
    returns n!
    """
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

def factR(n):
    """
    Assumes that n is an int > 0
    returns n!
    """
    if n == 1:
        return n
    return n*factR(n-1)

print(factI(100))
print(factR(100))

#%% [markdown]
# ### Fibonacci Numbers
# 
# The growth in rabbits population is described naturally by the **recurrence**
# 
# * females(0) = 1
# * females(1) = 1
# * females(n+2) = females(n+1) + females(n)

#%%
def fib(n):
    """
    Assumes n an int >= 0
    Returns Fibonacci of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print("fibonacci of ", i, '=' ,fib(i))
        
testFib(5)

#%% [markdown]
# ## Global Variables
#%% [markdown]
# Suppose we want to know how many recursive calls are made. We can add some code that counts the number of calls. Onw way to do it is using **Global Variables**

#%%
def fib(n):
    """
    Assumes n an int >= 0
    Returns Fibonacci of n
    """
    global numCalls
    numCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print("fibonacci of ", i, '=' ,fib(i))
        print('fibonacci called', numCalls, 'times')
        
testFib(35)

#%% [markdown]
# ## Lambda Functions

#%%
mult3L = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def filterfunc(x):
    return x % 3 == 0

mult3N = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(mult3L))
print(list(mult3N))


#%%
def filterfunc(x):
    return x % 3 == 0
mult3 = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])


#%%
f = lambda x, y : x + y
print(f(2,3))

def f(x,y):
    return x+y

print(f(2,3))


#%%
def transform(n):
    return lambda x: x + n

f = transform(3)
f(4)

#%% [markdown]
# # Import Modules and External data

#%%
import numpy as np
help(np.arange)
arang = np.arange(10)
arang


#%%
import pandas as pd
data = pd.read_csv('D:/Forestal Projects/Base.csv', sep=",", )


#%%
print(type(data))
data.head()


