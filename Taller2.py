#%% [markdown]
# # Structured Types, Mutability, and Higer-Order Functions
# 
#    So far the programs we have seen dealt with three types of object **int, float, and str**. Int and float are type scalar, which means they have no internal accessible structure. On the other hand, str object can be thought as structured object (non scalar) since one can index to extract and individual. Now, we are going to introduce three structured types **tuple, list, dict**
#%% [markdown]
# ## Tuples
# 
#    These are ordered sequences of elements, the difference is that the elements of a tuple need not to be characters, they can be of any type. They are written by enclosing a comma-separated list of elements within parentheses

#%%
t1 = ()
t2 = (1,'two', 3)

#%% [markdown]
# Which of these is a *tuple* and why??

#%%
tuple1 = (1)
tuple2 = (1,)
print(type(tuple1))
print(type(tuple2))

#%% [markdown]
# Like strings, tuples can be concatenated, indexed, and sliced

#%%
t1 = (1, "two", 3)
t2 = (t1, 2.25)
print(t2)
print((t1+t2))
print((t2+t1))
print((t1+t2)[3])
print((t1+t2)[2:5])

#%% [markdown]
# A for statement can be used to iterate over the elements of a tuple
#%% [markdown]
# ### Sequence and multiple assignment
# 
# If you know the length of a sequence, it can be convenient to use Python's multiple assignment statement to extract the individual elements

#%%
x, y = (3, 4)
a, b, c = 'xyz'
print(a)

def do_something(x,y):
    '''
    x and y must be either float or integers
    return x+1 and y**2
    '''
    return (x+1, y**2)
no_separado = do_something(3,4)
m, n = do_something(3,4)
print(m)
print(n)
print(no_separado)

#%% [markdown]
# ## Lists and Mutability 
# 
# Like a tuple, a list is an ordered sequence of values where each value is identified by an index. The syntax to express literals of type list is similar to that used for tuples. The diference is that we use squared brackets insted of parenthesis

#%%
L = ['I did it all', 4, 'love', [1,2,3]]
for i in range(len(L)):
    print(L[i])

#%% [markdown]
# what do you obtain from the following piece of code

#%%
[1,2,3,4][1:3][1]

#%% [markdown]
# List differ from tuples in a HUGELY important way: lists are **mutable**. The types, tuple, int, float, and str are all **immutable**. The big difference is that variables of **inmutable** type cannot be modified after creation.
# 
# Remember that in Python a variable is just a name, a label that can be attached to an object. Por ejemplo:
#     

#%%
Tech = ["MIT", "Caltech"]
Ivys = ["Harvard", "Yale", "Brown"]

#%% [markdown]
# The the assignment statements

#%%
Univs = [Tech, Ivys]
Univs1 = [["MIT", "Caltech"],["Harvard", "Yale", "Brown"]]
print(Univs)
print(Univs1)
print(Univs == Univs1)

#%% [markdown]
# For the naive, it appears that Univ and Univ1 are binded to the same value. Appearances can be deceiving.

#%%
print("id of Univs = ", id(Univs))
print("id of Univs1 =", id(Univs1))


#%%
print('Ids of Univs[0] and Univs1[1]', id(Univs[0]), id(Univs1[0]))

#%% [markdown]
# Why does it matters?
# 
# It matters because lists are mutable. Consider the **code** 

#%%
Tech.append("RPI")
Tech

#%% [markdown]
# The **append** method has a **side effect**. Rather than create a new list, it mutates the existing list Tech by adding a new element. Univs still contains the same two list, but the contents of one of those list has been changed

#%%
print("Univs = ", Univs)
print("Univs1 = ", Univs1)

#%% [markdown]
# It is possible to observe that Univs[0], and Tech are the same object, and since we changed Tech we also changed Univs[0]. This effect is called **aliasing**, which means that we can mutate the object using either path and the change will be reflected in both objects.

#%%
print(id(Tech))
print(id(Univs[0]))

#%% [markdown]
# The examples above showed us that concatenation of list generate a list of lists. However, sometimes you want to create a flat list for what you can use the '+' simbol

#%%
flat = Tech + Ivys
flat

#%% [markdown]
# ### Cloning
# 
# It is usually prudent to avoid mutating a list over which one is iterating. For example

