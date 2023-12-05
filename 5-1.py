from icecream import ic
from collections import defaultdict

class DefaultDict(defaultdict):
    def __missing__(self, key):
        return self.default_factory(key)

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

    
# print(seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc)

def inp_to_map(inp):
    final = DefaultDict(lambda key: key)
    for line in inp:
        dest, source, rge = map(int, line)
        final.update({x: x + dest - source for x in range(source, source+rge)})    
    # for i in range(max(final.keys())):
    #     if i not in final:
    #         final[i] = i    
    return final


seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = map(inp_to_map, (seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc))

def find_location(seed, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc):
    return humid_loc[temp_humid[light_temp[water_light[fert_water[soil_fert[seed_soil[seed]]]]]]]

# ic(find_location(79, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc))
# ic(find_location(14, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc))
# ic(find_location(55, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc))

l = []
for seed in seeds:
    try:
        l.append(find_location(int(seed), seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc))
    except:
        ic(seed, 'error')

print(min(l))