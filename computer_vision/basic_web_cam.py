import cv2

def start_camera(cam_id = 0):
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        status, image = camera.read()  
        #your code goes here
        cv2.imshow("Web Cam Output",image)
        if cv2.waitKey(1) == 27: # 27 is esc 13 is for enter
            break
    camera.release()#free up the camera
    cv2.destroyAllWindows()#close all windows
    