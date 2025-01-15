import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)
pTime = 0
mpDraw = mp.solutions.drawing_utils
mpFaceMesh  = mp.solutions.face_mesh
FaceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpace = mpDraw.DrawingSpec(thickness=1,circle_radius=1)

while True:
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = FaceMesh.process(imgRGB)
    if result.multi_face_landmarks:
        for faceLms in result.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms,mpFaceMesh.FACEMESH_CONTOURS,drawSpace,drawSpace)


# gat this point in face to draw
            for lm in faceLms.landmark:
                # print(lm)
                ih , iw, ic = img.shape
                x,y = int(lm.x*iw),int(lm.y*ih)
                print(id,x,y)

                
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'fps:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)





    cv2.imshow("Image",img)
    cv2.waitKey(1)

