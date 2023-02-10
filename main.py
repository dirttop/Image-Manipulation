from PIL import Image, ImageOps
import random
allImages = ["BMW325i.png", "fencer.png", "nausicaa.png", "skater.png", "unite.png"]
selected = ""
print(selected)

#note to drew: haha nerd

#menu 
def colorShift():
  pixels = img.load()
  print("Input your change in color (0 - 2)")
  r = input("r = ")
  g = input("g = ")
  b = input("b = ")
  if (r or g or b > 255):
    print("out of range")
  else:
    print("changing colors... please wait")
    for x in range(img.size[0]):
      for y in range(img.size[1]):
        rgb = img.getpixel((x,y))
        newrgb = (rgb[int(r)], rgb[int(g)], rgb[int(b)])
        pixels[x, y] = newrgb

    img.save('updated/modified.png')
    print("updated! check the photo in the updated folder!")

def diagonalLines():
  pixels = img.load()
  thickness = [0, 1, 2, 3, 4, 5, 6]
  print("What color would you like the lines to be? (0 - 255)")
  r = input("r = ")
  g = input("g = ")
  b = input("b = ")
  if (int(r) > 255 or int(g) > 255 or int(b) > 255):
    print("out of range")
  else:
    for x in range(img.size[0]):
      for y in range(img.size[1]):
        if ((x-y)%30 in thickness):
          rgb = (int(r), int(g), int(b))
          pixels[x, y] = rgb
    img.save('updated/modified.png')
    print("updated! check the photo in the updated folder!")

def border():
  imgBorder = ImageOps.expand(img,border=100,fill='black')
  imgBorder.save('updated/modified.png')
  print("updated! check the photo in the updated folder!")


print("Welecome to the Gleb Syomichev Epic Image Manipulation Software!")
print(allImages)
imgSelect = input("Choose an image 1 - 5! Select 6 to modify the last modified image\n")
while True:
  if (imgSelect == "1" or "2" or "3" or "4" or "5"):
    if (imgSelect == "1"):
      selected = allImages[0]
      print(selected)
    if (imgSelect == "2"):
      selected = allImages[1]
      print(selected)
    if (imgSelect == "3"):
      selected = allImages[2]
      print(selected)
    if (imgSelect == "4"):
      selected = allImages[3]
      print(selected)
    if (imgSelect == "5"):
      selected = allImages[4]
      print(selected)
    if (imgSelect == "6"):
      selected = "updated/modified.png"
  break
img = Image.open(selected)
img.show()

print("What filter would you like to apply?")
choice = input("1. Color Change \n2. Diagonal Lines \n3. Border\n")
if (choice == "1" or "2" or "3"):
  if (choice == "1"):
    colorShift()
  if (choice == "2"):
    diagonalLines()
  if (choice == "3"):
    border()