import sys
import cv2
import numpy as np
from cv2 import boundingRect, countNonZero, cvtColor, drawContours, findContours, getStructuringElement, imread, morphologyEx, pyrDown, rectangle, threshold
from PIL import Image
import os
import time
from pytesseract import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer, Qt



class MyWindow(QWidget):
    
   
    
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.file_name = ""
        self.step = 0
            
    def setupUI(self):
        self.setGeometry(400,400,600,400)
        self.setWindowTitle("임베디드")

        self.imglabel = QLabel()
        self.label = QLabel()
        self.uploadButton = QPushButton("업로드")
        self.uploadButton.clicked.connect(self.uploadButtonClicked)
        
        self.captureButton = QPushButton("캡처")
        self.captureButton.clicked.connect(self.captureButtonClicked)
        

        self.pbar = QProgressBar()
        self.convertButton = QPushButton("변환")
        self.convertButton.clicked.connect(self.convertButtonClicked)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.imglabel)
        layout.addWidget(self.label)
        layout.addWidget(self.captureButton)
        layout.addWidget(self.uploadButton)
        layout.addWidget(self.pbar)
        layout.addWidget(self.convertButton)

        self.setLayout(layout)

    def uploadButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])
        text = fname[0]
        text_list = text.split('/')
        self.file_name = text_list[4]
        pixmap = QPixmap(fname[0])
        self.imglabel.setPixmap(pixmap)
        
    def convertButtonClicked(self):
        self.transform(self.file_name)
        
    def captureButtonClicked(self):
        cam = cv2.VideoCapture(0)
        while(cam.isOpened()):
            ret, image = cam.read()
            if ret == True:
                cv2.imshow('Camera', image)
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyWindow('Camera')
                    cv2.imwrite('Image.jpg',image)
                    cam.release()
                    self.file_name = 'Image.jpg'
                    self.label.setText('Image.jpg')
                    pixmap = QPixmap('Image.jpg')
                    self.imglabel.setPixmap(pixmap)
                    break
                
    def ifcomplete(self):
        result = QMessageBox.information(self, "Information", "변환 완료")
        if result == QMessageBox.Ok:
            self.pbar.reset()
        
    def transform(self,file_name):
        str_list = []
        img = cv2.imread(file_name)
        
        rgb = img
        rgb1 = img

        # 그레이스케일 적용
        image = cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        # 커널 매트릭스 만들기 (ELLIPSE = 타원형으로 매트릭스 생성)
        morph_kernel = getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        grad = morphologyEx(image, cv2.MORPH_GRADIENT, morph_kernel)
        # 이진화
        _, bw = threshold(src=grad, thresh=0, maxval=255, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        dilate = cv2.dilate(bw, morph_kernel, iterations = 5)
        # 커널 매트릭스 만들기 (RECT = 사각형으로 매트릭스 생성)
        morph_kernel = getStructuringElement(cv2.MORPH_RECT, (9, 1))
        #작은 구멍을 메우고 경계를 강화
        connected = morphologyEx(dilate, cv2.MORPH_CLOSE, morph_kernel)
        
        mask = np.zeros(bw.shape)
        #이진화된 이미지에서 윤곽선 찾기
        contours, hierarchy = findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        
        for idx in range(len(contours)):
            #인자로 받은 윤곽을 외접하고 똑바로 세워진 직사각형의 좌표 값 리턴
            x, y, w, h = cv2.boundingRect(contours[idx])
            #검출된 윤곽선이 저장된 Numpy배열
            mask[y:y+h, x:x+w] = 0
            #검출된 윤곽선 그리기
            cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
            r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

            if r > 0.45 and w > 15 and h > 15:
                 
                 rgb = cv2.rectangle(rgb, (x, y+h), (x+w, y), (0,255,0),3)
                 crop = rgb1[y:y+h+3,x:x+w+3]
                 str_list.append(crop)
               
        cv2.imwrite("result.jpg",rgb)
        f=open('convert.hwp','w')

        x = len(str_list)
        y = 100/x
        self.step = 0
        for i in range(x):
            text = image_to_string(str_list[i-1], lang="kor+eng")
            f.write(text[:len(text)-1])
            
            self.step = self.step + y
            self.pbar.setValue(self.step)
            
        self.ifcomplete()
        f.close()           
 
        

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = MyWindow()
    wd.show()
    app.exec_()

    

