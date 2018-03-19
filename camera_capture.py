import threading, cv2

class CameraCapture(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.frame = None
        
    def get_frame(self):
        return self.frame

    def run(self):        
        cap = cv2.VideoCapture(0)
        cap.set(3,32)
        cap.set(4,24)
        while True:
            _, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.frame = frame
