# Object-Oriented Programming



## Object-Oriented Programing in Python

**class:** first, a collection of class attribute and functions.

```python
# Definition:
class MyObjectType :
    world= "world"

    def function1() :
        return "hello"

    def function2() :
        return MyObjectType.world

# Use:
hello= MyObjectType.function1()
print( hello + ' ' + MyObjectType.function2() )
```

Still with indentation... 

---

## OOP in Python : Class and Instances

The possibility to instantiate objects.

```python
# Definition:
class MyObjectType :
    class_word= "hello"     # A class attribute

# Use:
anInstance= MyObjectType()          # Instanciate a MyObjectType object

anInstance.instance_word= "world"   # an instance attribute

assert( type(anInstance) is MyObjectType )
print( anInstance.class_word + ' ' + anInstance.instance_word )
```

At this point: `anInstance.class_word is MyObjectType.class_word`


---

## OOP in Python : Class and Instances


<div class="line">
<div class="one2">

<br />
<br />

### What is the output <br /> of this code ?

<br />
<br />

A good way to manipulate a 
class attribute: `type(anInstance).classAttribut`


</div>
<div class="one2">

```python
# Definition:
class MyObjectType :
    classAttribut= "Void"

# Use:
anInstance= MyObjectType()

MyObjectType.classAttribut= "Hello"
print( anInstance.classAttribut )

anInstance.classAttribut= "World"
print( MyObjectType.classAttribut )

MyObjectType.classAttribut= "Hmmm"
print( anInstance.classAttribut )
```

</div>
</div>


---

## OOP in Python : Methods

Method: an _instance functions_ (the current instance is `self` by convention)

```python
# Definition:
class MyObjectType :
    def method(self) :
        return 42
    
# Use:
anInstance= MyObjectType() # Instanciate a MyObjectType

v1= MyObjectType.method(anInstance)
v2= anInstance.method()

if v1 == v2 :
    print( "Hello World" )
print( f"{MyObjectType.method}\nvs {anInstance.method}")
```


---

## OOP in Python: Methods

### Method versus Function

```python
# Definition:
class MyObjectType :
    def method(self) :
        return 42

print( f"{MyObjectType.method}\nvs\n{anInstance.method}")
```

Output:

```
<function MyObjectType.method at 0x7f36636e7a30> 
vs
<bound method MyObjectType.method
 of <__main__.MyObjectType  object at 0x7f366368c310>>
```


---

## OOP in Python: Methods

<br />
<br />
<br />

### Example of a method with $3$ arguments

```python
    def aMethod(self, argument1, argument2, argument3) :
        pass
```

<br />
<br />

---

## OOP in Python: default argument values


**Built-in Methods**: Method already defined in python Objects

- `__init__(self)` : Instance constructor
- `__del__(self)`  : Instance destructor
- `__str__(self)`  : String generation

Example:

```python
def aFunction() :
    anInstance= MyClass()      # call anInstance.__init__()
    print( anInstance )        # call anInstance.__str__()
    return True                # garbage call to anInsatnce.__del__()
```

---

## Object-Oriented Programing in Python

<br />

**Constructor**: `__init__` : initialize a new instance with potentially $n$ arguments

```python
class MyClass() :
    def __init__ ( self, arg1, arg2 ) :
        self._attribut1= param1
        self._attribut2= function( param1, param2 )

anInstance= MyClass( "Paul", "Mouaddib" )
```

<br />

In Python `__init__` method is unique (as all other methods)
(i.e. no overloading)


---

## Object-Oriented Programing in Python

Function with a variable number of arguments  - **Example:**

```
function(1, 2)
function(1, 2, 3, 4)
```

**Definition:** parameters with default values

```python
def aFuncrion ( val1=1, val2=0, val3=0, val4=1 ) :
    return (val1+ val1+ val1) * val4
```

**Alternative Run:**

```
function( val4=8 )
```


--- 

## Object-Oriented Programing in Python


**Good Practices:**

- Use `self`.
- Prefer instance method (at least `self` argument).
- Name your attributes starting with `_`.
- Never access class attributes from instances directly.
(Better `Class._att` or `type(instance)._att` than `instance._att`).
- `__init__` method (if defined) is your first method.
- Initialize your instance attributes into `__init__` method.
- ...


---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- OOP in Python
- **Let's Play**


---
<!-- --------------------------------------------------------------- -->

## Create a class to manipulate Point Cloud

<br />
<br />

- **Initialize your working space**
- Define **instance attributes**
- Propose some **initialization**
- Provide **accessors**
- Customize **built-in methods**
- Develope some **usefull methods**
- ...


---
<!-- --------------------------------------------------------------- -->

## Create a class to manipulate Point Cloud

- **Initialize your working space** - two files in a same directory: 
    - `myCloud.py` with _class definition_.
    - `test_myCloud.py` a _test script_ with instanciation and call to methods.

</br >

<div class="line">
<div class="one2">

`myCloud.py`:

```python
class Cloud :
    pass
```

</div>
<div class="one2">

`test_myCloud.py`:

```python
import myCloud as mc

aCloud= mc.Cloud()
assert( type(aCloud) == mc.Cloud )
```

</div>
</div>

Then execute: `python3 test_myCloud.py`

---
<!-- --------------------------------------------------------------- -->

## Cloud :: Construction and Accessors.

- As a first functionality the possibility of _adding_ and _access_ points.

The `test_cloud.py` will be:

```python
import myCloud as mc

aCloud= mc.Cloud()
assert( aCloud.size() == 0 )
assert( aCloud.points() == [] )

aCloud.append( 3, 8 )
assert( aCloud.size() == 1 )
assert( aCloud.points() == [(3,8)] )
assert( aCloud.point(0) == (3,8) )

...
```

---
<!-- --------------------------------------------------------------- -->

## Cloud :: More usefull elements

- **Random generator** - generate randomly a point cloud of $n$ points.
- **Print function** - overdefine `__str__` in an informative, not too long way.
    - Exemple: `print( aCloud )  > [(12.8, 8.5), (7.8, 0.5), ...](100)`

---
<!-- --------------------------------------------------------------- -->

## Create a class to manipulate Point Cloud

<br />
<br />

- **More Accessors:**
    - *listX():* return a list of the *x* values of all points (**&** *listY():* reciprocally)
- **Computation:** - *average():*, *standardDeviation()*, *minXPoint():*, ...
- ... 

<br />
