# System and Python Basis - Exercises

## 1. Exercise: Search for a User's Groups

Create a script returning the names (print) of all groups associated with the user.

Always process in an incremental way:

- Decompose the module to develop
- Implement it step by step
- Test the solution at each step


### Initialize your project:

- Make a new directory : `python-data-science` for instance.
- Edit a new Python file: `search-group.py` with *gedit* for instance.
- Test a *hello-world* script `python3 search-group.py`


### Load ressources

- Open a file and read-it line by line
- Apply it to `/etc/passwd` then `/etc/group`

I do not know how to open a file ? search the web... [w3schools](https://www.w3schools.com/python/python_file_handling.asp)


### Search for a specific word (user name) in a lines

- Detect for `instald` user in lines
- Print only lines with `instald` inside

There is a lot of string methods in Python (for instance, still in [W3School](https://www.w3schools.com/python/python_strings_methods.asp))
and one of them seems very interesting: `find()`.

Another one `split()` allows for decomposing a long string regarding a separator character.


### Reduce to user's Groups

- Select only the primary group name in `/etc/passwd` file for the user `bob`.
- Select each group name in `/etc/groups`, each time `bob` is present.


---

##  2. Exercise: Script as a shell command


The goal is to transform `search-group.py` code into a shell command, executable like anyother.


### Get user name as a command argument


For that, use the `sys.argv` from the Python package `sys`. This variable provides the list of the command line arguments.


### In the Shell

We aim to call our program by masking the need for the _Python3_ interpreter. 
Like that: 

```shell
search-user bob
```

- Version 1 : By using an `alias` (typically `alias search-user='python3 search-user.py'`)
- Version 2 : By using a [shebang](https://fr.wikipedia.org/wiki/Shebang), to identify the interpreter inside the Python script, and by setting the script executable `chmod +x`.


### Anywhere

The script is only accessible from the current directory. 
Resolve this problem

- Version 1 : Modify the `alias` definition with a global path to the script.
- Version 2 : Add the current directory to the _PATH_ variable (`export PATH=$PATH:~/path/to/`)


### Anytime

The _alais_ or _exports_ are not available in a new shell. 
To make them automatically defined, you may add the appropriate lines to your local `.bashrc` file. 
This file allows the users to tune their bash shell at start time.


## Exercise: Increased Command

- `split()` is restrictive much for extracting some element from a string ? Take a look at Regular Expression in _Python_ [w3school](https://www.w3schools.com/python/python_regex.asp)
- Handle bugs (no user name in arguments, ...)
- Add options to your command: *--help* or *-h* for help, **-i** for printing group ids, **-t** to test if the user is in a specific group, ...

- Make a new directory : `python-data-science` for instance.
- Edit a new Python file: `search-group.py` with *gedit* for instance.
- Test a *hello-world* script `python3 search-group.py`

<!--

### Load ressources

- Open a file and read-it line by line
- Apply it to `/etc/passwd` then `/etc/group`

I do not know how to open a file ? search the web... [w3schools](https://www.w3schools.com/python/python_file_handling.asp)


### Search for a specific word (user name) in a lines

- Detect for `bob` user in lines
- Print only lines with `bob` inside

There is a lot of string methods in Python (for instance, still in [W3School](https://www.w3schools.com/python/python_strings_methods.asp))
and one of them seems very interesting: `find()`.

Another one `split()` allows for decomposing a long string regarding a separator character.


### Reduce to user's Groups

- Select only the primary group name in `/etc/passwd` file for the user `bob`.
- Select each group name in `/etc/groups`, each time `bob` is present.


---

##  2. Exercise: Script as a shell command


The goal is to transform `search-group.py` code into a shell command, executable like anyother.


### Get user name as a command argument


For that, use the `sys.argv` from the Python package `sys`. This variable provides the list of the command line arguments.


### In the Shell

We aim to call our program by masking the need for the _Python3_ interpreter. 
Like that: 

```shell
search-user bob
```

- Version 1 : By using an `alias` (typically `alias search-user='python3 search-user.py'`)
- Version 2 : By using a [shebang](https://fr.wikipedia.org/wiki/Shebang), to identify the interpreter inside the Python script, and by setting the script executable `chmod +x`.


### Anywhere

The script is only accessible from the current directory. 
Resolve this problem

- Version 1 : Modify the `alias` definition with a global path to the script.
- Version 2 : Add the current directory to the _PATH_ variable (`export PATH=$PATH:~/path/to/`)


### Anytime

The _alais_ or _exports_ are not available in a new shell. 
To make them automatically defined, you may add the appropriate lines to your local `.bashrc` file. 
This file allows the users to tune their bash shell at start time.


## Exercise: Increased Command

- `split()` is restrictive for extracting some element from a string ? Take a look at Regular Expression in _Python_ [w3school](https://www.w3schools.com/python/python_regex.asp)
- Handle bugs (no user name in arguments, ...)
- Add options to your command: *--help* or *-h* for help, **-i** for printing group ids, **-t** to test if the user is in a specific group, ...

-->