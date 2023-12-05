

def compute_mapping_for_value(source, map_data):
    for coords in map_data:
        destination, src_start, range_length = coords[0], coords[1], coords[2]
        if src_start <= source < src_start + range_length:
            return destination + (source - src_start)
    return source

def p1():
    data_dict = {}
    current_map_name = None

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if 'seeds' in line:
                seeds = line.split(":")[0].strip()
                seednumbers = line.split(":")[1].strip()
                data_dict[seeds] = list(map(int, seednumbers.split(" ")))
            elif 'map' in line:
                current_map_name = line.split(":")[0].strip()
                data_dict[current_map_name] = []
            elif current_map_name and line:
                map_data = list(map(int, line.split()))
                data_dict[current_map_name].append(map_data)

    seednumbers = data_dict.get('seeds', [])

    locations = []

    for seed in seednumbers:
        source = seed
        for map_name in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map',
                         'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map',
                         'humidity-to-location map']:
            map_data = data_dict.get(map_name, [])
            source = compute_mapping_for_value(source, map_data)

        locations.append(source)
        print(f"Final value for seed {seed} is {source}")

    return min(locations)



def p2():
    data_dict = {}
    current_map_name = None

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if 'seeds' in line:
                _, seed_ranges_str = line.split(":")
                seed_ranges = seed_ranges_str.strip().split()
            elif 'map' in line:
                current_map_name = line.split(":")[0].strip()
                data_dict[current_map_name] = []
            elif current_map_name and line:
                map_data = list(map(int, line.split()))
                data_dict[current_map_name].append(map_data)

    locations = []

    for i in range(0, len(seed_ranges), 2):
        start = int(seed_ranges[i])
        length = int(seed_ranges[i + 1])
        for seed in range(start, start + length):
            source = seed
            for map_name in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map',
                             'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map',
                             'humidity-to-location map']:
                map_data = data_dict.get(map_name, [])
                source = compute_mapping_for_value(source, map_data)

            locations.append(source)

    return min(locations)




#print(p1())
print(p2())