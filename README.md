# python-electron
### Make desktop app with html5 and JS using python and pytron
Electron is a technology developed by [Github](https://www.github.com). Which you can use 
to render html5 and javascript as a desktop app . But it uses node js . I have used 
PyQt5 for the shell and it is written with pure python so enjoy . 

# Note
The code is beta and the idea is new . The project will be continuous . Please report issue . 

# Install
Installing pytron is very easy . 
## Windows
Open your cmd as administrator and type the following
<code> pip install pytron </code>
<hr>
## Linux
Open your terminal with <code> Ctrl + Alt + T </code> and then
<code> sudo pip install pytron </code>

# Docs
Pytron was mainly built in order to serve html5 file with a simple pyqt shell that acts like a desktop application
```python
import os
import pytron as pt

# setting the title via predefined variable 
pt.TITLE = 'App'

# htmlFile name can be saved via the variable htmlFile . os.path.join() is used for absolute file path
pt.htmlFile = pt.handler + os.path.join('index.html')

window = pt.BrowserWindow()
window.show() # show or execute the main Window

# Finally execute the file
if __name__ == '__main__':
  pt.app.exec_()
```