#%%
def removeDups(L1, L2):
    """
    Assumes that L1 and L2 are list. Remove any element in L1 that is also in L2
    """
    for e1 in L1:
        print("e1=",e1)
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]

removeDups(L1, L2)
print("L1 = ",L1)

#%% [markdown]
# To avoid this problem use slicing to **clone**

#%%
def removeDups(L1, L2):
    """
    Assumes that L1 and L2 are list. Remove any element in L1 that is also in L2
    """
    for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]

removeDups(L1, L2)
print("L1 = ",L1)

#%% [markdown]
# ### List comprehension
# 
# The technique provides a concise way to apply an operation to the values in a sequence. It creates a new list in which element is result of an operation in another list

#%%
L = [x**2 for x in range(1,7)]
print(L)
result=[]
for i in range(1,7):
    result.append(i**2)
print(result)


#%%
mixed = [1,2,"a",3,4.2]
print([x**2 for x in mixed if type(x) == int])

#%% [markdown]
# ## Functions as Objects
# 
# In Python, functions are **firts-class objects**. That means they can be treated like objects of any other type, e.g., int or list. They have types, can appear in expressions (right-hand side of an assignment statement) or as an argument to a function, etc.

#%%
type(removeDups)


#%%
def applyToEach(L,f):
    """
    Assumes L is a list, f is a function
    mutates L by replacing each element, e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])

#%% [markdown]
# The function *applyToEach* is called a **second-order** because it has an argument that is itself a function. Python has a built-in higher-order function, *map*.

#%%
L1 = [1, 28, 36]
L2 = [2, 57, 9]
a = [map(min, a) for a in zip(L1, L2)]
a

#%% [markdown]
# ## Dictionaries 
# 
# Objects of type **dict** are like the lists except that 'indices' need not to be integers. Since they are not ordered we call them **keys** rather than indices. The entries in a diccionary are unordered and cannot be accessed with an index.

#%%
monthNumbers = {'Jan': 1, 'Feb': 2, 'Mar' : 3, 'Apr': 4, 'May': 5,
               1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May'}

print('the third month is ' + monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print('Apr and Jan are ', dist, 'months apart')


#%%
monthNumbers.keys()

#%% [markdown]
# some of the most useful operations on dictionaries are: **len(d), d.keys(), d.values(), k in d** (True is key k in d)**, d[k], d.get(k,v], d[k] = v, del d[k], for k in d**.
# 
# Objects of any **immutable type** can be used as dictionay keys. For example

#%%
monthNumbers[('Jun', 'Summer')] = 'Hot'
monthNumbers

#%% [markdown]
# It is relatively easy to implement a dictionary using a list in which each element is a key/value pair, but a dictionary is >>>> faster than this

#%%
def keySearch(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None

#%% [markdown]
# # Testing and Debugging
# 
# testing is the process of running a program to try and ascertain whether or not it works as intended. [Debugging](http://history-computer.com/ModernComputer/Relays/Aiken.html) is the process of trying to fix a program that you already know does not work as intended.
# 
# ## Conducting Tests
# 
# Testing is often thought of as occurring in two phases. One should always start with **unit testing** to ensure whether individual modules (e.g. functions) work properly. This is followed by **integration testing**, which is designed to ascertain whether the program as a whole behaves as intended. 
# 
# ## Debugging
# 
# Runtime bugs can be categorized along two dimensions:
# 
# * **overt -> covert:** An overt bug has an obvious manifestation, e.g., the program crashes or takes far longer to run. A **covert** bug has no obvious manifestation. The program my run to conclusion with no problem, but gives a wrong answer.
# 
# * **Persistent -> Intermittent:** A persitent bug occurs every time the program is run. An ontermittent bug ocurrs only some of the time.
# 
# Good programers try to write their programs in such a way that programming mistakes lead to bugs that are both overt and persistent. This is often called **defensive programming**
# 
# ### When the going gets tough
# 
# What to do when debugging gets tough:
# 
# * Look for usual mistakes
#      * Arguments passed in the wrong order
#      * Misspelled of a name
#      * Failed to reinitialize a variable
#      * Tested that two floating point variables are (==) instead of nearly equal
#      * Tested value equality L1==L2 when you wanted object equality id(L1) == id(L2)
#      * Created an unintentional alias
#      * etc
#      
# * Stop asking why the program is not doing what you want and ask why the program is doing what it is doing
# * Keep in mind that the bug is probably not where you think it is
# * Try to explain the problem to sombody else
# * Do not believe everything you read, since the code cannot be doing what the documentation says
# * Stop debugging and start writting documentation
# * Walk away and try tomorrow
#%% [markdown]
# # Exceptions and Assertions

#%%
test = [1,2,3]
test[2]

#%% [markdown]
# IndexError is the type of exception that Python raises when a program tries to access an element that is not within the bounds of and indexable type
# 
# ## Handling Exception 
# 
# When an Exception is raised that caused the program to terminate, we say that an **unhandled exception** has been raised. Exceptions when raised can and should be **handled**

#%%
numSuccesses = 20
numFailures = 0
successFailureRatio = numSuccesses/float(numFailures)
print('The success/failure ratio is ', successFailureRatio)


#%%
numSuccesses = 2
numFailures = 0
try:
    successFailureRatio = numSuccesses/float(numFailures)
    print('The success/failure ratio is ', successFailureRatio)
except ZeroDivisionError:
    print('No failures so the success/failure ratio is undefined')

#%% [markdown]
# Let's look at another example

#%%
val = int(input('Enter int: '))
print('The square of the number you entered is: ', val**2)


#%%
while True:
    val = input('Enter int: ')
    try: 
        val = int(val)
        print('The square of the number you entered is: ', val**2)
        break
    except ValueError:
        print(val + ' is not an integer')

#%% [markdown]
# If the program has many places where it is needed to enter an integer you can create a function to save both time and space

#%%
def readInt():
    while True:
        val = input('Enter int: ')
        try: 
            val = int(val)
            return val**2
        except ValueError:
            print(val + ' is not an integer')

readInt()

#%% [markdown]
# But you can do even better creating a **polymorphic** function *readVal*

#%%
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try: 
            val = valType(val)
            return val
        except ValueError:
            print(val + ' ' + errorMsg)
            
#val = readVal(int, 'Enter an integer:', 'is not an integer')
#val

val = readVal(str, 'Enter an string:', 'is not an string')

#%% [markdown]
# ## Exceptions as a Control Flow Mechanism

#%%
def getRatios(vect1, vect2):
    """
    Assumes: vect1 and vect2 are lists of equal length of numbers
    Returns: a list containing the meaninfull values of vect1[i]/vect2[i]
    """
    ratios = []
    for indx in range(len(vect1)):
        try:
            ratios.append(vect1[indx]/float(vect2[indx]))
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a number
        except:
            raise ValueError('getRatios called with bad args')
    return ratios

try:
    print(getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0]))
    print(getRatios([],[]))
    print(getRatios([1.0,2.0],[3.0]))
except ValueError as msg:
    print(msg)


#%%
def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #open file for reading
    except IOError:
        raise ValueError('getGrades could not open '+ fname)
    grades = []
    for line in gradesFile:
        try: 
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades

try:
    grades = getGrades('quizgrades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as errorMsg:
    print('Whoops, ', errorMsg)

#%% [markdown]
# ## Assertions
# 
# The Python assert statement provides programmers with a simple way to confirm that the state of computation is as expected. The form of an assert statement is
# 
#     assert Boolean expression, optional argument
#     
# When the **assert** statement is encountered the boolean expression is evaluated. If it is evaluated to True, excecution proceeds on its merry way. If it evaluated to False and AssertionError exception is raised

#%%
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32


try:
    KelvinToFahrenheit(-2)
except AssertionError as errMsg:
    print(errMsg)
    

#%% [markdown]
# # Classes and Object-Oriented Programming
#%% [markdown]
# The last major topic related to writing a program in Python is the use of clases. Classes can be used in the context of **object-oriented programming**, which requires that you think about an object as a collection of both data and the functions that operate on that data. We have been relaying in object oriented programming but you did not know it!!!
# 
# ## Abstract data types and classes
# 
# An **abstract data type** is a set of objects and the operations on those objects. These are bound together so one can pass an object from one part of the program to another, providing access not only to the data but also to the method that operate on that data.
# 
# The specifications of these operations define an **interface** between the abstract data type and the rest of the program. The interface defines what the operation does, but not how it does it. The interface then, provides an **abstraction barrier**
# 
# Programming is about managing complexity which can be acomplished through **decomposition and abstraction**. Decoposition creates structure and abstraction supresses complexity

#%%
class IntSet(object):
    """
    An IntSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        '''
        Create an empty set of integers
        '''
        self.vals = []
        
    def insert(self, e):
        '''
        Assumes e is an integer and inserts e into self
        '''
        if not e in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        '''
        Assumes e is an integer
        Return True if e is in self, and False otherwise
        '''
        return e in self.vals
    
    def remove(self, e):
        '''
        Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self
        '''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+ ' not found')
    
    def __str__(self):
        '''
        Returns a string representation of self
        '''
        self.vals.sort()
        print(self.vals)
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:,-1] + '}'


