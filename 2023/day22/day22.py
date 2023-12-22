import time

def calculate_final_position(grid):
    
    changes_made = False
    for i, brick in enumerate(grid):
        print("working with brick", i)
        solid_below_x = False
        solid_below_y = False
        #if at ground level we skip
        if i == 0:
            continue
        
        #check if there's nothing below
        if grid[i][2] - grid[i-1][2] > 1:
            print("nothing below lowering by 1. brick: ", i)
            time.sleep(1)
            grid[i][2] -= 1
            grid[i][5] -= 1
            changes_made = True
            continue
            
        #check below brick's x-axis
        for j in range(brick[0], brick[3]+1):
            cube_below_positions = list(range(grid[i-1][0],grid[i-1][3]+1))
            for pos in cube_below_positions:
                if j == pos:
                    solid_below_x = True
        
        #check below brick's y-axis
        for j in range(brick[1], brick[4]+1):
            cube_below_positions = list(range(grid[i-1][1],grid[i-1][4]+1))
            for pos in cube_below_positions:
                print("brick", i)
                print("current brick pos", j)
                print("below prick pos", pos)
                time.sleep(2)
                if j == pos:
                    solid_below_y = True
        
        if not solid_below_x:
            print("not solid under x lowering by 1. brick: ",i)
            time.sleep(1)
            changes_made = True
            grid[i][2] -= 1
            grid[i][5] -= 1
            continue
            
        if not solid_below_y:
            print("not solid under y lowering by 1. brick: ",i)
            time.sleep(1)
            changes_made = True
            grid[i][2] -= 1
            grid[i][5] -= 1
            continue
        
        for line in grid:
            print(line)
            time.sleep(0.5)
    
    print("returning", changes_made)
    print(grid)
    print(time.sleep(2))
    return changes_made

def p1():

    x_axis_view = [[0 for _ in range(10)] for _ in range(400)]
    y_axis_view = [[0 for _ in range(10)] for _ in range(400)]


    with open("input.txt") as file:
        grid = [[int(item) for item in line.replace('~',',').strip().split(',')] for line in file if line.strip()]

        sorted_grid = sorted(grid, key=lambda x: x[2])
        
        while True:
            changes_made = calculate_final_position(sorted_grid)
            if not changes_made:
                break



print(p1())