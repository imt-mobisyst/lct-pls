# Devoirs sur table

### UV-PARIS 2024

**Studiant name:** (First name _then_ FAMILLY NAME)

---

---

---

---

Expected answer in _FRENCH_ or _ENGLISH_.

<br />

## Operating System : (6 points)

1. **What is a terminal (or shell) ?** _(only one response)_

      &#9711; $\quad$ A kernel (Noyau in french) of an Operating System
<br />&#9711; $\quad$ A machine/computer
<br />&#9711; $\quad$ A text interface to the system
<br />&#9711; $\quad$ A file browser

<br />

2. **Connect the commands to their definitions**


```
cd        o                          o locates the binary and other resources

whereis   o                          o reports a snapshot of the current processes

who       o                          o changes the working directory

alias     o                          o an interface to the system reference manuals

ps        o                          o defines or display renamed commands

man       o                          o shows the open sessions (users logged on)
```

<br />

3. **What mean** `drwxr-xr-x` **and** `-rw-r-----` **resulting from command** `ls -lah` **?**

Part of the command output:
```sh
...
drwxr-xr-x   2 root root   4,0K juin  28 07:26 sensors.d
-rw-r--r--   1 root root    13K mars  27  2021 services
drwxr-xr-x   3 root root   4,0K sept.  5 10:49 sgml
-rw-r-----   1 root shadow 1,5K juil. 10 10:42 shadow
-rw-r-----   1 root shadow 1,5K juil. 10 10:42 shadow-
...
```

response: 

---

---

---

---

---

---



<!--pageBreak-->

## Basic Programming : (10 points)

1. **Define a function:**

I need a function to find the closest elements in a list of values considering a given other value.


---

---

---

---

---

---

<br />

2. **Type:**

Python is dynamically typed. However provides an example of expected type of the parameters of the previously defined function.

---

---

---

---

---

---

3. **What is the output of the following code ?**<br />(the main idea is accepted if you cannot provide the exact output)

```python
class aClass:

      def __init__(self):
            self._anAttribute= 0

      def setAttribute(self, aValue):
            self._anAttribute= aValue
            return self

      def attribute(self):
            return self._anAttribute

anInstance= aClass()
anInstance.setAttribute(23)

print( anInstance.attribute() )
print( anInstance )
```

---

---

---

---

<br />

<!--pageBreak-->

4. **What is the output of the following code ?**<br />(the main idea is accepted if you cannot provide the exact output)

```python
def generateData(n=100):
	data= [ x for x in range(n) ]
	
generateData(5)
print( data )
```

---

---

---

---

<br />

5. **Example code:**

Knowing that, $\mathit{random}$ is a python module including the function $\mathit{choice}$ I need. The
documentation says $\mathit{choice}(\mathit{aList})$ return a random element of the list $\mathit{aList}$.

Provide a complete short program that illustrates the use of this function.

---

---

---

---

---

---

<!--pageBreak-->

## Object-Oriented Programming : (4 points)

You are mandated by GIEC experts to model and simulate climate change.
The simulator requires a python package to model the different sources of CO2 emission.

Whatever the source, the `plotCO2Generation` method must plot its CO2 emission.
The generated plot is for a given horizon (i.e. number of months), where a month is represented by one point in the plot.
This method relies on another method called `estimateMonthCO2` which takes additional parameters as simulation state.
`estimateMonthCO2` needs to be defined for each source type because the mechanism of CO2 production are generally different.

Three kinds of sources identified by the GIEC are Farm, Forest and Volcano.
Each of these 3 types of sources follows its own rules in terms of CO2 emission (different implementations of `estimateMonthCO2`).

In addition to these sources, the GIEC has also identified industrial sources.
The main particularity for all these industrial sources is that they are owned by a company.
Consequently, the GIEC needs to access the company name by calling a method called `companyName`.
GIEC consider 2 specialized industrial sources: Mine and Manufacture.
This 2 source types have its own CO2 estimation mechanisms (different between Mine and Manufacture).

1. Propose a graphical representation of the class structure. Classes are represented as boxes, have a name in the box' header and have their defined methods indicated (only the mentioned method and only their names).

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---


2. We want to implement this in a python package with a maximum of different files. What would be the tree structure of the python package ?

---

---

---

---

---

---

---

---


---

---
