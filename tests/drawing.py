import cairo, math

filePath= "drawing.png"
canvas= cairo.ImageSurface( cairo.Format.RGB24, 600, 400 )
context= cairo.Context( canvas )

# A Line
context.set_line_width( 4 )
context.move_to( 0, 0 )
context.line_to( 200, 100 )
context.set_source_rgb( 0.6, 1 , 0 )
context.stroke()

# A Rectangle :
context.set_line_width( 3 )
context.move_to( 100, 110 )
context.line_to( 500, 110 )
context.line_to( 500, 290 )
context.line_to( 100, 290 )
context.close_path()
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
