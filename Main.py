import errno
from msilib.schema import Error
import qrcode as qr 
import cmath
import math
import os



from PyQt6 import uic,QtWidgets

def CalcPolRect():
    Mod=QrcodeTela.Mod.text()
    angle=QrcodeTela.Angle.text()
    if(Mod=="" or angle==""):
        QrcodeTela.status.setText("Os campos Não Podem Estar Vazios")
    elif(any(chr.isdigit() for chr in Mod))==False:
        QrcodeTela.status.setText("Os campos devem ser números")
    elif(any(chr.isdigit() for chr in angle))==False:
        QrcodeTela.status.setText("Os campos devem ser números")
        
    
    else:
        try:
            Mod=float(QrcodeTela.Mod.text())
            angle=float(QrcodeTela.Angle.text())
            QrcodeTela.status.setText("")
            real=round((math.cos(math.radians(angle))*Mod),3)
            img=round((math.sin(math.radians(angle))*Mod),3)
            #img=img*1j
            resposta="( "+str(real) + " , " +str(img)+" J )"
            print(resposta)
            QrcodeTela.Resp1.setText(resposta)
            
        except:
            QrcodeTela.status.setText("Falha ao realizar conversão")
            QrcodeTela.Resp1.setText("Falha")
      
    
def CalcRectPol():
    Real=QrcodeTela.real.text()
    Img=QrcodeTela.img.text()
    if(Real=="" or Img==""):
        QrcodeTela.status.setText("Os campos Não Podem Estar Vazios")
    elif(any(chr.isdigit() for chr in Real))==False:
        QrcodeTela.status.setText("Os campos devem ser números")
    elif(any(chr.isdigit() for chr in Img))==False:
        QrcodeTela.status.setText("Os campos devem ser números")
    else:   
        try:
            Real=float(QrcodeTela.real.text())
            Img=float(QrcodeTela.img.text())
            Z=complex(Real,Img)
            Polar=cmath.polar(Z)
            resposta1=str(round(Polar[0],3))+"  /_"+str(round(((Polar[1]*180)/cmath.pi),3))+"°"
            QrcodeTela.Resp2.setText(resposta1)
            print(resposta1)
            print("RectPol")
            
        except: 
            QrcodeTela.status.setText("Falha ao realizar conversão")
            QrcodeTela.Resp2.setText("Falha")
        


app=QtWidgets.QApplication([])
QrcodeTela=uic.loadUi("Main.ui")
QrcodeTela.btnPolRect.clicked.connect(CalcPolRect)
QrcodeTela.btnRectPol.clicked.connect(CalcRectPol)
#QrcodeTela.actionSalva.triggered.connect(salvar)

QrcodeTela.show()
app.exec()