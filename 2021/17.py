
target_x = range(288, 331)
target_y = range(-96, -49)

def hits_target(vx,vy):
    x,y = 0,0
    y_max = 0
    while not (x in target_x and y in target_y):
        x += vx
        y += vy
        y_max = max(y_max,y)
        if vx > 0:
            vx -= 1
        vy -= 1
        if y < -97:
            return None
    return y_max

heights = [res for x in range(1,331) for y in range(-96,100) if (res:=hits_target(x,y)) is not None]
print('Part 1:', max(heights))
print('Part 2:', len(heights))
            
    

