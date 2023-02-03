""" this is how to get python working in VS code on a MAC. 
Firstly you need to download to VS studios from the internet. Just use thier website. 
Second go to extentions and download python. 
Third open terminal from applications>>utlities>>>terminal. 
Fourth in the terminal type the verison of python you want. Mind out for spaces!
Five type 'import sys'. This will import the system path to the interpriter. Then his enter. 
Six, type print(sys.executable) and hit enter. This will print out the file path for the code. 
Seven copy the executable path that has just been printed. 
Eight, go back to the editor and open up the JSON settings
Nine go to the bottom of the code and put in: "python.PYTHONPATH: (paste path here)"
Ten, close settings and print hellow world test."""
def test():
    if test == True:
        print("is it working?")
    else:
        print("error")
test()