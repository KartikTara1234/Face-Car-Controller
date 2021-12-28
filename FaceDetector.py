# import cv2
# import torch
# from facenet_pytorch import MTCNN
# import numpy as np

# class FaceDetection(object):
#     def __init__(self, mtcnn):
#         self.mtcnn = mtcnn

#     def _draw(self, frame,boxes,probs,landmarks):
#         for box,probs,ld in zip(boxes,probs,landmarks):
#             cv2.rectangle(frame,
#                             (box[0], box[1]),
#                             (box[2], box[3]),
#                             (0, 0, 255),
#                             thickness=2)

#             cv2.putText(frame, str(probs), (box[2], box[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

#             cv2.circle(frame, tuple(ld[0]), 5, (0,0,255), -1)
#             cv2.circle(frame, tuple(ld[1]), 5, (0,0,255), -1)
#             cv2.circle(frame, tuple(ld[2]), 5, (0,0,255), -1)
#             cv2.circle(frame, tuple(ld[3]), 5, (0,0,255), -1)
#             cv2.circle(frame, tuple(ld[4]), 5, (0,0,255), -1)
#         return frame

#     def run(self):
#         cap = cv2.VideoCapture(0)

#         while True:
#             ret,frame = cap.read()

#             try:
#                 boxes, probs, landmarks = self.mtcnn.detect(frame, landmarks=True) 
#                 self._draw(frame, boxes, probs, landmarks)

#             except:
#                 pass

#             cv2.imshow('Face Detection', frame)

#             if(cv2.waitKey(1) & 0xFF == ord('q')):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

# mtcnn = MTCNN()
# fcd = FaceDetection(mtcnn)
# fcd.run()

import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN
from pynput.keyboard import Key, Controller

keyboard = Controller()

class FaceDetector(object):

    def __init__(self, mtcnn):
        self.mtcnn = mtcnn

    def _draw(self, frame, boxes, probs, landmarks):
        try:
            for box, prob, ld in zip(boxes, probs, landmarks):
                
                cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 0, 255), thickness=3)

                #Forward Block
                cv2.rectangle(frame, (840,10), (430,180),(0,255,0), thickness=3)
                cv2.putText(frame, "Forward", (500, 100), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 198, 13), thickness=2)

                #Forward Left Block
                cv2.rectangle(frame, (140,200), (330,350),(0,255,0), thickness=3)
                cv2.putText(frame, "FL", (190, 290), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), thickness=2)

                #Backward Left Block
                cv2.rectangle(frame, (140,550), (330,450),(0,255,0), thickness=3)
                cv2.putText(frame, "BL", (190, 520), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), thickness=2)

                #Backward Block
                cv2.rectangle(frame, (840,550), (430,700),(0,255,0), thickness=3)
                cv2.putText(frame, "Backward", (500, 670), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 198, 13), thickness=2)

                #Backward Right Block
                cv2.rectangle(frame, (900,550), (1100,450),(0,255,0), thickness=3)
                cv2.putText(frame, "BR", (960, 520), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), thickness=2)

                #Foward Right Block
                cv2.rectangle(frame, (900,200), (1100,350),(0,255,0), thickness=3)
                cv2.putText(frame, "FR", (960, 290), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), thickness=2)

                cv2.circle(frame, (int(ld[2][0]), int(ld[2][1])), 5, (0, 0, 255), -1)

                ###################################################################
                
                #Print Forward value (840,10), (430,180)
                if (ld[2][0] > 430 and ld[2][0] < 840 and ld[2][1] > 10 and ld[2][1] < 180):
                    keyboard.release(Key.space)
                    keyboard.release('d')
                    keyboard.release('a')
                    keyboard.release('s')
                    keyboard.press('w')
                    print("Forward")
                
                #Print Forward Left value (140,200), (330,350)
                elif (ld[2][0] < 330 and ld[2][0] > 140 and ld[2][1] > 200 and ld[2][1] < 350):
                    keyboard.release(Key.space)
                    keyboard.release('d')
                    keyboard.release('s')
                    keyboard.press('w')
                    keyboard.press('a')
                    print("Forward Left")

                #Print Backward Left value (140,550), (330,450)
                elif (ld[2][0] < 330 and ld[2][0] > 140 and ld[2][1] < 550 and ld[2][1] > 450):
                    keyboard.release(Key.space)
                    keyboard.release('d')
                    keyboard.release('w')
                    keyboard.press('s')
                    keyboard.press('a')
                    print("Backward Left")

                #Print Backward value (840,550), (430,700)
                elif (ld[2][0] > 430 and ld[2][0] < 840 and ld[2][1] > 550 and ld[2][1] < 700):
                    keyboard.release(Key.space)
                    keyboard.release('d')
                    keyboard.release('a')
                    keyboard.release('w')
                    keyboard.press('s')
                    print("Backward")

                #Print Backward Right value (900,550), (1100,450)
                elif (ld[2][0] < 1100 and ld[2][0] > 900 and ld[2][1] < 550 and ld[2][1] > 450):
                    keyboard.release(Key.space)
                    keyboard.release('s')
                    keyboard.release('w')
                    keyboard.press('s')
                    keyboard.press('d')
                    print("Backward Right")

                #Print Forward Right value (900,200), (1100,350)
                elif (ld[2][0] < 1100 and ld[2][0] > 900 and ld[2][1] > 200 and ld[2][1] < 350):
                    keyboard.release(Key.space)
                    keyboard.release('a')
                    keyboard.release('s')
                    keyboard.press('w')
                    keyboard.press('d')
                    print("Forward Right")

                else:
                    print("Stop")
                    keyboard.release('w')
                    keyboard.release('s')
                    keyboard.release('a')
                    keyboard.release('d')
                    keyboard.press(Key.space)

        except Exception as e:
            print(e)
            pass

        return frame

    def run(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            try:
                boxes, probs, landmarks = self.mtcnn.detect(frame, landmarks=True)

                self._draw(frame, boxes, probs, landmarks)

            except:
                pass

            cv2.imshow('Face Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
mtcnn = MTCNN()
fcd = FaceDetector(mtcnn)
fcd.run()
