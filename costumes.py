import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)