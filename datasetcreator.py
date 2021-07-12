import numpy as np
import cv2
import random
import pandas as pd

def clickevent(event, x, y, flag, params):
    global points, draw, colors, color, cluster
    #if event == cv2.EVENT_MOUSEMOVE:
    #print(event)
    events.append(event)
    if events[-1]==4 and events[-2]==1:
        if draw == True:
            draw = False
        else:
            draw = True
            color = colors.pop()
            cluster+=1
    if draw == True:
        if random.random() > 0.8:
            #points.append((x,y))
            #img[y,x,0],img[y,x,1],img[y,x,2] = 255,255,255
            for i in range(2):
                if random.random() >0.6:
                    center = (x+random.randint(10,30),y+random.randint(10,30))
                    points.append([center[0],center[1],cluster])
                    cv2.circle(img,center,2,color,-1)
                    cv2.imshow("frame",img)
        else:
            cv2.imshow("frame",img)

    
img = np.zeros((512,512,3),np.uint8)
cv2.imshow("frame",img)
events = []
points = []
draw = False
colors = [(255,255,255),(255,0,0),(0,255,0),(0,0,255)]
color = 0
cluster = 0
cv2.setMouseCallback("frame",clickevent)

cv2.waitKey(0)
cv2.destroyAllWindows()
print(len(points))
print(points[0:5])

df = pd.DataFrame(points,columns=["x","y","class"])
#df = random.shuffle(df)
df = df.sample(len(df))
df.reset_index(inplace=True)
df.drop("index",axis=1,inplace=True)
print(df)
df.to_csv("Generated_data.csv")