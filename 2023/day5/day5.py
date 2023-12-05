

def p1():


    data_dict = {}
    
    map_data_structures = {
        'seed-to-soil map': {},
        'soil-to-fertilizer map': {},
        'fertilizer-to-water map': {},
        'water-to-light map': {},
        'light-to-temperature map': {},
        'temperature-to-humidity map': {},
        'humidity-to-location map': {}
    }

    current_map_name = None
    with open("input.txt") as file:
        for coords in file:
            coords = coords.strip()
            if 'seeds' in coords:
                seeds = coords.split(":")[0].strip()
                seednumbers = coords.split(":")[1].strip()
                data_dict[seeds] = list(map(int, seednumbers.split(" ")))
            if 'map' in coords:
                current_map_name = coords.split(":")[0].strip()
                data_dict[current_map_name] = []
            elif current_map_name and coords:
                map_data = list(map(int, coords.split()))
                data_dict[current_map_name].append(map_data)
    
    
    print(data_dict)
    for map_name, values in data_dict.items():
        print(f'processing {map_name}')
        if type(values[0]) is list:
            for coords in values:
                source, destination, range_length = coords[1], coords[0], coords[2]
                for i in range(range_length):
                    map_data_structures[map_name][source + i] = destination + i
    
    seednumbers = [int(num) for num in seednumbers.split(" ")]


    locations = []

    for seed in seednumbers:
        source = seed
        for map_name in map_data_structures.keys():
            current_map = map_data_structures[map_name]
            source = current_map.get(source, source)

        locations.append(source)
        print(f"Final value for seed {seed} is {source}")

    return min(locations)

def p2():
    
    return 0


print(p1())
#print(p2())