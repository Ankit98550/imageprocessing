# Accessing and Manipulating Pixels
"""import cv2
cam=cv2.VideoCapture(0)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) # convert to integer
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)
output_file="image/recording.mp4"
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
output=cv2.VideoWriter(output_file,fourcc,fps,(width,height))


while True:
    _,frame=cam.read()
    cv2.imshow('Webcam',frame)
    output.write(frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
output.release()
cv2.destroyAllWindows()
"""

"""import cv2
import numpy as np

line =np.zeros((300,300,3),dtype=np.uint8)
arrow = line.copy()
polyLine = line.copy()
rectangle = line.copy()
circle = line.copy()
text = line.copy()

p1 = [100,100]
p2 = [200,200]
p3 = [200,100]
p4 = [100,200]
points = np.array([p1,p2,p3,p4]) 

cv2.line(line,p1,p2,(0,255,0),2)
cv2.arrowedLine(arrow,p1,p2,(0,255,0),2)
cv2.polylines(polyLine,[points],False,(0,255,0),2)
cv2.rectangle(rectangle,p1,p2,(0,255,0),2)
cv2.circle(circle,(150,150),50,(0,255,0),2)
cv2.putText(text,'sample_text', p4, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0))

cv2.imshow('line',line)
cv2.imshow('arrow',arrow)
cv2.imshow('polyLine',polyLine)
cv2.imshow('rectangle',rectangle)
cv2.imshow('circle',circle)
cv2.imshow('text',text)

cv2.waitKey() # Wait untill a key press
cv2.destroyAllWindows()"""


# interacting with the video
"""import cv2
import numpy as np

def mouseClick(event, xPos, yPos,flags, param):
    print(event,xPos,yPos,flags,param)

frame=np.zeros((500,500),np.uint8)
cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME',mouseClick)

while True:
    cv2.imshow('FRAME',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()"""

# Draw a rectangle with Mouse
"""import cv2
import numpy as np

draw=False
p1=(0,0)
p2=p1

def mouseClick(event,xPos,yPos,flags,param):
    print(event,xPos,yPos,flags,param)
    global draw,p1,p2

    if event==cv2.EVENT_LBUTTONDOWN:
        draw=True
        p1=(xPos,yPos)
        p2=p1
    if event==cv2.EVENT_MOUSEMOVE and draw:
        p2=(xPos,yPos)

    if event==cv2.EVENT_LBUTTONUP:
        draw=False

frame=np.zeros((500,500,3),np.uint8)
cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME',frame)
while True:
    frame = np.zeros((500,500,3), np.uint8) 
    cv2.rectangle(frame,p1,p2,(0,255,0),2)
    cv2.imshow('FRAME',frame)
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cv2.destroyAllWindows()"""

a=[1,2,3]
a=tuple(a)
a[0]=2
print(a)