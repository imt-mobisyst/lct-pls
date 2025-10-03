# Object-Oriented Programming

This tutorial revisits *OOP* concepts, by presenting them in Python. 
In a second part, an exercise is proposed to create a toolbox for _MP3_ collection management.

All the proposed pieces of code should be tested in a `script.py`.


## 1. Object-Oriented Programming (OOP) in Python



### 1.a. Structuring element together

First a **class** can be reduced to a collection of class attributes and functions.

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

To notice the indentations that state for wath inside a class and the instructions of each class's function.
In this exemple, _MyObjectType_ is a class with one attribut (_world_) and two functions (_function1()_, _function2()_).

### 1.b. Class Instance

The main feature of **class** is the capacity to instantiate objects (_class instances_).
An instance of a class is an object defined as a specific type.
It is possible to associate attributes with an instance.
In this case, instance-attribute values can be different for different instances of the same class (by opposition to class-attributes).

```python
# Definition:
class MyObjectType :
    class_word= "hello"     # A class attribute

# Use:
anInstance= MyObjectType()          # Instanciate a MyObjectType object

anInstance.instance_word= "world"   # an instance attribute

aSecondInstance= MyObjectType()
aSecondInstance.instance_word= "nobody"

assert( type(anInstance) is MyObjectType )
print( anInstance.class_word + ' ' + anInstance.instance_word )
```

At this point, `anInstance.class_word` is `MyObjectType.class_word`,
and for no confusion, you should use `MyObjectType.class_word` to manipulate this attribut.

Another good way to manipulate a class attribute: `type(anInstance).classAttribut`.
Typically, nasty manipulation of class-attribut can transform them into instance attributes for specific instances that generate failure, difficult to debug...
As in this example :

```python
# Definition:
class MyObjectType :
    classAttribut= "Void"

# Use:
anInstance= MyObjectType()

MyObjectType.classAttribut= "Hello"
print( anInstance.classAttribut )

anInstance.classAttribut= "World"     # I should not do that...
print( MyObjectType.classAttribut )

MyObjectType.classAttribut= "Hmmm"
print( anInstance.classAttribut + " - " + MyObjectType.classAttribut )
```


### 1.c. Methods

The strength of _OOP_ relies on the instances that define a context for the executions of functions associated to the class.
A function associated to an instance is named a **METHOD**.
In _Python_, a method is a class function where the instance is explicit as the first parameter.
A convention supposes that this instance is named _self_.

```python
# Definition:
class MyObjectType :
    def method(self) :
        return 42
    
# Use:
anInstance= MyObjectType() # Instanciate a MyObjectType

v1= anInstance.method()
v2= MyObjectType.method(anInstance)

if v1 == v2 :
    print( "Hello World" )

print( f"{MyObjectType.method}\nvs {anInstance.method}")
```

As in this example, in _Python_ a method can be called directly on an instance (_v1_) or as a class function (_v2_).
In the first case, the method is bound to an instance :

```python
# Definition:
class MyObjectType :
    def method(self) :
        return 42

anInstance= MyObjectType()

print( f"{MyObjectType.method}\nvs\n{anInstance.method} ({anInstance})")
```

As a result, in _Python_, a method with $3$ arguments is defined by a function of $4$ arguments.

```python
    def aMethod(self, argument1, argument2, argument3) :
        pass
```

---

## 2. Built-in Python

_Python_ defines numerous tools natively. 
Many of those tools rely on functions/methods associated with types.
There are named [built-in functions](https://docs.python.org/3/library/functions.html).
Those functions can be redefined (overridden) to attach a specific behavior to developer types (classes).


### 2.a. Built-in Class

First of them are the **built-in functions** defined in _Python_ objects:

- `__init__(self)` : Instance initialization, called at instance construction.
- `__del__(self)`  : Instance destruction, called when a instance is deleted.
- `__str__(self)`  : Transform an instance in a string

```python
# Definition:
class MyObjectType :

    def __init__(self):
        print('Initialization')
    
    def __del__(self): 
        print('Destruction')
    
    def __str__(self):
        return "> MyObjectType::instance <"

# Use:
anInstance= MyObjectType()
print( anInstance )
```

To notice that it is posible to change the number of parameters in `__init__` to generate a constructor over parrameters.
In general, all the instance attributs are created in the `__init__` method. But it is not mandatory (in fact in python, the number and definition of instance attributes are dynamic). 
It is also possible to call the parent method when overriding with [`super`](https://docs.python.org/3/library/functions.html#super).


```python
# Definition:
class MyObjectType :

    def __init__(self):
        print('Initialization')
    
    def __del__(self): 
        print('Destruction')
    
    def __str__(self):
        return "> MyObjectType::instance <"

# Definition:
class ObjectSpecific(MyObjectType) :
    
    def __init__(self, aNumber):
        super(MyObjectType, self)._init__(self)
        self._aNumber= aNumber
        
    def __str__(self):
        return f"> MyObjectType::instance-{self._aNumber} <"

# Use:
anInstance= MyObjectType(42)
print( anInstance )
```


### 2.b.  Good practices. 

As we already see, several rules are more good practices than language constraints. 

- The current instance, context for a method execution, is always named _self_.
- `__init__` method (if defined) is your first method.
- Initialize your instance attributes into the `__init__` method.
- Attribute names start with `_`. 
- Class names start with an Uppercase letter.
- etc.

Most of those conventions are presented in the [style guide for Python code](https://peps.python.org/pep-0008/)


### 2.c.  Operators. 

Finally, most of the operator can be redefined based on built-in function.
For a complete list with other type built-in functions, see [docs.python.org](https://docs.python.org/3/library/stdtypes.html)

An example with the addition:

```python
class Vector :

    def __init__(self, x, y):
        self._x= x
        self._y= y
    
    def __add__(self, another):
        return Vector( self._x+another._x, self._y+another._y )

    def __str__(self):
        return f"({self._x}, {self._y})"

# Use:
a= Vector( 10.7, 8.0 )
b= Vector( -2.1, 34.0 )
print( f"{a} + {b} = {a+b}" )
```


---

## 3. Let's Play

We  now have an idea of what _OOP_ is capable of in _Python_. 
The exercise here is to put those notions in music.


### Read a Mp3 sound

- https://pypi.org/project/playsound3/
- https://eyed3.readthedocs.io/en/latest - https://pypi.org/project/eyeD3/


### Manipulating Meta-data


<!---

## OOP in Python: default argument values


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
- ...




---
<!-- --------------------------------------------------------------- - ->

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
<!-- --------------------------------------------------------------- - ->

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
<!-- --------------------------------------------------------------- - ->

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
<!-- --------------------------------------------------------------- - ->

## Cloud :: More usefull elements

- **Random generator** - generate randomly a point cloud of $n$ points.
- **Print function** - overdefine `__str__` in an informative, not too long way.
    - Exemple: `print( aCloud )  > [(12.8, 8.5), (7.8, 0.5), ...](100)`

---
<!-- --------------------------------------------------------------- - ->

## Create a class to manipulate Point Cloud

<br />
<br />

- **More Accessors:**
    - *listX():* return a list of the *x* values of all points (**&** *listY():* reciprocally)
- **Computation:** - *average():*, *standardDeviation()*, *minXPoint():*, ...
- ... 

<br />
