

def move_vertically(matrix, line, head_pos, tail_pos):

    to_move = int(line[1])
    for i in range(to_move):
        if line[0] == "U":
            head_pos[0] -= 1
            if tail_pos[0] - head_pos[0] > 1:
                if head_pos[1] != tail_pos[1]:
                    tail_pos[1] = head_pos[1]
                tail_pos[0] -= 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"
        else:
            head_pos[0] += 1
            if head_pos[0] - tail_pos[0] > 1:
                if head_pos[1] != tail_pos[1]:
                    tail_pos[1] = head_pos[1]
                tail_pos[0] += 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"

    return head_pos, tail_pos, matrix


def move_horizontally(matrix, line, head_pos, tail_pos):

    to_move = int(line[1])
    for i in range(to_move):
        if line[0] == "R":
            head_pos[1] += 1
            if head_pos[1] - tail_pos[1] > 1:
                if head_pos[0] != tail_pos[0]:
                    tail_pos[0] = head_pos[0]
                tail_pos[1] += 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"
        else:
            head_pos[1] -= 1
            if tail_pos[1] - head_pos[1] > 1:
                if head_pos[0] != tail_pos[0]:
                    tail_pos[0] = head_pos[0]
                tail_pos[1] -= 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"

    return head_pos, tail_pos, matrix


matrix = [["." for i in range(800)] for j in range(800)]
count = 0

knots = []
knot = [400, 400]
for i in range(10):
    knots.append(knot)

print(knots)

matrix[400][400] = "#"

with open("test.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        for i in range(len(knots)):
            if i == 0:
                continue
            if line[0] == "U" or line[0] == "D":
                head_pos, tail_pos, matrix = move_vertically(
                    matrix, line, knots[i-1], knots[i])
            else:
                head_pos, tail_pos, matrix = move_horizontally(
                    matrix, line, knots[i-1], knots[i])
            
            knots[i-1] = head_pos
            knots[i] = tail_pos
        print(knots)


for line in matrix:
    for el in line:
        if el == "#":
            count += 1
print("tiles visited", count)
