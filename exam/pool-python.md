
1. **What pip or pip3 is for ?** (one or several answers accepted)

    &#9634; Install python packages
    <br />&#9634; Configure shell environement
    <br />&#9634; Execute python test scrips
    <br />&#9634; Interpret python programe
    <br />&#9634; Manage python resources

<br />


## Problem - GIEC

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
