from PIL import Image
import os

import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

text = open('out.txt', mode='w', newline=None)

def send(msg):
    text.write(msg)

def to565(color):
    r, g, b = color
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | ((b & 0xF8) >> 3)

def string565(color):
    return hex(to565(color))

linelen = 30;

root = tk.Tk()
root.withdraw()

width = simpledialog.askinteger("Input", "Enter the width of the output")
height = simpledialog.askinteger("Input", "Enter the height of the output")
resolution = (width, height)

path = filedialog.askopenfilename(title = "Select GIF")

im = Image.open(path)

palette = im.getpalette()

send("/* Here is the converted version of the GIF!\n")
send(" * Converted using GIF2BYTE <3\n")
send(" * Copy this text into your program!*\n")
send(" * Original version: https://github.com/shraiwi/ESPGIF*\n")
send(" * Modified version: https://github.com/Ate329/ESPGIF_SSD1306*/\n")

send("\n#define NUM_FRAMES " + str(im.n_frames))

delay = 2000 / im.n_frames - (im.n_frames * 40)

if delay < 0:
    delay = 0;
    print("The GIF will not play at native speed, but at the max possible framerate.")

send("\n#define DELAY " + str(delay) + "\n\n")

colors = list(chunks(palette, 3))

print("generating palette...")

send("const uint16_t palette[] PROGMEM = {\n")

counter = 0

for value in colors:
    send(string565(value) + ",\t")
    
    counter += 1
    
    if counter == linelen:
        counter = 0
        send("\n")

send("\n};")

kb = (resolution[0] * resolution[1] * 1 * im.n_frames + 255) / 1024

print("size: " + str(kb) + " KiB.")

large = False

if kb > 700:
    large = True
    print("warning: might not fit into ESP8266 flash")

send("\nconst uint8_t frameData[][" + str(resolution[0] * resolution[1]) + "] PROGMEM = {\n")

for n in range(im.n_frames):

    im.seek(n)

    frame = im.resize(resolution)

    frame = frame.transpose(Image.FLIP_LEFT_RIGHT)
    frame = frame.transpose(Image.ROTATE_90)
    
    # frame.save('frames/img' + str(n) + '.png')

    print("converting frame" + str(n))

    send("/* Frame " + str(n) + " */\n{\n")

    counter = 0
    
    for x in range(frame.width):
        for y in range(frame.height):
            send(str(frame.getpixel((x, y))) + ",\t")
            counter += 1
            if counter == linelen:
                counter = 0
                send("\n")
            

    send("},\n")

send("\n};")

text.close()

os.startfile('out.txt')

with open('out.txt', 'r') as file:
    content = file.read()
file.close()

output_directory = './GIFDisplay'
output_file_path = os.path.join(output_directory, 'GIF.h')

# Use an absolute path for the output file
output_file_path = os.path.abspath(os.path.join(output_directory, 'GIF.h'))

# Create the directory if it doesn't exist
try:
    os.makedirs(output_directory)
except FileExistsError:
    pass  # Directory already exists

# Open the file for writing
try:
    with open(output_file_path, 'w') as file:
        file.write(content)
    print(f"File '{output_file_path}' successfully created.")
except Exception as e:
    print(f"Error creating the file '{output_file_path}': {e}")


print("complete!")
