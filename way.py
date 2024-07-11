from geobot_sdk import *
import time

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
   

def create_map(): #убрал END_X END_Y
    new_tr = []
    m = Map()   #64 ok
    m.create_map(110,11, 11) #первый аргумент дробление шага, чем он больше тем шаг обхода препятсвия больше


    for blockPoint in MAP_BLOCK_LIST:
        m.add_block(Point(blockPoint[0], blockPoint[1]))

    startPoint = Point(START_POS_GEOBOT[0], START_POS_GEOBOT[1])
    endPoint = Point(CAT_X, CAT_Y)

    tr = m.get_trajectory(startPoint, endPoint)
    tr.append(endPoint)

    for coord in tr:
        x, y = round(coord.x, 3), round(coord.y, 3)
        # print(x, y)

        new_tr.append(Point(x, y))


    print(new_tr)
    return new_tr




def move_geobot(bot, tr):
    k = 0

    while k != len(tr)+1:
        bot.go_to_local_point(tr[k].x, tr[k].y)

        # prev_x, prev_y = None, None
        # once = True
        # start_time = None
        # STOP = False

        while not bot.point_reached():
            pass

            # cur_x, cur_y, cur_z = bot.get_local_position_lps() # получаем координаты шеобота каждый раз пока он не доехал до нужной точки
            
            # if prev_x is None:
            #     prev_x , prev_y = cur_x, cur_y

            
            # else:
            #     if (prev_x - 0.05 <= cur_x <= prev_x +0.05 ) and (prev_y - 0.05 <= cur_y <= prev_y +0.05):
            #         if once:
            #             start_time = time.time() 
            #             once = False

            #         prev_x , prev_y = cur_x, cur_y

            #         if start_time:
            #             if time.time() - start_time > 10:
            #                 STOP = True
            #                 block_x, block_y = cur_x, cur_y
            #                 prev_trk_x = tr[k-1].x
            #                 prev_trk_y = tr[k-1].y

            #     else:
            #         STOP = False
            #         once = True


        
        print(f"reached: {tr[k].x} {tr[k].y}") 
        k += 1   


    bot.emergency_detection()


def GEOBOT():
    bot = init_bot()
    tr = create_map()
    move_geobot(bot, tr)



if __name__ == "__main__":
    GEOBOT()