#%%
print(type(IntSet)), print(type(IntSet.member))

#%% [markdown]
# When a function definition occurs within a class definition, the defined function is called a **method** and is associated with the class. 
# 
# Classes support two kinds of operations:
# 
# * **Instantiation**: is used to create instances of the class. The statement s = IntSet() creates a new object of type IntSet. This object is called an **instance** of IntSet
# * **Attribute references**: Use dot notation to access attributes associated with the class, e.g. s.remove(e)
# 
# When the line code
# 
#     s = IntSet()
#     
# is executed, the interpreter will create a new object, called an **instance**, of type IntSet, and then call IntSet.__init__ with the newly created object as the actual parameter that is bound to the formal parameter **self**. When invoked, IntSet.__init__ creates vals, an object of type list which is called a **data attribute**

#%%
s = IntSet()
s.insert(3)
s.insert(6)
s.remove(7)

#%% [markdown]
# A class should no be confussed with instances of that class, just as an object of type list should not be confused with the list type. Keep in mind that IntSet.member and s.member are different objects.
# 
# When data attributes are associated with a class we call them **class variables**, and when they are associated with an instance we call them **instance variables**.
# 
# Data abstraction achieves representation-independence. The **representation invariant** defines which values of the data attributes encode valid representation of abstract values.

