from setuptools import setup

l_d = '''
Electron is a technology developed by https://www.github.com/ . Which you can use 
to render html5 and javascript as a desktop app . But it uses node js . I have used 
PyQt5 for the shell and it is written with pure python so enjoy . For documentation visit
http://github.com/nishowsan/python-electron .
'''

setup(name='pytron',
      version='1.0',
      description='Make desktop app with html5 and JS using python and pytron',
      long_description=l_d,
      url='http://github.com/nishowsan/python-electron',
      author='Adib Mohsin',
      author_email='md.nishow@gmail.com',
      license='MIT',
      packages=['pytron'],
      requires= ['pyqt5'],
      zip_safe=False)