# Launching the camera
import cv2
"""# to open the camera using VideoCapture function
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()"""

# getting video properties like height, resolution, frame per second
"""
cam=cv2.VideoCapture(0)
width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cam.get(cv2.CAP_PROP_FPS)

while True:
    i, frame=cam.read()
    cv2.imshow("webcam",frame)
    print("resolution:",width, 'resoution',height,"FPS",fps)
    if cv2.waitKey(1) & 0xff ==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()"""

# Changing Video Properties:
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cam.set(cv2.CAP_PROP_FPS,15)

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cam.get(cv2.CAP_PROP_FPS)

while True:
    i,frame=cam.read()
    cv2.imshow("webcam",frame)
    print("resolution:",width, 'resoution',height,"FPS",fps)
    if cv2.waitKey(1) & 0xff ==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()


