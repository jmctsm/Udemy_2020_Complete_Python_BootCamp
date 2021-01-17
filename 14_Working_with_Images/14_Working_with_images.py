from PIL import Image

mac = Image.open("example.jpg")

# Note this is a specialized file type from PIL (pillow)
print(type(mac))

# uncomment to show the actual file.  Commented out so that I can move forward without opening it every dang time
#mac.show()

# Image information
# (width, height)
print(mac.size)

print(mac.filename)

print(mac.format_description)

# Cropping Images
#mac.crop((0,0,100,100)).show()
#mac.show()

pencils = Image.open("pencils.jpg")
# pencils.show()

print(pencils.size)

# Start at the top corner (0,0)
x = 0
y = 0
# Grab about 10% in y direction, and about 30% in x direction
w = 1950/3
h = 1300/10

#pencils.crop((x,y,w,h)).show()
#pencils.show()

print(pencils.size)

# Crop starting at the bottom
x = 0
y = 1100
w = 1950/3
h = 1300

# pencils.crop((x,y,w,h)).show()

# get the MAC only
print(mac.size)

halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257

#mac.crop((x,y,w,h)).show()

# Copying and pasting Images

# Only happening in memory
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))
# mac.show()
mac.paste(im=computer,box=(796,0))
#mac.show()

print(mac.size)
h,w = mac.size
new_h = int(h/3)
new_w = int(w/3)

# Note this is not a permanent change
# for permanent change, do a reassignment
# e.g. mac = mac.resize((100,100))
#mac.resize((new_h,new_w)).show()
#mac.resize((3000,500)).show()

# rotating images
#pencils.rotate(90).show()
# pencils.rotate(90,expand=True).show()
#pencils.rotate(120).show()
#pencils.rotate(120,expand=True).show()


#Transparency
red = Image.open('red_color.jpg')
#red.show()
blue = Image.open('blue_color.png')
#blue.show()

red.putalpha(128)
#red.show()
blue.putalpha(128)
#blue.show()
blue.paste(im=red,box=(0,0),mask=red)
#blue.show()

# Saving Images
blue.save("purple.png")
purple = Image.open("purple.png")

purple.show()