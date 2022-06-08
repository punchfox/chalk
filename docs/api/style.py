import sys
sys.path.append("/home/srush/Projects/diagrams/venv/lib/python3.9/site-packages")
import math
from chalk import *
from colour import Color
blue = Color("blue")
orange = Color("orange")



# ### Diagram.fill_color

help(Diagram.fill_color)

#

triangle(1).fill_color(blue)

# ### Diagram.fill_opacity

help(Diagram.fill_opacity)

#

triangle(1).fill_color(blue).fill_opacity(0.2)


# ### Diagram.line_color

help(Diagram.line_color)

#

triangle(1).line_color(blue)

# ### Diagram.line_width

help(Diagram.line_width)

#

triangle(1).line_width(0.05)


# ### Diagram.dashing

help(Diagram.dashing)

#

triangle(1).dashing([0.2, 0.1], 0) 


# ### Advanced Example


# Example: Outer styles override inner styles

(triangle(1).fill_color(orange) | square(2)).fill_color(blue)
