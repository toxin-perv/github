
# import pyautogui 
# from PIL import Image, ImageGrab 
# import time





# # def hit(key):
# #     pyautogui.keyDown(key)
    


# # def iscollide(data):
# #     for i in range(350, 370):
# #         for j in range(250, 300):
# #             if data[i, j] < 100:
# #                 return True
# #     return False


# def shot():
#     imagge = ImageGrab.grab()
#     imagge.show()




# if __name__ == "__main__": 
#     shot()
#     # print("Dino starts in 3 seconds.....") 
#     # time.sleep(3)
#     # hit("up") 
#     # while True:
#         # img = ImageGrab.grab().convert('L')
#         # data = img.load()
#         # if iscollide(data):
#         #     hit("up")

#         # for i in range(350, 370):
#         # for j in range(250, 300):           


import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(230, 310):
        for j in range(350, 390):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(230, 310):
        for j in range(400, 490):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
    
        # # Draw the rectangle for cactus
        # for i in range(230, 270):
        #     for j in range(350, 390):
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(230, 270):
        #     for j in range(400, 500):
        #         data[i, j] = 171

        # image.show()
        # break


