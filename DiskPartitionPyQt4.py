import os  #importing os module 
import sys 
from PyQt4.QtCore import * #importing pyqt4 
from PyQt4.QtGui import *  #importing pyqt4 gui
 
def main():    #main function
    app = QApplication(sys.argv) 
    w = MyWindow()  #initialising window     
    w.show() 	    #displaying window
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

	
        # create objects
        label = QLabel(self.tr("Press Enter To View Disk Partition Details "))   
	#setting non-editable text to display window purpose
        self.le = QLineEdit("sudo fdisk -l")					 
	#setting a line edit text box to linux command ( editable text )
        self.te = QTextEdit()							 
	#text box to display excecuted linux command ( to view disk partion)


        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 

        # create connection
        self.connect(self.le, SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        cmd = str(self.le.text())	
	#excecuting linux command to string cmd
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)	
	#setting text of textbox to excecuted linux comand
	self.showMaximized()  
	#maximises window when run 
  
if __name__ == "__main__": 
    main()

