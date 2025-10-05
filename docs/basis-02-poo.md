# Object-Oriented Programming

This tutorial revisits *OOP* concepts, by presenting them in Python. 
In a second part, an exercise is proposed to create a toolbox for _MP3_ collection management.

All the proposed pieces of code should be tested in a `script.py`.


## 1. Object-Oriented Programming (OOP) in Python

Playing with class, and the main concepts of OOP in _Python_.

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

To notice the indentations that state what is inside a class with a new level of indentation for instructions of the class's function.
In this example, _MyObjectType_ is a class with one attribute (_world_) and two functions (_function1()_, _function2()_).

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
Typically, nasty manipulation of class-attributes can transform them into instance attributes for specific instances that generate failure, difficult to debug...
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

To notice that it is possible to change the number of parameters in `__init__` to generate a constructor over parameters.
In general, all the instance attributes are created in the `__init__` method. But it is not mandatory (in fact, in Python, the number and definition of instance attributes are dynamic). 
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


### 3.a Read a Mp3 sound

As a first exercie we want a class representing a song. 
First, an exploration on internet showed us the librairie: [playsound3](https://pypi.org/project/playsound3) allowing us for play _mp3_ music.

This example loads a music song and play it :

```python
import time 
from playsound3 import playsound

# You can play sounds in the background
sound = playsound("./song.mp3", block=False)

# and check if they are still playing
if sound.is_alive() :
    print("Sound is playing!")
    time.sleep( 5.0 )

# and stop them whenever you like.
sound.stop()
```

So as a first result, we aim to have a class (_Song_ for instance) with methods to load a music file and to play it.

Something like this: 

```python
class song :
   # To implement ... 

asong= Song()
asong.load("./song.mp3")
aSound.play()
```

### 3.b Accessor

Our _Song_ class defines a few attributes for an instance: a title, an artist name, an album name, and the number of tracks in the album. First, we want a constructor that defines all of these attributes. Then we ask for an accessor method for each of these attributes.

```python
class song :
   # To implement ... 

asong= Song("Rodriguez", "Can't Get Away", "Searching for Sugar Man",  7 )
asong.load("./song.mp3")
print( f"{asong.artist()} - {asong.album()} {asong.track()} - {asong.title()}" )
asound.play()
```

In fact, we will prefer to get metadata from the file directly when loading it.
To do that we can count on [eyeD3](https://pypi.org/project/eyeD3) _Python_ library ([documentation](https://eyed3.readthedocs.io/en/latest)).

Here's a piece of code to help in this mission: 

```python
import eyed3

audiofile = eyed3.load("song.mp3")
print( audiofile.tag.artist )
print( audiofile.tag.album )
print( audiofile.tag.album_artist )
print( audiofile.tag.title )
print( audiofile.tag.track_num.count)
```

It is also possible to define default parameter values in the `__init__` method to be capable of instantiating a new song without metadata.
To learn how to do that, let's go on internet.
For instance, the [w3schools]( is an excellent entrance point regarding web technologies and presents, among others, the notion of [function default parameter](https://www.w3schools.com/python/gloss_python_function_default_parameter.asp), with a sandbox...



### 3.c Some commands

You should now have a first skeleton of the application we want to create.
However, in fact, the goal is to create several commands. So the best way to do that in a first move, is to create several _Python_ files. A first _Python_ file will implement our _Song_ class with all the required functionality as methods of the class. Then we add a _Python_ file for each command we want to implement. 

In your directory you should have :

```sh
songpkg.py   # With the Song class
command1.py
command2.py
command3.py
...
```

The command script should be as small as possible.
All the important code is in `songpkg.py`, and imported in your command file.

For instance, the `play.py` command will look like 

```python
import songpkg

asong= songpkg.Song()
asong.load("./song.mp3")
print( f"{asong.artist()} - {asong.album()} {asong.track()} - {asong.title()}" )
asound.play()
```

The expected command: 

- `play.py` : Takes a file name of a song as an argument and print the metadata of that song  before playing the song.
- `set.py` : Takes a file name of a song and all metadata as command arguments and save the file with those metadata.
- `playlist.py` : Takes a playlist as an argument (a text file, with a list of MP3 files to play) and plays it.
- `search.py` : Takes an artist name, a search all the local MP3 files matching that artist.
- `rename.py` :  search all MP3 recursively in a directory, and rename them as `artist - album track - title.mp3`.

To do that, you will certainly requires _os_ _Python_ modul (again on [w3schools](https://www.w3schools.com/python/module_os.asp)) and more specifically, the `os.listdir()` returning a list of the names of the entries in a directory.





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

