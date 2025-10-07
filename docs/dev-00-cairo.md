# Graphic Interlude with Cairo

This tutorial is a short parenthesis to present [cairo](https://cairographics.org) one of the numerous librairy allowing drawing.
_Cairo_ is a librairy written in _C_, dedicated to vectorial 2D drawing.


## 1. Get started: 

In follow, a simple example drawing a line, a rectangle. a triangle and a circle.
The _cairo_ python package can be installed with _pip_  (`pip install pycairo`).


```python 
import cairo, math

filePath= "drawing.png"
canvas= cairo.ImageSurface( cairo.Format.RGB24, 600, 400 )
context= cairo.Context( canvas )

# A Line
context.move_to( 0, 0 )
context.line_to( 200, 100 )

context.set_line_width( 4 )
context.set_source_rgb( 0.6, 1 , 0 )
context.stroke()

# A Rectangle :
context.move_to( 100, 110 )
context.line_to( 500, 110 )
context.line_to( 500, 290 )
context.line_to( 100, 290 )
context.close_path()

context.set_line_width( 3 )
context.set_source_rgb( 0.7, 0.7, 1.0 )
context.fill_preserve()
context.set_source_rgb( 0, 0.1 , 0.8 )
context.stroke()

# A triangle :
context.move_to( 300, 180 )
context.line_to( 350, 220 )
context.line_to( 250, 220 )
context.close_path()

context.set_source_rgb( 0, 0.1 , 0.8 )
context.fill()

# A triangle :
context.arc(450, 150, 20, 0, 2.0*math.pi)

context.set_source_rgb( 0.8, 0.1 , 0 )
context.stroke()

canvas.write_to_png( filePath )
```

Notice the particular syntaxe. 
First you move your pencil on a surfasse, then you fill and/or stroke the shape you drawing.
Filling or stroking also erase the pencil movement execpt if you use preserve functions.


## 2. Ressource: 

- pip page: [pypi.org/project/pycairo](https://pypi.org/project/pycairo/)
- official page: [cairographics.org](https://cairographics.org)
- Python tutorial: [on tortall.net](https://www.tortall.net/mu/wiki/CairoTutorial)

## 3. Play with it:

Try to draw something relaxing, a tree for instance.
