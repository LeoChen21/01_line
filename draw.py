from display import *
import math

def draw_line( x0, y0, x1, y1, screen, color ):
    #makes it so the line is always drawn from left to right regardless of which x is bigger
    if x1 < x0:
        x, y, x1, y1 = int(x1), int(y1), int(x0), int(y0)
    else:
        x, y, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    
    
    A = 2 * (y1 - y)
    B = 2 * (x - x1)
    if B != 0:
        m = (y1 - y)/(x1 - x)

    #vertical lines
    if x1 - x == 0:
        while (y <= y1):
            plot(screen, color, x,y)
            y += 1

    #horizontal lines
    elif A == 0:
        while (x <= x1):
            plot(screen, color, x,y)
            x += 1
    
    #octant 1 & 5
    elif 0 < m <= 1:
        d = 2*A + B  
        while(x <= x1):
            plot(screen, color, x,y)

            if d > 0:
                y += 1 
                d += 2 * B 
          
            x += 1
            d += 2 * A
    #octant 2 & 6 
    elif m > 1:
        d = A + 2*B  
        while(y <= y1):
            plot(screen, color, x,y)

            if d < 0:
                x += 1 
                d += 2 * A 
          
            y += 1
            d += 2 * B
    #octant 3 & 7
    elif m < -1:
        d = A - 2*B  
        while(y >= y1):
            plot(screen, color, x,y)

            if d > 0:
                x += 1 
                d += 2 * A 
          
            y -= 1
            d -= 2 * B
    #octant 4 & 8
    else:
        d = 2*A - B  
        while(x <= x1):
            plot(screen, color, x,y)

            if d < 0:
                y -= 1 
                d -= 2 * B 
          
            x += 1
            d += 2 * A

    
    

