import random
import numpy
import cv2

image = cv2.imread(r"E:\MY FILES\Wallpapers\1863d0a35e091-1db1A68645A0E056186.6DF93341C9DFDF35_message_424114256221508_1656696313365.jpg")
noised_img = image.copy()
height = image.shape[1]
width = image.shape[0]
probability_percent = float(input("Enter probability:"))
probability = probability_percent / 100



for y in range(height):
    for x in range(width):
        n = random.random()
        if n < probability:
            noise_r = random.randint(0,255)
            noise_g = random.randint(0,255)
            noise_b = random.randint(0,255)
            noised_img[x , y , 2] = noise_r
            noised_img[x , y , 1] = noise_g
            noised_img[x , y , 0] = noise_b


FastNLfilter = cv2.fastNlMeansDenoisingColored(noised_img , None , 9 ,9,20,30)


cv2.imshow("original" , image)
cv2.imshow("noised", noised_img)
cv2.imshow("FastNL", FastNLfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()