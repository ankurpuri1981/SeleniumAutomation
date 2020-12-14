import os
import sys
os.chdir("..")
#os.getcwd() + "\\TestData\\testData.xlsx"
from shutil import copyfile
#print(os.path.dirname(sys.executable))
copyfile('chromedriver.exe', str(os.path.dirname(sys.executable))+ "\\chromedriver.exe")