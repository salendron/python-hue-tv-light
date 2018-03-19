import cv2

cap = cv2.VideoCapture(0)
cap.set(3,32)
cap.set(4,24)
        
while True:
  _, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  cv2.imshow('my webcam', frame)
  if cv2.waitKey(1) == 27: 
    break  # esc to quit
            
cv2.destroyAllWindows()
