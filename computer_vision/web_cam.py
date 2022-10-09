import cv2

def start_camera(cam_id = 0):
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        status, image = camera.read()  #if there is a dull word we can write '_' in place of the word
        #print(status, image.shape) #_(under score)-> it is  a garbage collector
        cv2.imshow("Web Cam Output",image)
        if cv2.waitKey(1) == 27: # 27 is esc 13 is for enter
            break
    camera.release()#free up the camera
    cv2.destroyAllWindows()#close all windows
    
if __name__=='__main__':
    start_camera()


