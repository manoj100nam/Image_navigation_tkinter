from tkinter import *
import os
from PIL import ImageTk,Image

root= Tk()

#Creating List of images from Root directonry
imgList=[]
for (root_, dirs, files)in os.walk('img/', '.jpg'):
    if files:
        for file in files:
            path = os.path.join('img/', file)
            image = Image.open(path)
            img = image.resize((300, 300))
            photo = ImageTk.PhotoImage(img)
            imgList.append(photo)


# Global Label for Both forward & backward
def labelFunc():
    global label1
    label1.grid_forget()
    label1 = Label(root, image=imgList[currentImageIndex])
    label1.grid(row=0, column=0, columnspan=3)


#Defining Forward function
def forward(imageNo):
    global currentImageIndex
    currentImageIndex = imageNo
    if imageNo != len(imgList) - 1:
        currentImageIndex+=1
    else:
        currentImageIndex=0
    labelFunc()


#Defining Backward function
def backward(imageNo):
    global currentImageIndex
    currentImageIndex = imageNo
    if currentImageIndex != -3:
        currentImageIndex -=1
    else:
        currentImageIndex = 2
    labelFunc()


# On app starting default value of image index will be 0
currentImageIndex = 0
label1= Label(root, image=imgList[0])
label1.grid(row=0, column=0, columnspan=3)
Button(root, text='Back', command= lambda :backward(currentImageIndex)).grid(row=1, column=0, ipadx=12, pady=10)
Button(root, text='Quit', command=root.quit).grid(row=1, column=1, ipadx=12)
Button(root, text='Forward', command= lambda :forward(currentImageIndex)).grid(row=1, column=2)

root.mainloop()

