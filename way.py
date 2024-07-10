from geobot_sdk import *


MAP_BLOCK_LIST = [
(0.04, -0.04),
(0.25, -0.18),
(-0.35, -0.87),
(1.22, -0.91),
(0.46, -1.82),
(-0.42, -1.82),
(-0.17, -1.94),
(-0.77, -2.9),
(-0.11, -2.92),
(-0.79, -3.9),
(1.08, -3.16),
(1.83, -2.33),
(2.83, -1.42),
(4.17, -1),
(2.14, -0.01),
(2.4, -0.11),
(1.81, 0.4),
(2.62, 0.78),
(1.95, 2.08),
(2.98, 2.09),
(4, 2.13),
(1.94, 4,14),
(-2.31, -3.67),
(-3.26, -1.91),
(-4.36, -1.76),
(-2.12, -1.5),
(-1.5, -0.67),
(-1.24, -0.83),
(-2.71, -0.16),
(-3.99, 0.86),
(-3.72, 0.72),
(-1.04, 0.53),
(-2.97, 1.58),
(-2.28, 2.09),
(-1.43, 1.73),
(-1.16, 1.60),
(-3.32, 2.88),
(-3.05, 2.72),
(-1.60, 2.92),
(-2.23, 4.11),
(0, 1.51),
(0.36, 2.87),
(-0.13, 3.97),
(0.85, 0.26)

]


START_POS_GEOBOT = (-3, -4)

CAT_X, CAT_Y = 2, 2

def init_bot():
    bot = None
    return bot
   

def create_map(END_X, END_Y):
    m = Map()
    m.create_map(15,11, 11) #первый аргумент дробление шага, чем он больше тем шаг обхода препятсвия больше


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

