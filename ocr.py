from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib
from tkinter import messagebox
import pytesseract
from sympy import *
import numpy as np
#from scipy.optimize import *
from array import *

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.resize(1038, 521)
		MainWindow.setMaximumSize(QtCore.QSize(1100, 1080))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(280, 40, 291, 21))
		font = QtGui.QFont()
		font.setFamily("Mongolian Baiti")
		font.setPointSize(14)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.textbox = QtWidgets.QTextEdit(self.centralwidget)
		self.textbox.setGeometry(QtCore.QRect(460, 100, 561, 251))
		self.textbox.setObjectName("textbox")
		self.select_img = QtWidgets.QPushButton(self.centralwidget)
		self.select_img.setGeometry(QtCore.QRect(150, 400, 131, 41))
		self.select_img.setObjectName("select_img")
		self.img_txt_btn = QtWidgets.QPushButton(self.centralwidget)
		self.img_txt_btn.setGeometry(QtCore.QRect(680, 400, 131, 41))
		self.img_txt_btn.setObjectName("img_txt_btn")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(810, 470, 201, 21))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic Medium")
		font.setPointSize(9)
		font.setBold(False)
		font.setWeight(50)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.img_lbl = QtWidgets.QLabel(self.centralwidget)
		self.img_lbl.setGeometry(QtCore.QRect(30, 70, 411, 301))
		self.img_lbl.setFrameShape(QtWidgets.QFrame.Box)
		self.img_lbl.setText("")
		self.img_lbl.setObjectName("img_lbl")
		MainWindow.setCentralWidget(self.centralwidget)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.select_img.clicked.connect(self.set_image)
		self.img_txt_btn.clicked.connect(self.im2txt)
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Python OCR"))
		self.label.setText(_translate("MainWindow", "OCR Python GUI Application"))
		self.select_img.setText(_translate("MainWindow", "Select Image"))
		self.img_txt_btn.setText(_translate("MainWindow", "Convert Image To Text"))
		self.label_2.setText(_translate("MainWindow", "Made with <3 @ 2019"))
	def set_image(self):
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files(*.jpg *.jpeg*.png)")
		if fileName:
			pixmap = QtGui.QPixmap(fileName)
			pixmap = pixmap.scaled(self.img_lbl.width(), self.img_lbl.height(), QtCore.Qt.KeepAspectRatio)
			self.img_lbl.setPixmap(pixmap)
			self.img_lbl.setAlignment(QtCore.Qt.AlignCenter) 
            #url = QUrl.fromLocalFile(fileName)
			self.URL_OF_IMG = pathlib.Path(fileName)
	def im2txt(self):
		import argparse
		import cv2
		import os
		try:
			from PIL import Image
		except ImportError:
			import Image
        #import pytesseract
        #pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'OCR', 'Tesseract-OCR', 'tesseract.exe')
        # load the example image and convert it to grayscale
		image = cv2.imread(str(self.URL_OF_IMG))
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
		filename = "{}.png".format(os.getpid())
		cv2.imwrite(filename, gray)
		im = Image.open(filename)
		text = pytesseract.image_to_string(im)
		#x, y = symbols(['x', 'y'])
		#sol = solve([3 * x0 + x1 - 9, x0 + 2 * x1 - 8], [x0, x1])
		text = pytesseract.image_to_string(Image.open(filename))
		os.remove(filename)
		self.textbox.append(text)
		data=self.textbox.toPlainText()

		#data = "".join(data.split())

		l1=[]
		l1.append(data.split('\n'))
		print(l1)
		a=l1[0][0]
		print(a)
		a=a.replace(" ","")
		print(a)
		b=l1[0][1]
		print(b)
		b=b.replace(" ","")
		print(b)


		import numpy as np
		
		
		arr1=[]
		arr2=[]
		arr3=[]

		indx1=a.index('x')-1
		i=a[indx1]
		j=int(i)
		if(a[indx1-1]=='-'):
			j=j*(-1)
		arr1.append(j)
		indy1=a.index('y')-1
		k=a[indy1]
		if(k=='+'):
			k=1
		elif(a[indy1-1]=='-'):
			k=k*(-1)
		l=int(k)
		arr1.append(l)
		print(np.array(arr1)) #arr1 ends here
	



		indx2=b.index('x')-1
		i=b[indx2]
		j=int(i)
		if(a[indx2-1]=='-'):
			j=j*(-1)
		arr2.append(j)
		indy2=b.index('y')-1
		k=b[indy2]
		if(k=='+'):
			k=1
		elif(a[indy2-1]=='-'):
			k=k*(-1)
		
		l=int(k)
		arr2.append(l)
		print(np.array(arr2))#arr2 ends here
		
		inde1=a.index('=')+1
		if(inde1=='-'):
			inde1=a.index('=')+2
		i=a[inde1]
		j=int(i)
		arr3.append(j)
		inde2=b.index('=')+1
		if(inde2=='-'):
			inde2=b.index('=')+2
		k=b[inde2]
		l=int(k)
		arr3.append(l)
		print(np.array(arr3)) #arr1 ends here
		

		A = np.array([ arr1, arr2 ])
		print(A)

		B = np.array(arr3)
		z = np.linalg.solve(A,B)
		print(z[0],z[1])
		str3=''+str(z[0])
		str4=''+str(z[1])
		messagebox.showinfo("x="+str3)
		messagebox.showinfo("y="+str4)

		t1="x="+str(z[0])+"  y="+str(z[1])
		self.textbox.append(t1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    root.mainloop()