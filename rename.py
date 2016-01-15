import os,sys
folder = "C:\\Users\\mattg\\Desktop\\diagnostic-files.PS65158-2299.2015-04-16T10-52-16\\server\\data\\printers"
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       newname = infilename + (".xml")
       os.rename(infilename, newname)
