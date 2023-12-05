with open('data/5.txt') as f:
    seeds = f.readline().strip().split(': ')[1].split()
    next(f)

    line = f.readline().strip()
    seed_soil = []
    while line:
        if line := f.readline().strip():
            seed_soil.append(line.split())

    line = f.readline().strip()
    soil_fert = []
    while line:
        if line := f.readline().strip():
            soil_fert.append(line.split())

    line = f.readline().strip()
    fert_water = []
    while line:
        if line := f.readline().strip():
            fert_water.append(line.split())

    line = f.readline().strip()
    water_light = []
    while line:
        if line := f.readline().strip():
            water_light.append(line.split())

    line = f.readline().strip()
    light_temp = []
    while line:
        if line := f.readline().strip():
            light_temp.append(line.split())

    line = f.readline().strip()
    temp_humid = []
    while line:
        if line := f.readline().strip():
            temp_humid.append(line.split())

    line = f.readline().strip()
    humid_loc = []
    while line:
        if line := f.readline().strip():
            humid_loc.append(line.split())

    maps = (seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc)


def get_value(key, map_):
    for contig in map_:
        dest, source, range_ = map(int, contig)
        if source <= key <= source+range_:
            return key + dest - source        
    return key

def find_location(seed, maps):
    ans = seed
    for map in maps:
        ans = get_value(ans, map)
    return ans


print(min(find_location(int(seed), maps) for seed in seeds))