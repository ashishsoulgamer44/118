import cv2
video= cv2.VideoCapture(0)

# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray ,1.2, 3 )
    print(bodies)
    for (x,y,w,h) in bodies:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)



    #Convert Each Frame into Grayscale
 
  
    # Pass frame to our body classifier
    
    
    # Extract bounding boxes for any bodies identified
    cv2.imshow('frame',frame)
      # cv2.waitKey(0)                                                  
    if cv2.waitKey(30)==32:

     cap.release()
     cv2.destroyAllWindows()
 