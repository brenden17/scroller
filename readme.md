This is a GUI utility that scrolls two documents in Python.

## Needs.

* Tkinter
* pyautogui 

### install 

 
 On Windows, there are no other modules to install.
 
 On OS X, 

~~~~

 sudo pip3 install pyobjc-framework-Quartz
 sudo pip3 install pyobjc-core
 sudo pip3 install pyobjc.

~~~~
 
 On Linux,
 
~~~~

sudo pip3 install python3-xlib
sudo apt-get install scrot
sudo apt-get install python3-tk
sudo apt-get install python3-dev

~~~~

run pip install pyautogui (or pip3 on OS X and Linux) to install PyAutoGUI.


### Run & how to use

~~~~

python scroll.py

~~~~

push these key to scroll.

~~~~

number key <1> : set left-side document
number key <2> : set right-side document

key <Up> or <k> : scroll two documents down
key <Down> or <j> : scroll two documents up
key <Right> or <l> : scroll right-side documents down
key <Left> or <h> : scroll left-side documents down

key <q> : reverse direction
key <a> : big jump
~~~~

