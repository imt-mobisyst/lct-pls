# Python packaging.

Until now, all our _Python_ components have been defined in a unique file `scene2d.py`.
By growing in complexity, most of the project relies on several source files. 
Then your _Python_ package would be all the content of an entire directory.

Here, the goal would be to create shape classes, in our _scene2d_ packages.

## 1. Classical package strucure 

Classically the package is in a source (src) directory.
It is composed with `__init__.py` files defined (potentially empty) in each pkg directory. 
This file marks a _Python_ package. It would  also be the imported file when you will `import pkg`.

```verbatim
workspace
    src
    └── pkg
        ├── __init__.py
        ├── module1.py
        └── subpkg
            ├── __init__.py
            └── module2.py
```

In our case it should be :

```verbatim
scene-prj
    src
    └── scene2d
        ├── __init__.py
        ├── camera.py
```

Naturally, the Camera class should be defined on `camera.py`.

## 2. local import

Inside the package, it is possible to use local imports. 
Imports based on '.' this position '..' the parent position.
For instance, a `from . import camera` will import the content of `camera.py`.

This way, the `__init__.py` file can redefine the Camera to make it available from an import of `scene2d`. 

```python
from . import camera

Camera= camera.Camera
```

At this point, _Pytest_ should work again just by changing `import scene2d` by `import src.scene2d` in the test files.

3. Implement Shapes

Ask the teacher...



