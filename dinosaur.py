
import pyautogui 
from PIL import Image, ImageGrab 
import time
# from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)


# def draw():
#     for i in range(100, 200):
#         for j in range(200, 300):
#             pass


def iscollide(data):
    for i in range(350, 370):
         for j in range(250, 300):
            if data[i, j] < 100:
                return True
    return False
        





if __name__ == "__main__": 
    print("Dino starts in 3 seconds.....") 
    time.sleep(3)
    hit("up") 
    while True:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        if iscollide(data):
            hit("up")
        # print(asarray(img))
        # for i in range(350, 370):
        #     for j in range(250, 300):
        #         data[i, j] = 0
        
        
        # img.show()