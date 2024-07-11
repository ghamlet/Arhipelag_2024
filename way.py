from geobot_sdk import *


MAP_BLOCK_LIST  =  [(-0.777681, -3.905615), (-2.299109, -3.696187), (-3.231148, -1.952335), (-4.381873, -1.800591), (-1.334348, -0.751029), (-2.750625, -0.194634), (-3.812833, 0.74112), (-0.942343, 0.538795), (-2.915015, 1.512485), (-1.255862, 1.676032), (-2.312713, 2.043972), (-3.181678, 2.779853), (-1.545518, 2.889452), (-2.242256, 4.095045), (-0.165873, 3.918541), (0.327294, 2.843688), (0.049097, 1.566509), (0.023807, 1.503283), (0.213486, -0.229128), (0.807817, 0.226104), (-0.355553, -0.949911), (1.250404, -0.975202), (0.479038, -1.809794), (-0.267036, -1.923602), (-0.026775, -2.998455), (1.073369, -3.137554), (1.85738, -2.328253), (2.894297, -1.392498), (4.15883, -1.051074), (2.312611, -0.127965), (1.819444, 0.339912), (2.666681, 0.782499), (4.007086, 2.084968), (3.033395, 2.021741), (1.996478, 2.097613), (2.122932, 4.032349)]
# points_file = "/home/arrma/Documents/points.txt"


# with open(points_file, "r") as file:
#     for line in list(file)[2:]:
#         line = line.split()
#         MAP_BLOCK_LIST.append((float(line[2]), float(line[3])))

# print(MAP_BLOCK_LIST)



START_POS_GEOBOT = (-3, -4)

CAT_X, CAT_Y = 1.25, 1.5

def init_bot():
    bot = None
    return bot
   

def create_map(END_X, END_Y):
    m = Map()   #64 ok
    m.create_map(110,11, 11) #первый аргумент дробление шага, чем он больше тем шаг обхода препятсвия больше


    for blockPoint in MAP_BLOCK_LIST:
        m.add_block(Point(blockPoint[0], blockPoint[1]))

        startPoint = Point(START_POS_GEOBOT[0], START_POS_GEOBOT[1])
        endPoint = Point(END_X, END_Y)

        tr = m.get_trajectory(startPoint, endPoint)
        tr.append(endPoint)

        print(tr)

        return tr


def move_geobot(bot, tr):
    k = 0

    while k != len(tr)+1:
        bot.go_to_local_point(tr[k].x, tr[k].y)

        while not bot.point_reached():
            pass

        print(f"reached: {tr[k].x} {tr[k].y}") 
        k += 1   


    bot.emergency_detection()


def GEOBOT(END_X, END_Y):
    bot = init_bot()
    tr = create_map(END_X, END_Y)
    move_geobot(bot, tr)



if __name__ == "__main__":
    GEOBOT(CAT_X, CAT_Y)

