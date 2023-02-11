#change code
#now made a change
#to check git diff-staged
#ok
#without staging
print("this is the way to get output")
if 1<2:
    print("hello")
#single line comment
'''multiline comment x=8'''
x=3
y=5
z="vishal"
print(x,y,z)
x=8
print(x) #x has been overwrited
x=str(3) #typecasting
y=int(3)
z=float(3)
print(x,y,z)
#x="vishal" same as x='vishal'
#variable can have only alpha numeric with _ and start with alpha or _
#myValue camel case
#MyValue pascal case
#my_value snake case
a,b,c=1,2,3
print(a)
print(b)
print(c)
a=b=c=5
print(a,b,c)
e=[1,2,3,4] #one variable many values
a,b,c,d=e
print(a,b,c,d) #this iterate through list
x,y,z="hi","friends","how are you"
print(x+y+z) #+concatentate strings
print(x,y,z)#,seperate variables
a=2
b="vishal"
print(a,b) #right answer
#print(a+b) is wrong as it is different datatype
x="variable"
def fun():
    print(x)
fun()    #that is without local global taken
x="variable1"
def fun1():
    x="variable2"
    print(x)
print(x) #this give preference to global
fun1() #here give preference to local
#to change local
def fun2():
    global x
    x="vishal"
    print(x)
fun2()
print(x)#this way global creatted and we can even change value of global variable
x=5
print(type(x)) #this say data type
x=5.0
print(type(x))
x=1j
print(type(x)) #this is complex
print({"a":1,"b":2}) #this is dictionary type
print(frozenset({1,2,3,4})) #this is frozenset
#exact bool type is True and False
x=b"vishal" #this is bytes type
print(x)
x = bytearray(5)
print(x) #this is bytearray
x = memoryview(bytes(5)) #this is memoryview
print(x)
print(complex(1,2)) #this gives a+ib form
print(list((1,2,3))) #same way use for all dict,bool,bytes,bytearray with two brackets
#remember b,bytearray,memoryview(bytes(x))