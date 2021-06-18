from PIL import Image

cactus = Image.open("cactus.jpg")
beach = Image.open("beach.jpg")

cactus_pixels = cactus.load()
beach_pixels = beach.load()


red = 0
green = 0
blue = 0

for x in range(0, 800): 
    for y in range (0, 600): 
        red, green, blue = cactus_pixels[x, y]
        
        if green != 244 and red != 76 and blue != 24:
            beach_pixels[x, y] = (red, green, blue)

beach.show()

cactus.save("cactusonbeach.jpg")