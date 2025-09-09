# Developper tools


## Python, a Modular tool

**resources:** `myOwnPkg.py`

```python
def myWonderfullFunction( aFirstIntergerPaprameter, aSecondIntergerParameters )
    intergerSum= aFirstIntergerPaprameter + aSecondIntergerParameters
    return intergerSum

```

**script:** `myOwnCommand.py`

```python
import myOwnPkg

...

b= myOwnPkg.myWonderfullFunction( a, 40 )
...

```

---
<!-- --------------------------------------------------------------- -->

## Python, a Modular tool

- Python packages are easy to install with `pip` tool.

```sh
pip install tqdm pytest
```

- python _import_ relies on environment path variable:

```python
import sys
print( sys.path )
```

---
<!-- --------------------------------------------------------------- -->