#%%
import datetime

class Person(object):
    def __init__(self, name):
        '''
        Creates a person with name name
        '''
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthDay = None
        
    def getLastName(self):
        '''
        returns self's last name
        '''
        return self.lastName
    
    def setBirthDay(self, birthDate):
        '''
        Assume birthDate is of type datetime.date
        set self's birthday to birthDate 
        '''
        self.birthday = birthDate
    
    def getAge(self):
        '''
        returns self's current age in days
        '''
        if self.birthday == None:
            raise ValueError
        return(datetime.date.today()-self.birthday).days
    
    def __lt__(self, other):
        '''
        return True if self's name is lexicographically
        less than other's name, and False otherwise
        '''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        '''
        return self's name
        '''
        return self.name


#%%
me = Person('Rodrigo DeLaFuente')
him = Person('Barack Obama')
him2 = Person('Levi Campos')
print(me.getLastName())
me.setBirthDay(datetime.date(1981, 5, 4))
print(me.getAge()/365.25)
print(him2)


#%%
pList = [me, him, her]
for p in pList:
    print(p)

#%% [markdown]
# Now, use the __lt__ method to sort the list

#%%
pList.sort()
for p in pList:
    print(p)

#%% [markdown]
# ## Inheritance
# 
# **Inheritance** provides a convenient mechanism for building groups of related abstractions. It allows programmers to create a type hierarchy in which each type inherits attributes from the type above it in the hierarchy. The class **object** is at the top of the hierarchy. Because **Person** inherits all of the properties of objects, programs can bind a variable to a **Person**, append a Person to a list, etc.

#%%
class MITPerson(Person):
    nextIdNum = 0 # this is a class variable
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum

#%% [markdown]
# MITPerson is a **subclass** of Person, and therefore **inherits** the attributes of the **superclass**. In addition, the subclass can:
# * Add new attributes
# * **Override** attributes of the superclass (MITPerson overrode __init__ and __lt__)

#%%
p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
p2 = MITPerson('Rodrigo Alarcon')
print(str(p2) + '\'s id number is ' + str(p2.getIdNum()))
p3 = MITPerson('Rodrigo Tapia')
print(str(p3) + '\'s id number is ' + str(p3.getIdNum()))


#%%
print('p1 < p2 =', p1 < p2)

#%% [markdown]
# ### Multiple levels of inheritance

#%%
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

#%% [markdown]
# By using the Python reserved word pass as the body, we indicate that the class has no attributes than those inherited from its superclass

