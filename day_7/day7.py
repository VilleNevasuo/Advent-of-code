
d = {}
folder = ""

with open("test.txt", "r") as file:
    for line in file:
        line = line.strip()
        data = line.split(" ")

        if data[1] == "cd":
            folder = data[2]
            d[data[2]] = 0
        elif data[0].isnumeric():
            d[folder] += int(data[0])

print(d)
