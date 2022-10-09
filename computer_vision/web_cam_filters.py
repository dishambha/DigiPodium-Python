import cv2

def start_camera(cam_id = 0):
    camera = cv2.VideoCapture(cam_id)
    while camera.isOpened():
        _, image = camera.read()  #if there is a dull word we can write '_' in place of the word
        image2 = image * 255
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imshow("Web Cam Output",image)
        cv2.imshow("Image2",image2)
        cv2.imshow("GREY",grey)
        cv2.imshow("RGB",rgb)
        if cv2.waitKey(1) == 27: # 27 is esc 13 is for enter
            break
    camera.release()#free up the camera
    cv2.destroyAllWindows()#close all windows

start_camera()
