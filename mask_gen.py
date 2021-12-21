from PIL import Image
import os
import numpy as np
from random import randint
import cv2

work = '/home/timur/Documents/Projects/Unet-for-Person-Segmentation'
back = work + '/background'
path_to_obj = work + '/fruits/gen/new_data'
img_test = '/home/timur/Documents/Projects/Unet-for-Person-Segmentation/ap.bmp'



def full_create(real, black, num):
    flag = False
    img = np.asarray(black)
    for i in range(len(img)):
        for j in range(len(img[i])):
            try:
                if (int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])) >= (255 * 3)-30:
                    black.putpixel((j, i), (0, 0, 0))
                else:
                    black.putpixel((j, i), (255, 255, 255))
                    real.putpixel((j, i), (int(img[i][j][0]), int(img[i][j][1]), int(img[i][j][2])))
            except:
                pass
            else:
                flag = True
    if flag == True:
        black.save(f'{work}/fruits/gen/mask/mask_{num}.bmp')
        real.save(f'{work}/fruits/gen/real/real{num}.bmp')
        flag = False


num = 0
for new_img in os.listdir(path_to_obj):
    backgr = back + '/' + f'{os.listdir(back)[randint(0, 24338)]}'
    real = Image.open(backgr)
    coords = [(int(real.size[0]-real.size[0]/4), 0), (0, 0), (0, int(real.size[1]-real.size[1]/4)),
              (int(real.size[0]-real.size[0]/4), int(real.size[1]-real.size[1]/4)),
              (int(real.size[0]/2-(real.size[0]/4)/2), int(real.size[1]/2-(real.size[1]/4)/2))]
    black = (np.zeros([real.size[0], real.size[1], 3], dtype=np.uint8)) * 0
    black.fill(255)
    black = Image.fromarray(black)
    rndm = randint(0, 4)
    image = Image.open(path_to_obj + '/' + new_img).resize((int((real.size[0])/4), int((real.size[1])/4)))
    black.paste(image, coords[rndm])
    full_create(real, black, num)
    num += 1
