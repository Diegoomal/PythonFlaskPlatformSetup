import os
import cv2
import random
import datetime
import numpy as np

from skimage import io, img_as_ubyte
from skimage.transform import rotate, AffineTransform, warp
from skimage.util import random_noise


def rotation_anti_clockwise(image):
    angle = random.randint(0, 180)
    return rotate(image, angle)

def rotation_clockwise(image):
    angle = random.randint(0, 180)
    return rotate(image, -angle)

def h_flip(image):
    return np.fliplr(image)

def v_flip(image):
    return np.flipud(image)

def brightness(image):
    bright = np.ones(image.shape, dtype="uint8") * 70
    brightincrease = cv2.add(image, bright)
    return brightincrease

def blur_img(image):
    k_size = random.randrange(1, 10, 2)
    img_blur = cv2.medianBlur(image, k_size)
    return img_blur

def noise_img(image):
    return random_noise(image)

def zoom(image):
    zoom_value = random.random()
    hidth, width = image.shape[:2]
    h_taken = int(zoom_value*hidth)
    w_taken = int(zoom_value*width)
    h_start = random.randint(0, hidth-h_taken)
    w_start = random.randint(0, width-w_taken)
    image = image[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    image = cv2.resize(image, (hidth, width), cv2.INTER_CUBIC)
    return image

transformations = {
    'rotation_anti_horaria': rotation_anti_clockwise,
    'rotation_horaria': rotation_clockwise,
    'horizontal_flip': h_flip,
    'vertical_flip': v_flip,
    'brightness': brightness,
    'blur_img': blur_img,
    'noise': noise_img,
    'zoom': zoom
}

def execute_data_augmentation_operation_on_image_by_path(path_image:str):

    for transformation in list(transformations):
            
        transformed_image = transformations[transformation](
            io.imread(path_image)
        )

    #     transformed_image = img_as_ubyte(transformed_image)

    #     transformed_image = cv2.cvtColor(
    #         transformed_image, cv2.COLOR_BGR2RGB)



    #     path_dir, filename = os.path.split(path_image)

    #     _timestamp = datetime.datetime.now().timestamp()
    #     stimestamp = str(_timestamp).replace('.', '_')+".jpg"
        


    #     cv2.imwrite(
    #         os.path.join(path_dir, stimestamp),
    #         transformed_image
    #     )
