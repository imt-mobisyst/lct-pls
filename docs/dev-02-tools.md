# Develloper's tools

The idea here is to present brieflly the main tools in the develloper toolbox (exept for it favorit IDE).
It is mainly question of _Versionning_ and _Test-Driven-Devellopement_.

It is philosofical tools.

_Versionning_ tell you that you should adopt a develloper behavior allowing you to keep the historic of the devellopement process (succesive code changes). 
At any time, you should be capable to return the project in any previous state achieved. 

_Test-Driven-Devellopement_ tell you that you should firts devellope the tests of the functionnallity to devellope. 
This way you you start from an example of how to use it, and witch results the functionnality generate.

Those two philosofy allows you to work in complete security, with no risk of trying things and maibe broke every thing.
Naturally those philosofy come with implemeted tools to deploye. You have for instance _git_ for _Versionning_  and _pytest_ for _Test-Driven-Devellopement_ 


## 1. Versionning

So the idea is to keep traces of code changes.
But first, it start with a project.
The idea is to create a python package (let say scene2d), that represent a a 2 dimentional vectorial scene. 
I.e. a collection of shapes (points, lines, poligones, ...).

### 1.a Project initialization

So first, we require to create our project, with a `scene-prj` directory, a `README.md` file inside including a brief description of wath we apptenting to do and a `scene2d.py` file for our new python package.

This is our initial state. And we want to save it.
To do that we will use _git_ :

- Offical webpage: [git-scm.com](https://git-scm.com)
- On windows tipically: [on git-scm.com](https://git-scm.com/downloads/win) on [gitforwindows.org](https://gitforwindows.org/)
- Basis in less than 30 minutes: [git-scm.com/videos](https://git-scm.com/videos)

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

As git inform you, _git_ works with different branches. 
Each branch match a specfic vertion of the project. 
Typically you can have `master` for the main branch shared with all the user, `beta` for the beta-test version and `dev` for the in-devellopement branch.
You can also have a branch per target `window`, `linux` or `mac` a branch per contributor in the project etc.
By default, `git init` create a unique empty branch `master`.

The command `git status` allows develloper to get the status of the repository (repository : a versionned directory).
At this time, status should state that _README.md_ and _scene2d.py_ is not included to keep changes.

We should add them, and commit to reccord those new file and the content.

```sh
git add README.md scene2d.py
git commit
```

Potentially, this command require some information about the author. 
You should provide them as recommanded, and commit again.

The commit command open an editor to allows you to put a reccord message. 
Here you can put "initial commit" and save. 
Those message serve to remember the status of the project at commit time. 
Finaly, the command `log` permit to list the history of comit.
Only one for now.

```sh
git log
| commit a6e5dc1b0fd47f22416e66787dd6c13f8b365fdd (HEAD -> master)
| Author: guillaumeLozenguez <guillaume@drods.net>
| Date:   Tue Oct 7 16:57:42 2025 +0200
| 
|    initial commit
```

### 1.b Camera.

As a first functionnally, _scene2d_ project should be capable of drawing differents shapes.
However, our scene should be define in a cartesian space, with floating point values. 
The drawing is in pixel.
Futhermore the frame of our scene is not necessarlly the same than the drawing. 

We imagine to include those functionnality into a class _Camara_ defined with a _scale_ (a number of pixel per scene unit - meters for instance) and _position_.
So we initialize such a new class in our `scene2d.py`.

```python
class Camera :
    def __init__(self)
        self._scale= 10
        self._position_x= 0.0
        self._position_y= 0.0
```

At this point, a `git status` should inform us that the file `scene2d.py` is modified.
If you want to reccord those modification, we should add again `scene2d.py` to be track in the next commit then commit.
A short way to do that is to use a _add-all_ option (`-a`). 
It is also possible to feed the commit with the commit message, by using the option `-m`.

So : 

```sh
git commit -a -m "new Camera class"
```

For a complet description of commit options: [git-scm.com/docs](https://git-scm.com/docs/git-commit).

Now the `git log` command should state _2_ commits. 
Notice that the commit comes with an identifier, _a6e5dc1b0fd47f22416e66787dd6c13f8b365fdd_ in my case, for the first commit.
This identifier allows you to retrieve previous version of your code. 

For instance with a :

```sh
git checkout a6e5dc1b0
```

my `scene2d.py` is empty. 
It is my initial commit.
A `git checkout master` returns the code in the last version in the time line, on the _master_ branch (our unique branch at this point).

For more about _git_, you can search all the _git_ commands: [git-scm.com/docs](https://git-scm.com/docs).


##  2. Test-Driven Devellopement

Define test-cases before to code.
The main idea de develloping program is to implement functionnalities incrementally to allows our program to grows in complexity.
With tests, you create scripts that will test each of your functionnalities in any direction possible.

Test-Driven Devellopement (_TDD_) go further. 
It invites devellopers to create the tests before creating the functionnallity.
This process, in this order, force the devellopers to clearly defines the conxte of execution of the desired functionnallity.

More on TDD on [wikipedia.org](https://en.wikipedia.org/wiki/Test-driven_development).

Professor advise: It seams to cost you a lot at begining, to create a test before of the functionnality.
In fact, in a professional life, it will save you a lot of times.


### 2.a Get Started

Again, python comes with several tools for automatic test. 
Here we propose to use _pytest_.
For a complete introduction of the tool: [wikipedia.org](https://en.wikipedia.org/wiki/Pytest)

_Pytest_ can be install with pip (wath a surprise...).

By default, tests are implemented on specific test python files.
Those files will alwais be named as `test_something.py`. 
This way, _pytest_ will recognise the file as resseource to test.
To notice that _pytest_ will test all `test_...py` files in an alphabetic order. 
So we recommand to adopt specific naming rules to control the order the tests are executed.

Let start with a first test file `test_01_package.py`. 
This test tests the existance of our package and its component.
Tests are _Python_ function with no argument.
As for file names, function names should start with `test_`.

Exemple for our `test_01_package.py`.

```python
def test_import():
    import scene2d

import scene2d

def test_camera():
    camera= scene2d.Camera()
```

Then, you can test a specific file `pytest test_01_package.py` or all a directory tree with `pytest` alone.
_Pytest_ also accept argument, as _-x_ to stop on the first failure.

At this point, test should fail. A `:` is missing after `def __init__(self)` of the _Camera_ class.

You can commit after adding _test_01_package.py_ with a commit message: _'first tests'_.
In fact you can commit as often as possible.
Git reccords only modifications in the files and frequent commits will not cost a lot more space than rare commits.

### 2.b Frame transform



### 2.b Drawing




## 3. Debugging

Investigate debugging tools is out of the scope of this lecture. 
However you can see : 

1. Wath your favorit editor is capable of: [code.visualstudio.com](https://code.visualstudio.com/docs/python/debugging).
2. The _Python_ debuger lib: [pdb](https://docs.python.org/3/library/pdb.html)
3. And potentially the main _Python_  [profiler](https://docs.python.org/3/library/profile.html).

In our level, we just expect a good behavior.
In case of bug, it is expected to isolate the bug. 
So first, create a new test-case that repropose the detected problem.
At this step, the test should not pass. 
Then, try to correct the bug. 

This way you continouslly inprove your test base and you garanty that any modification in future code changes will never generate again a already visited bug whithout to be detected.
