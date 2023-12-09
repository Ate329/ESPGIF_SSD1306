# Introduction

**DO NOT RUN THE GIFConvert.py FILE IN THIS FOLDER!!!**

GIFConvert.py is the original file created by [shraiwi](https://github.com/shraiwi).  

GIFConvertNew.py is the modified one.  

You can now select GIF with any size and convert it into any size of GIF.  

GIFConverNew.py will ask you to input the aiming size of GIF after being converted through Tkinter.  

**YOU NEDD TO PUT THE CONVERTED FILE(GIF.h) IN THE SAME FOLDER WITH GIFDisplayNew.ino or GIFDisplay.ino or CHANGE THE CODE DEPENDING ON THE SCREEN YOU HAVE.**  


# Changes
There might be some other changes are not being mentioned.    


## Added
```python
import tkinter.simpledialog as simpledialog
```


## Deleted 
```python
import sys
```
Because it is not used in the entire program.  


## Modifications

### Changed from
```python
    for x in range(resolution[0]):
        for y in range(resolution[1]):
            send(str(frame.getpixel((x, y))) + ",\t")
            counter += 1
            if counter == linelen:
                counter = 0
                send("\n")
```
to
```python
    for x in range(frame.width):
        for y in range(frame.height):
            send(str(frame.getpixel((x, y))) + ",\t")
            counter += 1
            if counter == linelen:
                counter = 0
                send("\n")
```

### Changed from
```python
resolution = (128, 128)
```
to
```python
width = simpledialog.askinteger("Input", "Enter the width of the output")
height = simpledialog.askinteger("Input", "Enter the height of the output")
resolution = (width, height)
```
