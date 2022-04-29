from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QListWidget
from PyQt5.QtCore import *

from Decrypt_Username_and_Password import mainDecrypteFun
from Encrypt_Username_and_Password import encryptUsername, encryptPassword
from writeSavedPasswords import writeSavedPasswords
from GenDecrypt import genDecrypt
import sys
import time


class MyWindow(QMainWindow):
    PTEusr=None
    PTEpas=None
    PTEuseLower=None
    PTEpasLower=None


    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(720,360,500,400)
        self.setWindowTitle('Password Saver')
        self.setFixedSize(500,300)
        self.initUI()
        self.colors()
        self.update()

            
    def initUI(self):    
        self.mainLabelTop=QtWidgets.QLabel(self)
        self.mainLabelBot=QtWidgets.QLabel(self)
        self.mainList=QListWidget(self)
        self.resetLabel=QtWidgets.QLabel(self)

        self.mainLabelTop.setText('''
        Click Button and Enter Credentials 
        ''')
        self.mainLabelBot.setText('''
        If this is your first time please create a username and password by Clicking Button Below
        ''')
        self.mainLabelTop.adjustSize()
        self.mainLabelTop.move(150,100)
        self.mainLabelBot.adjustSize()
        self.mainLabelBot.move(10,100)
   

        self.resetLabel.setText('''
        Click below to reset username and password
        All current data will be lost
        ''')
        self.resetLabel.move(0,225)
        self.resetLabel.setAlignment(Qt.AlignCenter)

        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText('OK')
        self.b1.move(200,135)
        self.b1.clicked.connect(self.clicked)

        self.b2=QtWidgets.QPushButton(self)
        self.b2.setText('Enter and Save')
        self.b2.move(200,135)
        self.b2.clicked.connect(self.clickedLower)

        self.bReset=QtWidgets.QPushButton(self)
        self.bReset.setText('Reset')
        self.bReset.move(75,265)
        self.bReset.clicked.connect(self.resetdata)
        self.update()

        self.bS1=QtWidgets.QPushButton(self)
        self.bS1.setText('Add New')
        self.bS1.move(395,265)
        self.bS1.hide()
        self.bS1.clicked.connect(self.addSavedPasswords)


        self.mainList.setFixedSize(500,300)
        self.mainList.hide()


    def clicked(self):
        
        Username,Password=mainDecrypteFun()
        Username=Username[:-1]

        self.PTEusr=QtWidgets.QInputDialog.getText(
            self,'Username Input','Enter Your Username')
        self.PTEpas=QtWidgets.QInputDialog.getText(
            self,'Password Input','Enter Your Password')
        self.update()

        PTEusr=self.PTEusr[0]
        PTEpas=self.PTEpas[0]
        if PTEusr==Username and PTEpas==Password:
            self.b1.hide()
            self.b2.hide()
            self.mainLabelTop.hide()
            self.bS1.show()
            self.mainList.show()
            self.bReset.hide()
            self.resetLabel.hide()

            self.readsaves()
            self.insertList()


    def clickedLower(self):
        self.PTEusrLower=QtWidgets.QInputDialog.getText(
            self,'Username Input','Create Username')
        self.PTEpasLower=QtWidgets.QInputDialog.getText(
            self,'Password Input','Create Password')

        PTEusrLower=self.PTEusrLower[0]
        PTEpasLower=self.PTEpasLower[0]
        if PTEusrLower.isspace() or PTEpasLower.isspace():
            self.resetdata()
        encryptUsername(PTEusrLower)
        encryptPassword(PTEpasLower)
        self.clock()


    def update(self):
        self.mainLabelTop.adjustSize()
        self.mainLabelBot.adjustSize()
        self.mainList.adjustSize()
        self.resetLabel.adjustSize()

        outFile=open('Code\passwordData.txt','r')
        lines=outFile.readlines()
        if lines:
            self.b2.hide()
            self.mainLabelBot.hide()
            self.resetLabel.show()
            self.bReset.show()
            self.b1.show()
            self.mainLabelTop.show()
        else:
            self.bReset.hide()
            self.resetLabel.hide()
            self.b1.hide()
            self.mainLabelTop.hide()


    def addSavedPasswords(self):
        self.website=QtWidgets.QInputDialog.getText(
            self,'Website Input','Enter The Website Name')
        
        self.username=QtWidgets.QInputDialog.getText(
            self,'Username Input','Enter The Username Used')
        
        self.password=QtWidgets.QInputDialog.getText(
            self,'Password Input','Enter The Password Used')
        
        writeSavedPasswords(self.website[0],self.username[0],self.password[0])
        time.sleep(.01)
        self.mainList.clear()
        self.readsaves()
        self.insertList()


    def resetdata(self):
        file1=open('Code\savedPassword.txt','r+')
        file1.truncate(0)
        file1.close()
        
        file2=open('Code\savedPassword.txt','r+')
        file2.truncate(0)
        file2.close()
        sys.exit()


    def insertList(self):
        for i in range(len(self.called)):
            self.mainList.insertItem(i,self.called[i])
        self.mainList.show()


    def readsaves(self):
        self.mainFile=open('Code\savedPassword.txt','r')
        self.mainFileLines=self.mainFile.readlines()
        self.mainFile.close()
        
        self.called=[]
        for i in range(len(self.mainFileLines)):
            lineTaken=genDecrypt(self.mainFileLines[i])
            self.called.append(lineTaken)


    def clock(self):
        time.sleep(.01)
        self.update()


    def colors(self):
        self.setStyleSheet('background-color: gray;')
        self.mainLabelTop.setStyleSheet('color: white')
        self.mainLabelBot.setStyleSheet('color: white')
        self.resetLabel.setStyleSheet('color: white')

        self.b1.setStyleSheet('color: white')
        self.b2.setStyleSheet('color: white')
        self.bReset.setStyleSheet('color: white')
        self.bS1.setStyleSheet('color: white')

        self.mainList.setStyleSheet('color: white')

def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())


window()