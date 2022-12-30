import numpy as np
from PIL import Image
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import os
while(True):
    print("Resim Yuklemek İcin 1e:")
    print("Siyah Beyaza Cevirmek icin 2ye:")
    print("Resmi Kirpmak icin 3e")
    print("Cikis yapmak icin 4e")
    print("Resme ayna efekti uygulamak icin 5e Basın")
    x=int(input(":"))
    if x==1:
        root = tk.Tk()
        root.withdraw()
        filename=(filedialog.askopenfilename())
        image = Image.open(filename)
        npImage = np.array(image)
        a=np.array(image)
        sutun,satir=image.size
    if x==2:
        try:
            npImage
        except NameError:
            print("Dosya yuklemeden bu secenegi secmeyin")
            continue;
        npImage=np.array(image)
        for i in range(0,satir):
            for j in range(0,sutun):
                for k in range (0,3):
                    if k==0:
                        x=npImage[i,j,k]*0.2989
                    if k==1:
                        y=npImage[i,j,k]*0.5870
                    if k==2:
                        z=npImage[i,j,k]*0.1140
                        npImage[i,j]=x+y+z
                        
        sbImage= Image.fromarray(npImage)
        sbImage.show()
        file=os.path.basename(filename)
        t=os.path.splitext(file)[0]
        r=(t+"_sb")
        sbImage=sbImage.save(r+".jpg")
    if x==3:
        try:
            npImage
        except NameError:
            print("Dosya yuklemeden bu secenegi secmeyin")
            continue;
        npImage=np.array(image)
        solx=0
        soly=0
        sagx=0
        sagy=0
        npImage=np.array(image)
        print("Sol Ust Kosesinin x degerini girin")
        solx=int(input(":"))
        print("Sol Ust Kosenin y degerini girin")
        soly=int(input(":"))
        print("Sag alt Kosesinin x degerini girin")
        sagx=int(input(":"))
        print("Sag alt Kosenin y degerini girin")
        sagy=int(input(":"))
        if sagx<solx or sagy<soly:
            print("Gecersiz deger girdiniz:")
            continue;

        for i in range(satir):
            for j in range(sutun):
                if i<solx or j <soly or i>sagy or j>sagx:
                    npImage[i,j]=255
        sbImage=Image.fromarray(npImage)
        sbImage.show()
        file=os.path.basename(filename)
        t=os.path.splitext(file)[0]
        r=(t+"_kirpilmis")
        sbImage=sbImage.save(r+".jpg")
    if x==4:
        break;
    if x ==5 :
        try:
            npImage
        except NameError:
            print("Dosya yuklemeden bu secenegi secmeyin")
            continue;
        npImage=np.array(image)
        for o in range(0,satir):
            for m in range (0,sutun):                
                    a[o,(sutun-1)-m]=npImage[o,m]   
        
        sbImage=Image.fromarray(a)
        sbImage.show()
        file=os.path.basename(filename)
        t=os.path.splitext(file)[0]
        r=(t+"_yatay")
        sbImage=sbImage.save(r+".jpg")
                    
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                