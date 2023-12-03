

def p1():

    with open("input.txt") as file:
        grid = []
        for line in file:
            gridline = []
            line = line.strip()
            gridline.append(line)
            grid.append(gridline)
        print(grid)
    
    return 0


def p2():
    
    return 0


print(p1())
print(p2())