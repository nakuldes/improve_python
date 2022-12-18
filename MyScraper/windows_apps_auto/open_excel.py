import win32com.client

import subprocess
import os
import sys

# subprocess.Popen("C:\Program Files (x86)\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe")

SapGuiAuto = win32com.client.GetObject("Excel.Application")
application = SapGuiAuto.GetScriptingEngine #This        
connection = application.OpenConnection(sys, True) #This        

#print "some"                
session = connection.Children(0)



