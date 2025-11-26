# Develloper's tools

The idea here is to present briefly the main tools in the developer toolbox.
It is mainly a question of _Versionning_ and _Test-Driven-Devellopement_.

In some way, they are philosophical tools. Their main reliance is on good practices (and a little on dedicated software).

_Versionning_ tell you that you should adopt a developer behavior allowing you to keep the history of the development process (successive code changes). 
At any time, you should be capable of returning the project to any previous state. 

_Test-Driven-Devellopement_ tell you that you should first develop the tests of the functionality before to implement it. 
This way you start from an example of how to use it and which results the functionality should generate.

Those two philosophies allow you to work in complete security. You can try things that could break everything. Tests will help in the repairing process, or versions will allow you to return to a working state.
Naturally those philosophies come with software-tools to deploy. You have, for instance, _Git_ for _Versionning_  and _Pytest_ for _Test-Driven-Devellopement_.


## 1. Versionning

So the idea is to keep traces of code changes.
But first, it starts with a project.
The idea is to create a _Python_ package (let's say scene2d), that represents a 2-dimensional vectorial scene. 
I.e. a collection of shapes (points, lines, polygons, ...).

### 1.a Project initialization

So first, we are required to create our project, with a `scene-prj` directory, a `README.md` file inside including a brief description of what we are attempting to do, and a `scene2d.py` file for our new _Python_ package.

This is our initial state. And we want to save it.
To achieve it, we will use _git_ :

- Official webpage: [git-scm.com](https://git-scm.com)
- On Windows, typically: [git-scm.com](https://git-scm.com/downloads/win) or [gitforwindows.org](https://gitforwindows.org/)
- And some basis in less than 30 minutes: [git-scm.com/videos](https://git-scm.com/videos)

So, with your favorite shell, you initialize a _git_ repository:

```sh
cd scene-prj
ls .
| README.md scene2d.py
cat README.md
| # Scene2d
|
| A python package to model a 2 dimentional scene as a collection of shapes. 
git init .
```

As _Git_ informs you, _Git_ works with different branches. 
Each branch matches a specific version of the project. 
Typically you can have `master` for the main branch shared with all the users, `beta` for the beta-test version, and `dev` for the in-development branch.
You can also have a branch per target: `window`, `linux` or `mac` a branch per contributor in the project, etc.
By default, `git init` creates a unique empty branch: `master`.

The command `git status` allows developers to get the status of the repository (a repository can be seen as a versioned directory).
At this time, status should state that _README.md_ and _scene2d.py_ are not included to keep changes.

We should add them, and commit to recording those new files and their content.

```sh
git add README.md scene2d.py
git commit
```

Potentially, this command requires some information about the author. 
You should provide them as recommended and commit again.

The commit command opens an editor to allow you to define a commit message. 
Here you can write "initial commit" and save. 
Those messages serve to remember the status of the project at commit time. 
Finally, the command `log` permits listing the history of commits.
Only one for now.

```sh
git log
| commit a6e5dc1b0fd47f22416e66787dd6c13f8b365fdd (HEAD -> master)
| Author: guillaumeLozenguez <guillaume@drods.net>
| Date:   Tue Oct 7 16:57:42 2025 +0200
| 
|    initial commit
```

### 1.b The Camera Class

As a first functionality, the _scene2d_ project should be capable of drawing different shapes.
However, our scene should be defined in a Cartesian space, with floating-point values. 
By opposition, the drawing is in pixels.
Furthermore, the Cartesian basis of our scene is not necessarily the same as in the drawing. 

We imagine including that functionality into a class _Camara_ defined with a _scale_ (a number of pixels per scene unit - meters for instance) and _position_.
So we initialize such a new class in our `scene2d.py`.

```python
class Camera :
    def __init__(self)
        self._scale= 10
        self._position_x= 0.0
        self._position_y= 0.0
```

At this point, a `git status` should inform us that the file `scene2d.py` is modified.
If you want to record those modifications, we should add again `scene2d.py` to be included in the next commit then commit.
A short way to do that is to use a _add-all_ option (`-a`). 
It is also possible to feed the commit with the commit message, by using the option `-m`.

So : 

```sh
git commit -a -m "new Camera class"
```

For a complete description of commit options, see [git-scm.com/docs](https://git-scm.com/docs/git-commit).

Now the `git log` command should state _2_ commits. 
Notice that each commit comes with an identifier, _a6e5dc1b0fd47f22416e66787dd6c13f8b365fdd_ in my case, for the first commit.
This identifier allows you to retrieve previous versions of your code. 

For instance, with a :

```sh
git checkout a6e5dc1b0
```

my `scene2d.py` is empty, as in my initial commit.
A `git checkout master` returns the code in the last version in the timeline on the _master_ branch (our unique branch at this point).

For more about _Git_, you can search all the _Git_ commands at [git-scm.com/docs](https://git-scm.com/docs).


##  2. Test-Driven Devellopement

Define test-cases before to code.
The main idea of develloping program is to implement functionalities incrementally to allow our program to grow in complexity.
With tests, you create scripts that will test each of your functionalities in any direction possible.

Test-Driven Development (_TDD_) goes further. 
It invites developers to create the tests before creating a functionality.
This process, in this order, forces the developers to clearly define a context of execution for the desired functionality.

More on _TDD_ on [wikipedia.org](https://en.wikipedia.org/wiki/Test-driven_development).

Professor's advice: It seems to cost you a lot at the beginning to create a test before of the functionality.
In fact, in a professional life, developing _TDD_ reflexes will save you and your team many times.


### 2.a Get Started

Again, _Python_ comes with several tools for automatic testing. 
Here we propose to use _pytest_.
For a complete introduction of the tool, see [wikipedia.org](https://en.wikipedia.org/wiki/Pytest).

_Pytest_ can be installed with pip (what a surprise...).

By default, tests are implemented on specific _Python_ test files.
Those files will always be named as `test_something.py`. 
This way, _pytest_ will recognize those files as resources to test.
To notice that _pytest_ will test all `test_...py` files in an alphabetic order. 
So we recommend adopting specific naming rules to control the order the tests are executed.

Let start with a first test file `test_01_package.py`. 
This test tests the existence of our package and its components.
Tests are _Python_ functions with no argument.
As for file names, function names should start with `test_`.

Exemple for our `test_01_package.py`.

```python
def test_import():
    import scene2d

import scene2d
def test_camera():
    camera= scene2d.Camera()
```

You can test a specific file with `pytest test_01_package.py` or an entire directory tree with `pytest` alone.
_Pytest_ also accepts arguments, such as _-x_ to stop on the first failure.

At this point, test should fail. A `:` is missing after `def __init__(self)` of the _Camera_ class. Correct the file and try again.

You can commit after adding _test_01_package.py_ with a commit message: _'first tests'_.
In fact, you can commit as often as possible.
Git records only modifications in the files, and frequent commits will not cost a lot more space than rare commits.

### 2.b Frame transform

So the first functionality of our camera is to be capable of transforming coordinates in the scene into pixels in the drawing.
As a first approximation, the test can be worded in usual english: 

```verbatim
It is possible to define a Camera.
The Camera has a drawing surface (by default 600x400).
The Camera has a position (by default (0, 0) ).
(The position points the location in the center of the image)
So transforming origin position should retrun (300, 200).
The Camera has a scale (number of pixel per scene unit).
The default scale is 10 pixels.
So the transfrom of (1.0, 1.0) should be (310, 190)
(y-axis is in the oposit direction in a drawing).
```

To define this test, we will use the `assert` instruction. 
`Assert` is a built-in instruction in _Python_, testing for a condition, and stopping the execution of the program if the condition is false (failure).

Example in [w3schools.com](https://www.w3schools.com/python/ref_keyword_assert.asp).

So, our new `test_02_camera.py` will be: 

```python
def test_defaultCamera():
    camera= scene2d.Camera()
    assert type(camera) == scene2d.Camera
    x, y= camera.position()
    assert (x, y) == (0.0, 0.0)
    assert camera.scale() == 10

def test_defaultTransform():
    camera= scene2d.Camera()
    assert camera.pixel(0.0, 0.0) == (300, 200)
    assert camera.pixel(1.0, 1.0) == (310, 190)
```

At this point, `pytest -x` should fail.
The first error is that the `position` method is not implemented.
To leverage this error, we can implement this method by returning the coordinates.
The second error will point to the `scale` accessor method, etc.

At the end of this debugging process, your code should not fail in any way. 
This will indicate you terminate to implement the functionality. 
It is a good time to commit.

Before going on to another functionality, it is possible to add more tests to validate that, the transformation operates with different camera positions and scalings. 
That's supposed to test the possibility to modify the camera attributes and that the transform computations remain ok.

### 2.b Drawing

For a complete _Camera_ class, we suppose the capability to effectively draw some vector-graphics in a file (based on the _cairo_ librairy for instance).


```verbatim
It is possible to instanciate a Camera.
The camera point to a file ('output.png' by default).
It is possible to use the Camera to draw a line.
It is possible to use the Camera to draw the frame basis.
```

So, in a new `test_03_drawing.py` file: 

```python
def test_drawLine():
    camera= scene2d.Camera()
    assert camera.file() == "output.png"
    camera.drawLine( (-3.0, -5.0), (3.0, 5.0) )
    camera.save()

    outputFile= open( "output.png", mode='rb' ).read()
    refsFile= open( "resources/02-line.png", mode='rb' ).read()
    assert shotFile == refsFile 

def test_drawBasis():
    camera= scene2d.Camera()
    camera.setPosition( 2.0, 1.5 )
    camera.setScale( 50 )
    camera.drawBasis()
    camera.save()

    outputFile= open( "output.png", mode='rb' ).read()
    refsFile= open( "resources/02-basis.png", mode='rb' ).read()
    assert shotFile == refsFile 
```

The tests mainly rely on comparing `.png` bitmap.
To do that, we open the bitmap in _read bit_ mode and perform a comparison.
Potentially, the test fails because the test is wrong. 
In our case, at some point, the tests should fails on `open("resources/02-line.png")`.

When you are satisfied with the generated _output.png_ (a beautiful black line under a white background, for instance), 
then you copy-paste this file as _02-line.png_ into a new _resources_ directory.
_Pytest_ should pass to the next failure.
In other words, defining the tests helps you in the process of implementing the functionality. 
However, the test implementation can evolve with the implementation of the functionnality.

Is everything ok ? Then commit. 
Attention, the `output.png` file should not be included in your _Git_ repository. 
This file is generated, there is no need to save it.

Look at [gitignore](https://git-scm.com/docs/gitignore) to do that properly.

### 2.c Go on...

Let apply this methodology (define a test and use the test to implement a functionality) for several more functionalities: 

- Drawing polydones and circles.
- Changing the drawing color (stroke and/or fill colors).

## 3. Debugging

Investigate debugging tools is out of the scope of this lecture. 
However you can see : 

1. What your favorite editor is capable of: [code.visualstudio.com](https://code.visualstudio.com/docs/python/debugging).
2. The _Python_ debugger lib: [pdb](https://docs.python.org/3/library/pdb.html)
3. And potentially a _Python_ [profiler](https://docs.python.org/3/library/profile.html).

At our level, we just expect good behavior: 

In case of a bug, it is expected to isolate the bug. 
So first, create a new test-case that reproduces the detected problem.
At this step, the test should fail. 
Commit. Then, correct the bug. Commit.

This way you continuously improve your test-pool and you guarantee clean future developments.
If any modification in the code generates again a bug already encountered, this bug will be automatically detected.


