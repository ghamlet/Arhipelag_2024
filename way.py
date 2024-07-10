from geobot_sdk import *


MAP_BLOCK_LIST = [
        (-3.9, 0.7),
        (-2.4, -1.15),
        (-2.8, 0.5),
        (-2.6, 0.5),
        (-2.65, 1.6),
        (-2, -2)
    ]


def init_bot():
    bot = None
    return bot

   

def init_MAP(start_x, start_y, end_x, end_y):
    m = Map()
    m.create_map(22,11, 11)


    for blockPoint in MAP_BLOCK_LIST:
        m.add_block(Point(blockPoint[0], blockPoint[1]))

    startPoint = Point(start_x, start_y)
    endPoint = Point(end_x, end_y)

    tr = m.get_trajectory(startPoint, endPoint)
    return tr


def move_geobot(tr, bot):
    k = 0

    while k != len(tr):
        bot.go_to_local_point(tr[k].x, tr[k].y)

        while not bot.point_reached():
            pass

        print(f"reached: {tr[k].x} {tr[k].y}") 
        k += 1   



    bot.emergency_detection()


def GEOBOT(start_x, start_y, end_x, end_y):
    print("start Geobot")

    bot = init_bot()
    trajectory = init_MAP(start_x, start_y, end_x, end_y)
    move_geobot(trajectory, bot)

   