points_file = "Agisoft_Metashape/points.txt"

MAP_BLOCK_LIST = []

with open(points_file, "r") as file:
    for line in list(file)[2:]:
        line = line.split()
        MAP_BLOCK_LIST.append((round(float(line[2]),2), round(float(line[3]),2)))

print(MAP_BLOCK_LIST)