#%%
p3 = Grad('Buzz Aldrin')
p4 = UG('Billy Beaver', 1984)
print(p3, ' is a graduate student is ', type(p3) == Grad)
print(p3, ' is an undergraduate student is ', type(p3) == UG)


#%%
class MITPerson(Person):
    nextIdNum = 0 # this is a class variable
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def isStudent(self):
        return isinstance(self, Student)
    def __lt__(self, other):
        return self.idNum < other.idNum
    
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

p3 = Grad('Buzz Aldrin')
p4 = UG('Billy Beaver', 1984)
print(p3, 'is a student is', p3.isStudent())
print(p4, 'is a student is', p4.isStudent())


#%%
print(isinstance(p4, Student))
print(type(p4) == Student)

#%% [markdown]
# Adding a transfer student

#%%
class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool
    def getOldSchool(self):
        return self.fromSchool

#%% [markdown]
# ### The substitution principle
# 
# The subclasses extend the behavior of their superclasses. For example TransferStudent extends Student by adding the notion of a former school. If a client code works correctly using an instance of the supertype, it should also work correctly when an instance of the subtype is substituted for the instance of the supertype. This is known as the **substitution principle**.
#%% [markdown]
# ## Encapsulation and information Hiding

#%%
class Grades(object):
    """
    A mapping from students to a list of grades
    """
    def __init__(self):
        '''
        Create empty grade book
        '''
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        """
        Assumes: Student is of type Student
        Add student to the grade book
        """
        if student in self.students:
            raise ValueError("Duplicate Student")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        '''
        Assumes: grade is a float
        Add grade to the list of grades for student
        '''
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError("Student not in mapping")
    
    def getGrades(self, student):
        '''
        Return a list of grades for students
        '''
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
            
    def allStudents(self):
        '''
        Return a list of the students in the grade book
        '''
        if not self.isSorted:
            self.students.sort()
        return self.students[:] # Return copy of list of students
    
def gradeReport(course):
    """
    Assumes: course is of type grades
    """
    report = ''
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n'                    + str(s) + '\'s mean grade is '                    + str(average)
        except ZeroDivisionError:
            report = report + '\n'                    + str(s) + ' has no grades'
    return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
SixHundred = Grades()
SixHundred.addStudent(ug1)
SixHundred.addStudent(ug2)
SixHundred.addStudent(g1)
SixHundred.addStudent(g2)
for s in SixHundred.allStudents():
    SixHundred.addGrade(s,75)
SixHundred.addGrade(g1, 25)
SixHundred.addGrade(g2, 100)
SixHundred.addStudent(ug3)
print(gradeReport(SixHundred))


#%%
SixHundred.getGrades(g2)

#%% [markdown]
# ### User-defined iterators
# 
# A percived risk of information hiding is that preventing client programs from directly accessing critical data structures leads to an unacceptable loss of efficiency. The invocation of **course.allStudents** creates and return a list of size **n**, which can be a huge problem when n has more than a million elements. A better soluction is to add an **iterator** to the abstraction.
# 
# Below, an improved version of the method is given. It uses a generator, which is like a function with the exception that it can stop in the middle, then return a value using a **yield** statement, and later resume from the point it has stopped.

#%%
class Grades(object):
    """
    A mapping from students to a list of grades
    """
    def __init__(self):
        '''
        Create empty grade book
        '''
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        """
        Assumes: Student is of type Student
        Add student to the grade book
        """
        if student in self.students:
            raise ValueError("Duplicate Student")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        '''
        Assumes: grade is a float
        Add grade to the list of grades for student
        '''
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError("Student not in mapping")
    
    def getGrades(self, student):
        '''
        Return a list of grades for students
        '''
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
            
    def allStudents(self):
        '''
        Return a list of the students in the grade book
        '''
        if not self.isSorted:
            self.students.sort()
        for s in self.students:
            yield s
            
def gradeReport(course):
    """
    Assumes: course is of type grades
    """
    report = ''
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n'                    + str(s) + '\'s mean grade is '                    + str(average)
        except ZeroDivisionError:
            report = report + '\n'                    + str(s) + ' has no grades'
    return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
SixHundred = Grades()
SixHundred.addStudent(ug1)
SixHundred.addStudent(ug2)
SixHundred.addStudent(g1)
SixHundred.addStudent(g2)
gen = SixHundred.allStudents()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


