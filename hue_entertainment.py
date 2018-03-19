from camera_capture import CameraCapture
import time, cv2
from lights import setLight
from colors import frameToColorMapImage, getRGBXYBri

def main():
    cam = CameraCapture()
    cam.start()
    
    lastState=[
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ]
    first = 0
    
    while True:
        frame = cam.get_frame()
        if  frame != None:
            #cv2.imshow('my webcam', frame)
            
            colorMapImage = frameToColorMapImage(frame)
            #colorMapImage.save("/home/bruno/color.jpg")
            
            light_idx = 0
            
            for img_x in range(3):
                r,g,b,x,y,bri = getRGBXYBri(colorMapImage,[img_x,1])
                
                lastR = lastState[light_idx][0]
                lastG = lastState[light_idx][1]
                lastB = lastState[light_idx][2]
                
                if abs(r - lastR) > 40 or abs(g - lastG) > 40 or abs(b - lastB) > 40 or first < 6 or bri == 0:
                    try:
                        setLight(light_idx,x,y,bri)
                        lastState[light_idx][0] = r
                        lastState[light_idx][1] = g
                        lastState[light_idx][2] = b
                        first = first + 1
                        print "set"
                    except Exception as ex:
                        print "Failed to set light: " + str(ex)
                        time.sleep(0.5)
                else:
                    print "skipped"
                    
                light_idx = light_idx + 1
        
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    
    
