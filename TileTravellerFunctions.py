def move(x,y,txt):
    if txt == 'n':
        y +=1
    elif txt == 's':
        y -=1
    elif txt == 'w':
        x -=1
    elif txt == 'e':
        x +=1
    tile = (x,y)
    return tile
out = move(1,1,'n')
print = (out)