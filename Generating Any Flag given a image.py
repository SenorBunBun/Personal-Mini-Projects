from PIL import Image, ImageDraw, ImageDraw2

# Was planning to add an array and shape it using numpy but it didn't work because I was testing using gifs at the time.
# I removed that portion of the code because I thought it was numpy and I forgot to reimplement it.
import numpy

# V1 Notes: version used to submit the Japan picture (one on the flag assignment). I kept the portions of the code which
# I forgot to remove when making the actual Japan picture.
# This version of the program is having a simple time dealing with simple designs like japan, or france
# but when it gets to more complicated flags it starts to break down and draw less accurately.

# this program, due to the lack of accessible rgb information in gif you must use jpg and pngs, at this point I have
# only tested with jpgs but should work with pngs
print("this program, due to the lack of accessible rgb information in gif you must use jpg and pngs ")

# the reason they are split up in this weird order is because when using hardcoded values when i type "\a" or other like
# it doesn't register as a normal string and counts as a escape sequence character
folderpath = input("Enter the path to your folder containing your file [including \ at the end] : ")
extension = input("Enter what type of image is it (.jpg .gif. png) ")
imagename = input("Enter your filename (without extension) : ")


# some hardcoded presets so when debugging and testing I don't have to keep typing the input info
# imagename = "japan"
# folderpath = "D:\Downloads"
# extension = ".jpg"

# sets the image path by concatenating the strings
ogimage = Image.open(folderpath + imagename + extension)

# The flags are available in many aspect ratios and I was wanting to make the file smaller so my computer has an easier
# time going through and iterating the pixel data. Some of the images were 2000 x 2000 and I didn't want to deal with
# that issue. This causes most flags to be distorted in a way so in v2 will try to add a conditional here. Sets a tuple
# for the size.
(width, height) = (144, 80)

# resizes the image and takes the rgb details and puts it in a list.
ogimage = ogimage.resize((width, height), Image.ANTIALIAS)
rgbvals = ogimage.load()

# a option I use for debugging so I can see the actual small image where the data is coming from and compare that to
# what the program outputs.
ogimage.save(folderpath+imagename+"small"+extension)

# making and filling a empty image with a white color
outputflag = Image.new("RGB", (144, 80), (254, 254, 254))
outputflag.paste((254, 254, 254), [0, 0, outputflag.size[0], outputflag.size[1]])

# setting a variable draw so I canb remove some repition of statements
draw = ImageDraw.Draw(outputflag)

# starts the x-value and isn't changed in the for loop so it can stay out of it
x = 0

# the program processes the image horizontally from top to down. I didn't hardcode the values for the height and width
# so I can update the program later easier. The coordinate system they use for accessing the images is a bit weird.
for y in range(0, height):

    # sets the color of the first point to a value and redefines the start and endpoints
    tempfill = rgbvals[x, y]
    startpoint = (x, y)
    endpoint = (x, y)

# the bulk of the program where it generates most of the drawing commands, used tempx because I didn't want to change
# the variable x's value. Just starts going through whatever row of pixels placed at the y-coordinate.The program is
# set to always start from the left so it just goes right.
    for tempx in range(x, width - 1):

        if tempfill == rgbvals[tempx - 1, y]:
            endpoint = (tempx, y)
        else:
            draw.line([startpoint, endpoint], fill=tempfill, width=1)
            startpoint = (tempx, y)
            tempfill = rgbvals[tempx, y]

    #another debugging tool to just saving the image every 2 rows so I can analyze the programs process for debugging,
    #creates many versions of the pngs.
    if y % 2 == 0:
        outputflag.save(folderpath + imagename + str(y + 4) + extension)

#saves the3 output with recreation3 at the end
outputflag.save(folderpath + imagename + "recreation3" + extension)
