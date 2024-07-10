from ultralytics import YOLO
import os
import cv2

from way import GEOBOT



path_to_model = "best.pt"
path_to_images = "/home/arrma/Documents/DataExample/"
path_to_coordinates = "/home/arrma/Documents/DataExample/"



def object_ground_coordinates(drone_x, drone_y, cat_x, cat_y):

    #размер изображения
    img_widht = 640
    img_hight = 480

    img_mid_x = img_widht /2
    img_mid_y = img_hight /2

    #размер местности на изображении
    ground_meters_x = 1.8 
    ground_meters_y = 1.2

    #масштаб изображения (метров в 1 пикселе)
    scale_x = ground_meters_x / img_widht 
    scale_y = ground_meters_y / img_hight

    #находим длину от середины снимка до кота в пикселях, а затем переводим в метры
    X = drone_x + (cat_x - img_mid_x) * scale_x
    Y = drone_y - (cat_y - img_mid_y) * scale_y
    print(f"coordinates of cat: {X} {Y}")

    return X, Y

   

def find_coord_of_drone(name_of_interest_file):
    with open(f"{path_to_coordinates}/coordinates.txt", "r") as f:
        for line in f:
            line = line.split()

            if line[0] == name_of_interest_file:
                x, y, z = list(map(float, line[1:]))
                print(f"coordinates of drone: {x} {y} {z}")
                return x, y,z

    

def load_model():
    print("model is loading...")
    model= YOLO(path_to_model)
    print("model loaded\n")
   
    return model


def main(model):
    files = os.listdir(path_to_images)
    #фильтрация снимков от файла с координатами
    files = [file for file in files if file[0] == "i"]
    print("fotos: ", files, "\n")


    for name_img in files:
        full_name = path_to_images + name_img

        img = cv2.imread(full_name)
        results = model.predict(source =img, conf = 0.8, verbose = False)[0]

        # names = model.names 
        # objects_found = results.boxes.cls

        annotated_frame = results.plot()


        if len(results.boxes.xywh.numpy()) != 0:
            print("detect")

            box = results.boxes.xywh.numpy()[0]
            cat_x ,cat_y, w, h = list(map(int, box))


            x, y, z = find_coord_of_drone(name_img)

            CAT_X, CAT_Y = object_ground_coordinates(x, y, cat_x, cat_y)


            GEOBOT(CAT_X, CAT_Y)


            # annotated_frame = cv2.circle(annotated_frame, (cat_x, cat_y), 5, (255,0,0), 5)

            # annotated_frame = cv2.circle(annotated_frame, (320, 240), 5, (255,0,255), 5)
            # cv2.putText(annotated_frame, "drone", (330, 240), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 255), 2)
            # cv2.imshow("detect", annotated_frame)

            # k = cv2.waitKey(10000) 
            # if k == ord("q"):
            #     break

            break




if __name__ == "__main__":
    model = load_model()
    main(model)
