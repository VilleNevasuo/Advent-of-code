

def drop_sand():

    resting_sand = 0
    sand_curr = [0, 500]

    while True:
        if cave[sand_curr[0]+1][sand_curr[1]] == "#":
            if cave[sand_curr[0]+1][sand_curr[1]-1] == ".":
                sand_curr[0] += 1
                sand_curr[1] -= 1

            elif cave[sand_curr[0]+1][sand_curr[1]+1] == ".":
                sand_curr[0] += 1
                sand_curr[1] += 1
            else:
                cave[sand_curr[0]][sand_curr[1]] = "#"
                resting_sand += 1
                sand_curr[0] = 0
                sand_curr[1] = 500
        else:
            sand_curr[0] += 1

        max_y = y
        for l in rock_coordinates:
            for coord in l:
                if coord[1] > max_y:
                    max_y = coord[1]

        if max_y < sand_curr[0]:
            return resting_sand


cave = []
rock_coordinates = []
with open("data.txt", "r") as file:
    for line in file:
        l = []
        line = line.strip().split(" -> ")
        for coord in line:
            coord = coord.split(",")
            l.append((int(coord[0]), int(coord[1])))
        rock_coordinates.append(l)

for i in range(1000):
    row = []
    for a in range(1000):
        row.append(".")
    cave.append(row)

for i in range(len(rock_coordinates)):
    for a in range(1, len(rock_coordinates[i])):
        if rock_coordinates[i][a][0] == rock_coordinates[i][a-1][0]:
            min_y = min(rock_coordinates[i][a][1], rock_coordinates[i][a-1][1])
            max_y = max(rock_coordinates[i][a][1], rock_coordinates[i][a-1][1])
            for fill in range(min_y, max_y+1):
                x = rock_coordinates[i][a][0]
                y = fill
                cave[y][x] = "#"
        else:
            min_x = min(rock_coordinates[i][a][0], rock_coordinates[i][a-1][0])
            max_x = max(rock_coordinates[i][a][0], rock_coordinates[i][a-1][0])
            for fill in range(min_x, max_x+1):
                x = fill
                y = rock_coordinates[i][a][1]
                cave[y][x] = "#"


resting_sand = 0

resting_sand = drop_sand()
print(resting_sand)
