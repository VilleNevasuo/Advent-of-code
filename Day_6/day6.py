
markers = []

with open("data.txt", "r") as file:
    for line in file:
        for index, char in enumerate(line.strip()):
            markers.append(char)
            if len(markers) == 4:
                if len(markers) == len(set(markers)):
                    print(index+1, markers)
                    quit()
                del markers[0]
